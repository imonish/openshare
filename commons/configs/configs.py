import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from abc import ABC, abstractmethod

class BaseSecretProvider(ABC):
    """
    All secret providers must implement this interface.
    """

    @abstractmethod
    def get(self, key: str, default=None):
        pass


class LocalEnvProvider(BaseSecretProvider):
    """
    Loads secrets from local .env file (development mode).
    """

    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        env_path = base_dir / ".env"

        load_dotenv(env_path)

    def get(self, key: str, default=None):
        return os.getenv(key, default)



class VaultProvider(BaseSecretProvider):
    """
    Loads secrets from Hashicorp Vault.
    """

    def __init__(self, url: str, token: str, path: str):
        self.url = url
        self.token = token
        self.path = path

        self.cache = self._load_secrets()

    def _load_secrets(self):
        headers = {"X-Vault-Token": self.token}

        response = requests.get(
            f"{self.url}/v1/{self.path}",
            headers=headers
        )

        response.raise_for_status()
        return response.json()["data"]

    def get(self, key: str, default=None):
        return self.cache.get(key, default)



class ConfigManager:
    """
    ConfigManager selects the secret provider
    based on SECRET_PROVIDER value.
    """

    def __init__(self):
        print("Initializing ConfigManager...")
        provider = os.getenv("SECRET_PROVIDER", "local")

        if provider == "local":
            print("Using LocalEnvProvider...")
            self.client = LocalEnvProvider()

        elif provider == "vault":
            print("Using VaultProvider...")
            self.client = VaultProvider(
                url=os.getenv("VAULT_URL"),
                token=os.getenv("VAULT_TOKEN"),
                path=os.getenv("VAULT_PATH"),
            )

        else:
            print("Unsupported SECRET_PROVIDER specified.")
            raise ValueError(
                f"Unsupported SECRET_PROVIDER: {provider}"
            )

    def get(self, key: str, default=None, data_type=str):
        """
        Unified access method.
        """
        value = self.client.get(key, default)
        if data_type == int:
            return int(value) if value is not None else default
        elif data_type == float:
            return float(value) if value is not None else default
        elif data_type == bool:
            return value.lower() in ("true", "1", "yes") if isinstance(value, str) else bool(value)
        elif data_type == list:
            return value.split(",") if isinstance(value, str) else list(value)
        elif data_type == dict:
            import json
            return json.loads(value) if isinstance(value, str) else dict(value)
        return value



config = ConfigManager()


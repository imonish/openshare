# Contributing to OpenShare

Thank you for considering contributing to **OpenShare** 🎉  
OpenShare is an open-source platform for event photographers to manage and share photos securely with guests.

We welcome all contributions including:

- Bug fixes
- Feature improvements
- Documentation updates
- New feature suggestions

---

## 📌 How to Contribute

### 1. Fork the Repository

Click the **Fork** button on GitHub, then clone your fork:

```bash
git clone https://github.com/c4d1/openshare.git
cd openshare
```

---

### 2. Create a Branch

Create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
```

---

### 3. Setup the Project Locally

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

---

### 4. Make Changes

* Follow Django best practices
* Keep code clean and readable
* Add comments where necessary
* Update documentation if required

---

### 5. Run Tests (If Available)

Before submitting, ensure the project runs correctly:

```bash
python manage.py test
```

---

### 6. Commit Your Changes

Write clear commit messages:

```bash
git add .
git commit -m "Add: feature description"
```

---

### 7. Push and Open a Pull Request

Push your branch:

```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub.

---

## ✅ Contribution Guidelines

* Keep pull requests focused and small
* Ensure code is properly formatted
* Avoid committing sensitive data (API keys, secrets)
* Discuss major changes via GitHub Issues first

---

## 💡 Feature Requests / Bugs

If you find a bug or want to suggest a feature:

* Open an issue in the GitHub Issues tab
* Provide clear steps or explanation

---

## 📄 Code of Conduct

By participating, you agree to follow respectful and inclusive community behavior.

---

Thank you for helping build OpenShare ❤️
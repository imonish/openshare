from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError

from commons.notifications import send_discord_alert


def health_check(request):
    try:
        connections["default"].cursor()
        return JsonResponse(
            {
                "status": "ok",
                "database": "ok",
            }
        )
    except OperationalError:
        send_discord_alert("Database connection failed ❌")

        return JsonResponse(
            {
                "status": "error",
                "database": "error",
            },
            status=500
        )

from datetime import datetime
from zoneinfo import ZoneInfo
import requests

MY_LAT = 44.8125
MY_LONG = 20.4612

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

try:
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters, timeout=5
    )
    response.raise_for_status()
    data = response.json()

    belgrade_tz = ZoneInfo("Europe/Belgrade")

    sunrise_utc = datetime.fromisoformat(data["results"]["sunrise"])
    sunset_utc = datetime.fromisoformat(data["results"]["sunset"])

    sunrise_local = sunrise_utc.astimezone(belgrade_tz)
    sunset_local = sunset_utc.astimezone(belgrade_tz)

    now_local = datetime.now(belgrade_tz)

    print("== Podaci o suncu za Beograd ===")
    print(f"Trenutno vreme:   {now_local.strftime('%H:%M:%S (%d.%m.%Y.)')}")
    print(f"Izlazak sunca:    {sunrise_local.strftime('%H:%M:%S')}")
    print(f"Zalazak sunca:   {sunset_local.strftime('%H:%M:%S')}")

except requests.exceptions.RequestException as e:
    print(f"greska pri preuzimanju podataka sa servera: {e}")
# ---------------------------------------------[IMPORT MODULE]---------------------------------------------------
# Module für den Zugriff auf Dateien aus dem Internet
import sys
import time

import requests
# Modul zum Arbeiten mit Datum
import datetime


# ---------------------------------------------[FUNKTIONEN]-----------------------------------------------------
def now_kw():
    """
    Zuerst wird die aktuelle KW ermittelt.
    Mithilfe der Funktion "insert_week(kw)" wir eine Null vor die Zahl hinzufügt.
    ALs return erhalten wir also immer die aktuelle KW in zwei Werten.
    """
    # Heutiges Datum definieren
    datum = datetime.date.today().isocalendar()
    return insert_week(datum.week)


def next_kw():
    # Heutiges Datum definieren
    datum = datetime.date.today().isocalendar()
    # Nächste KW zurückgeben
    return insert_week(datum.week + 1)


def insert_week(kw):
    """
    Wenn die Zahl aus nur einem Wert besteht, wir eine null vor der Zahl eingefügt damit die KW Eingabe zwei Werte hat.
    """
    # Kontrolle und Korrektur, falls KW unter 10, weil wir für den Link zwei Werte benötigen
    if kw < 10:
        # KW in String umwandeln
        kw_str = str(kw)
        # Die 0 hinzufügen, falls KW woche unter 10 ist
        kw_str = "0" + kw_str
        # KW Ausgeben als String mit 0 davor
        return kw_str
    else:
        # KW in String umwandeln
        kw_str = str(kw)
        # KW Ausgeben als String, in diesem fall ohne null, weil KW > 10, es sind bereits zwei Werte.
        return kw_str


def download(week):
    url = STANDARD_URL.replace("KW01", "KW" + week)
    # Der oben gezeigte Code wird das Favicon (Bild) von STANDARD_URL herunterladen und Speichern
    webseite = requests.get(url)
    if webseite.status_code == 200:
        print("KW:", week + "\n" + "Download beginnt...")
        # Öffne Datei Stun. und speicher den Konten Speichern webseite
        open(f"FIAE_B_Stundenplan_KW_{week}_.pdf", "wb").write(webseite.content)
        print("Download abgeschlossen!")
    elif webseite.status_code == 404:
        print("KW:", week)
        print("Kein stundenplan verfügbar!")
    else:
        print("Unbekannter Fehler.")


# ---------------------------------------------[HAUPTPROGRAMM]---------------------------------------------------
# STANDARD_URL Definieren und in Var. Speichern
STANDARD_URL = "https://service.viona24.com/stpusnl/daten/US_IT_2022_Sommer_FIAE_B_2023_abKW01.pdf"

print("_____ WILLKOMMEN zum STUNDENPLAN DOWNLOADER _____")
print("Heutiges Datum:", datetime.date.today())
print("_"*50)

print("Aktuelle KW:", now_kw())
download(now_kw())
print("_"*50)

print("Nächste KW:" + next_kw())
download(next_kw())
print("_"*50)

print("Fenster wird in 10 Sec. automatisch geschlossen.")
for i in range(-10, 1):
    time.sleep(1)
sys.exit("Programm Ende.")

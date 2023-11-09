# Stundenplan-Downloader

Dieses Python-Skript ermöglicht es Ihnen, den Stundenplan für die aktuelle und die nächste Kalenderwoche von einer bestimmten URL herunterzuladen.

## Abhängigkeiten

Das Skript verwendet die folgenden Python-Module:

- `sys`, `time`: Zum Interagieren mit dem Betriebssystem und zur Handhabung von Zeitverzögerungen.
- `requests`: Zum Abrufen von Dateien aus dem Internet.
- `datetime`: Zum Arbeiten mit Datum und Zeit.

Stellen Sie sicher, dass diese Module installiert und importiert sind, bevor Sie das Skript ausführen.

## Verwendung

Das Skript führt die folgenden Schritte aus:

1. Es definiert die Standard-URL, von der der Stundenplan heruntergeladen wird.
2. Es begrüßt den Benutzer und zeigt das aktuelle Datum an.
3. Es ermittelt die aktuelle Kalenderwoche mit der Funktion `now_kw()` und lädt den entsprechenden Stundenplan herunter.
4. Es ermittelt die nächste Kalenderwoche mit der Funktion `next_kw()` und lädt den entsprechenden Stundenplan herunter.
5. Es informiert den Benutzer, dass das Fenster in 10 Sekunden automatisch geschlossen wird, und beendet dann das Skript.

Das Skript fängt auch `KeyboardInterrupt`-Ausnahmen ab und beendet das Skript ordnungsgemäß, wenn der Benutzer es während der Ausführung abbricht.

## Hinweis

Bitte stellen Sie sicher, dass Sie über eine stabile Internetverbindung verfügen, bevor Sie dieses Skript verwenden, da es Dateien aus dem Internet herunterlädt. Stellen Sie außerdem sicher, dass Sie die Berechtigung haben, die Dateien von der angegebenen URL herunterzuladen.
[assistant'](#message)d
Schön, dass Ihnen diese Antwort gefallen hat!

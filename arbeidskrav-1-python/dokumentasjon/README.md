# Gabriel Waade-Eriksen

## Oppgave 2 - Begrunnelse av valgt datastruktur:

Jeg valgte å legge til dataen i en array med flere dictionaries. Dette er fordi denne datastrukturen er en enkel og oversiktlig måte å lagre flere studieøkter på. Listen inneholder alle studieøktene, mens hver dictionary representerer en studieøkt. Dictionary gjør det enkelt å lagre forskjellig informasjon om hver økt, som tema, varighet og status. Det er også enkelt å hente ut, endre og filtrere informasjonen, som for eksempel å finne alle ferdige økter eller legge til en økt. Dette er også en veldig standarisert datastruktur, og er brukt mye i den profersjonelle verden i form av non-sql databaser og json-filer.

## Oppgave 3 - Funksjoner og dokumentasjon:

### Testtilfeller:

| Test | Input                        | Forventet resultat                        | Gyldig/ugyldig |
| ---- | ---------------------------- | ----------------------------------------- | -------------- |
| 1    | `14.09.2026`                 | Datoen godtas                             | Gyldig         |
| 2    | `31.02.2026`                 | Feilmelding og ber brukeren prøve på nytt | Ugyldig        |
| 3    | `13:30`, `90`                | Sluttid blir `15:00`                      | Gyldig         |
| 4    | `13:30`, `-20`               | Feilmelding og ber brukeren prøve på nytt | Ugyldig        |
| 5    | `13:30`, `abc`               | Feilmelding og ber brukeren prøve på nytt | Ugyldig        |
| 6    | `14.09.2026` og `20.09.2026` | Returnerer `6` dager                      | Gyldig         |

### Kilder:

**Tittel:** datetime — Basic date and time types
**Nettadresse:** https://docs.python.org/3/library/datetime.html

## Oppgave 4.4 - Finn og rett feil

### Original kode:

```
def sum_resolved_minutes(requests: list[dict[str, str | int]]) -> int:
    total = 0
    for request in requests:
        if request["is_resolved"] = "yes":
            total = request["minutes"]
    return total_minutes
```

### Feil 1 - `=` i stedet for `==`

Originalt sto det:

```
if request["is_resolved"] = "yes":
```

Jeg endret `=` til `==`:

```
if request["is_resolved"] == "yes":
```

`=` brukes til å tilordne en verdi til en variabel, mens `==` brukes til å sammenligne to verdier. Siden vi skal sjekke om is_resolved er lik "yes", må vi bruke `==`.

### Feil 2 - `total_minutes` eksisterer ikke

Originalt sto det:

```
return total_minutes
```

Problemet er at variabelen `total_minutes` ikke var opprettet. Det var bare opprettet en variabel som het `total`.

Jeg endret derfor variabelnavnet fra `total` til `total_minutes`, siden funksjonen skal finne det totale antallet minutter.

### Første test - `print(total)`

For å finne ut hva verdien i `total` faktisk var, la jeg til:

```
print(total)
```

Da kunne jeg se at verdien var antall minutter for hver enkelt henvendelse.

Koden etter denne endringen var:

```
def sum_resolved_minutes(requests: list[dict[str, str | int]]) -> int:
    total_minutes = 0
    for request in requests:
        if request["is_resolved"] == "yes":
            total = request["minutes"]
            print(total)
    return total_minutes
```

### Endring 2 - bedre variabelnavn

Jeg endret variabelnavnene `requests` og `request` til `inquiries` og `inquiry`.

Jeg endret også `total` til `minutes`, fordi variabelen inneholder antall minutter for én enkelt henvendelse.

Dette gjør koden lettere å forstå:

```
def sum_resolved_minutes(inquiries: list[dict[str, str | int]]) -> int:
    total_minutes = 0
    for inquiry in inquiries:
        if inquiry["is_resolved"] == "yes":
            minutes = inquiry["minutes"]
            print(minutes)
    return total_minutes
```

### Endring 3 – legge sammen minuttene

Jeg oppdaget at koden bare hentet ut minuttene, men ikke la dem sammen.

Jeg endret derfor:

```
print(minutes)
```

til:

```
total_minutes += minutes
```

Dette gjør at minuttene fra hver løste henvendelse blir lagt til `total_minutes`.

Koden ble da:

```
def sum_resolved_minutes(inquiries: list[dict[str, str | int]]) -> int:
    total_minutes = 0
    for inquiry in inquiries:
        if inquiry["is_resolved"] == "yes":
            minutes = inquiry["minutes"]
            total_minutes += minutes
    return total_minutes
```

Dette er den riktige løsningen dersom `minutes` allerede er et heltall.

### Endring 4 - teste beregningen

For å kontrollere at beregningen faktisk ble riktig, lagde jeg midlertidig en variabel som lagret den gamle verdien av `total_minutes`.

Deretter sjekket jeg om:

gammel verdi + minutter = ny verdi

Koden jeg brukte for å teste dette var:

```
def sum_resolved_minutes(inquiries: list[dict[str, str | int]]) -> int:
    total_minutes = 0
    for inquiry in inquiries:
        if inquiry["is_resolved"] == "yes":
            old_total_minutes = total_minutes

            minutes = inquiry["minutes"]
            total_minutes += minutes

            if old_total_minutes + minutes == total_minutes:
                print(f"True: {old_total_minutes} + {minutes} = {total_minutes}")
            else:
                print(f"False: {old_total_minutes} + {minutes} = {total_minutes}")

    return total_minutes
```

Dette var bare en test for å kontrollere at summeringen fungerte. Testkoden trenger ikke være med i den endelige funksjonen.

### Endring 5 - `try/except` og konvertering til `int`

Funksjonen bruker typen:

```
str | int
```

Det betyr at `minutes` kan være enten en streng eller et heltall.

For at vi skal kunne summere verdien på en trygg måte, bruker jeg:

```
minutes = int(inquiry["minutes"])
```

Da blir for eksempel `"60"` gjort om til `60`.

Jeg la også til en målrettet try/except rundt konverteringen:

```
try:
    minutes = int(inquiry["minutes"])
    total_minutes += minutes
except (ValueError, TypeError):
    continue
```

`ValueError` kan oppstå dersom verdien ikke kan konverteres til et heltall, for eksempel `"abc"`.

Jeg bruker ikke en tom `except`, fordi det ville skjult alle typer feil. Her håndterer jeg bare de feilene som kan oppstå ved konverteringen.

### Endelig løsning

```
def sum_resolved_minutes(inquiries: list[dict[str, str | int]]) -> int:
    total_minutes = 0
    for inquiry in inquiries:
        if inquiry["is_resolved"] == "yes":
            try:
                minutes = int(inquiry["minutes"])
                total_minutes += minutes
            except (ValueError, TypeError):
                continue
    return total_minutes
```

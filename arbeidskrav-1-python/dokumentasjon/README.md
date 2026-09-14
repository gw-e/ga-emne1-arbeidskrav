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

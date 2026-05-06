from dataclasses import dataclass

@dataclass(frozen=True)
class Aeroporto:
    ID: int
    IATA_CODE: str
    AIRPORT: str

    def __str__(self):
        return f"{self.AIRPORT} ({self.IATA_CODE})"
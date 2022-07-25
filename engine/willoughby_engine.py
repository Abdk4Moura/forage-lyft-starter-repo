from dataclasses import dataclass

from engine import Engine


@dataclass
class WilloughbyEngine(Engine):
    current_mileage: float
    last_service_mileage: float

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000

from dataclasses import dataclass

from engine_def import Engine


@dataclass
class CapuletEngine(Engine):
    current_mileage: float
    last_service_mileage: float

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000

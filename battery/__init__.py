from dataclasses import dataclass
from datetime import datetime

from abstract_components import Serviceable


class Battery(Serviceable):
    pass


@dataclass
class SpindlerBattery(Battery):
    last_service_date: object

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date():
            return True
        return False


@dataclass
class NubbinBattery(Battery):
    warning_light_is_on: bool

    def needs_service(self) -> bool:
        return self.warning_light_is_on

from abstract_components import Serviceable
from battery import SpindlerBattery, NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


# @dataclass
# class Car(Serviceable):
#     engine: Engine
#     battery: Battery
#
#     def __post_init__(self, *components):
#         self.components = components
#
#     def needs_service(self) -> bool:
#         return any([True for _component in self.components if _component.needs_service()])

class Car(Serviceable):
    def __init__(self, *components):
        self.engine, self.battery = components
        self.components = components

    def needs_service(self) -> bool:
        return any([True for _component in self.components if _component.needs_service()])


class CarFactory:
    @staticmethod
    def create_calliope(*params):
        (last_service_date,
         current_mileage,
         last_service_mileage
         ) = params
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(warning_light_is_on, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(warning_light_is_on)
        car = Car(engine, battery)
        return car

from abc import ABC, abstractmethod

class CarComponent(ABC):
    pass


class Serviceable(CarComponent):
    """Represents object that must be serviced at some point in time"""

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Engine(Serviceable):
    pass


class Tire(Serviceable):
    pass

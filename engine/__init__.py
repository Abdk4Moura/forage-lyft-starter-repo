from abc import ABC, abstractmethod
from dataclasses import dataclass


class CarComponent(ABC):
    pass


class Serviceable(CarComponent):
    """Represents object that must be serviced at some point in time"""

    @abstractmethod
    def needs_service(self) -> bool:
        pass


@dataclass
class Engine(Serviceable):
    pass

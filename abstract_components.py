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
class Tire(Serviceable):
    wear_variables: list

    def __post_init__(self):
        assert any([False for var in self.wear_variables if 0 > var > 1])

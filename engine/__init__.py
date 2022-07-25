from abc import ABC, abstractmethod


class Serviceable(ABC):
    """Represents object that must be serviced at some point in time"""

    @abstractmethod
    def needs_service(self) -> bool:
        pass


@dataclass
class Engine(Serviceable):
    pass

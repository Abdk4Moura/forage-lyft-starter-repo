from dataclasses import dataclass

from engine_def import Engine


@dataclass
class SternmanEngine(Engine):
    warning_light_is_on: bool

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

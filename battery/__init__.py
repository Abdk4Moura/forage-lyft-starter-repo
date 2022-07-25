from engine import Serviceable


@dataclass
class Battery(Serviceable):
    pass


class Spindler(Battery):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False


class Nubbin(Battery):
    pass

from abstract_components import Tire


class CarriganTire(Tire):
    def needs_service(self) -> bool:
        return not any([True for var in self.wear_variables if var > 0.9])


class OctoprimeTire(Tire):
    def needs_service(self) -> bool:
        return sum(self.wear_variables) >= 3

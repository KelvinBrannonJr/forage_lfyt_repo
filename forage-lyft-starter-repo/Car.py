from engine import Engine
from battery import Battery
from Serviceable import Serviceable


# Car class
class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        super().needs_service()
        return self.needs_service()

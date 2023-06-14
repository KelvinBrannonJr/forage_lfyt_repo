from battery import NubbinBattery
from battery import SpindlerBattery
from Car import Car
from engine import CapuletEngine
from engine import SternmanEngine
from engine import WilloughbyEngine


# Factory for Car instances
class CarFactory:

    # create calliope
    @staticmethod
    def create_calliope(self,
                        current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    # create glissade
    @staticmethod
    def create_glissade(self,
                        current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    # create palindrome
    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    # create rorschach
    @staticmethod
    def create_rorschach(self,
                         current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    # create thovex
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

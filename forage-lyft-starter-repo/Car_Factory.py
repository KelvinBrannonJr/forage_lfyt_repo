from abc import ABC, abstractmethod
from datetime import date


# Factory for Car instances
class CarFactory(ABC):

    # create calliope
    @abstractmethod
    def create_calliope(self,
                        current_date: date, last_service_date: date, current_milage: int, last_service_mileage: int):
        pass

    # create glissade
    @abstractmethod
    def create_glissade(self,
                        current_date: date, last_service_date: date, current_milage: int, last_service_mileage: int):
        pass

    # create palindrome
    @abstractmethod
    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):

        pass

    # create rorschach
    @abstractmethod
    def create_rorschach(self,
                         current_date: date, last_service_date: date, current_milage: int, last_service_mileage: int):

        pass


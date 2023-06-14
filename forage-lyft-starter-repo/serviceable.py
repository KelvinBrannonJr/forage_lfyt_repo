from abc import ABC, abstractmethod


# Abstract Serviceable class and method
class Serviceable(ABC):

    @abstractmethod
    def needs_service(self):
        pass

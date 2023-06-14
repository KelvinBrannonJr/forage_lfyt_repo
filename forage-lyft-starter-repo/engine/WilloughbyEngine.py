import Engine


# Willoughby Engine class
class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000



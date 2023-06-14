import Engine


# Capulet Engine class
class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000


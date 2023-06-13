import Engine


# Capulet Engine class
class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_serviced(self) -> bool:
        super().needs_serviced(self)
        return self.needs_service()

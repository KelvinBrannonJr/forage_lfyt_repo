import Engine


# Sternman Engine class
class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on

    def needs_serviced(self) -> bool:
        super().needs_serviced(self)
        return self.needs_serviced()

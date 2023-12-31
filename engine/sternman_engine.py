from engine.engine import Engine


# Sternman Engine class
class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

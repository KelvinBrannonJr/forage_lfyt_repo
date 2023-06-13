from Car import Car


# Engine class
class Engine(Car):
    def needs_service(self):
        super().needs_service()
        return self.needs_service()

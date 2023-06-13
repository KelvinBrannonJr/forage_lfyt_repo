from Car import Car


# Battery Class
class Battery(Car):
    def needs_service(self):
        super().needs_service()
        return self.needs_service()

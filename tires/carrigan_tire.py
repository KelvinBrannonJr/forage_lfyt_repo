from tires import Tire
import array as arr


# Carrigan Tire Class
class CarriganTire(Tire):
    def __init__(self, front_driver, front_passenger, rear_driver, rear_passenger):
        self.front_driver = front_driver
        self.front_passenger = front_passenger
        self.rear_driver = rear_driver
        self.rear_passenger = rear_passenger

        # Array to hold class attribute values
        self.tire_wear = arr.array("f", [front_driver, front_passenger, rear_driver, rear_passenger])

    # Needs Service
    def needs_service(self):
        # Holder for tire wear sum
        tire_wear_sum = 0.0

        # Iterate through the array and add values
        for index in self.tire_wear:
            tire_wear_sum += index

        # Format the sum
        formatted_tire_sum = "%.1f" % tire_wear_sum

        # Conditionals to check values
        if float(formatted_tire_sum) >= 0.9:
            return True

        else:
            return False


# Contained Test
test = CarriganTire(0.2, 0.3, 0.3, 0.0)

print(test.needs_service())
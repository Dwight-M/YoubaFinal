class Driver:
    """
    Constructs a class for a new Driver

    Args:
        first_name: Drivers first name
        last_name: Drivers last name
        car_make_and_model: Drivers car make and model
        trips_completed: Number of trips Drivers has completed

    Returns:
        driver: A Driver Class
    """

    def __init__(self,
                 first_name, last_name, car_make_and_model, trips_completed=0):
        """Initalize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.car_make_and_model = car_make_and_model
        self.trips_completed = trips_completed

        def get_first_name(self):
            return self.first_name

        def get_last_name(self):
            return self.last_name

        def get_car_make_and_model(self):
            return self.car_make_and_model

        def get_trips_completed(self):
            return self.trips_completed

        def set_car_make_and_model(self, car_model):
            self.car_make_and_model = car_model

        def increment_trips(self, car_model):
            self.trips_completed += 1

        def is_driver_new(self):
            if self.trips_completed == 0:
                return True
            else:
                return False

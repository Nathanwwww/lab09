class Location:
    def __init__(self, pickup, dropoff):
        self._pickup = pickup
        self._dropoff = dropoff

    @property
    def pickup(self):
        return self._pickup

    @property
    def dropoff(self):
        return self._dropoff

    def __str__(self):
        return "Location Details: pickup - {}, dropoff - {}".format(self.pickup, self.dropoff)

    def check_location(self):
        if not self._pickup:
            return False
        elif not self._dropoff:
            return False
        return True

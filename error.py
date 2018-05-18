class BookingError(Exception):
    def __init__(self,location,period,msg=None):
        if msg == None:
            msg = "An error happened with bookings"
        self._location = location
        self._period = period
        self.msg = msg
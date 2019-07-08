import utils


class TravelPoint:

    def __init__(self, destination_name, departure_time=None, arrival_time=None):
        """ Initialising function to check if the data being passed is valid, and if it is, store it in a tuple.

        :param destination_name: Name of a travel destination.
        :param departure_time: The time when a journey starts to get to this destination. (Defaults to None)
        :param arrival_time: The time when a journey to get to this destination would end. (Defaults to None)
        :raises ValueError: If both the departure time and the arrival time are set to None.
        :raises ValueError: If the departure or arrival time dont follow the format of YYYY/MM/DD HH:MM.
        """
        if (departure_time is None) and (arrival_time is None):
            raise ValueError('At least one of arrival or departure time must be set')

        if departure_time is not None:
            try:
                utils.time_to_datetime(departure_time)
            except ValueError:
                raise ValueError("The departure_time must have the format YYYY/MM/DD HH:MM")

        if arrival_time is not None:
            try:
                utils.time_to_datetime(arrival_time)
            except ValueError:
                raise ValueError("The arrival_time must have the format YYYY/MM/DD HH:MM")

        travel_info = (destination_name, departure_time, arrival_time)

import utils


class Journey:

    def __init__(self, start_place, end_place):
        """ Checks and stores the start and end details of a journey.

        :param start_place: A TravelPoint object from location.py for the starting location.
        :param end_place: A TravelPoint object from location.py for the end destination.
        :raises ValueError: If the end time is less than or equal to the start time.
        """
        if start_place[1] < end_place[1]:
            self.start_place = start_place[0]
            self.start_time = start_place[1]
            self.end_place = end_place[0]
            self.end_time = end_place[1]
        else:
            raise ValueError("Journey must end after the start time")

    def time(self):
        """ Calculates the time taken to undertake a given journey.

        :return: A tuple that contains the length of the journey in hours and minutes.
        """
        start_time = utils.time_to_datetime(self.start_time)
        end_time = utils.time_to_datetime(self.end_time)
        difference = end_time - start_time
        difference = str(difference).split(":")
        difference = int(difference[0]), int(difference[1])

        return difference


import utils


class JourneyOptions:
    def __init__(self, default, alternatives=tuple()):
        """ Stores a number of options for a journey.

        :param default: a default TravelPoint object from journey.py.
        :param alternatives: a tuple storing potentially alternative journey objects(Defaults to an empty tuple).
        """
        self.default = default
        self.alternatives = alternatives

    def earliest_arrival(self):
        """ Finds the earliest possible arrival time among the alternative journey options stored.

        :return: returns one of the alternative journey objects if faster, returns default journey if not.
        """

        shorter_time = 5
        for i in range(len(self.alternatives)):
            if utils.time_to_datetime(self.alternatives[i].time()) < utils.time_to_datetime(self.default.time()):
                shorter_time = i
        if shorter_time != 5:
            return self.alternatives[shorter_time]
        else:
            return self.default

    def latest_arrival(self):
        """ Finds the latest possible arrival time among the alternative journey options stored.

        :return: returns one of the alternative journey objects if slower, returns default journey if not.
        """

        shorter_time = 5
        for i in range(len(self.alternatives)):
            if utils.time_to_datetime(self.alternatives[i].time()) > utils.time_to_datetime(self.default.time()):
                shorter_time = i
        if shorter_time != 5:
            return self.alternatives[shorter_time]
        else:
            return self.default

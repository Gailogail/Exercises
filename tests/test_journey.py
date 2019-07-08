"""Unit tests for the journey module.

This module provides a Journey class that, well, stores all the information for
a journey. The information includes things like:

- Departure and destination point.
- Departure and arrival times.
- Location, arrival and departure times for intermediate points; e.g. train
  changes.
"""

import collections
import unittest   # Standard unittest framework.

import journey    # The module implementing the Journey class.


StartPlace = collections.namedtuple(
    'Place', ('name', 'departure_time'))
EndPlace = collections.namedtuple(
    'Place', ('name', 'arrival_time'))


class TestJourney(unittest.TestCase):
    """Tests for the Journey class.

    I journey is created by passing in a start and end object. The start
    must provide a a name and departure_time attribute The end must provide
    a name and arrival_time attribute. The time attributes are strings of the
    form YYYY/MM/DD HH:MM.
    """
    # A departure and destination for the tests.
    southampton_station = StartPlace(
        name='Eastleigh Southampton Airport, Train Station',
        departure_time='2019/05/15 10:20')
    waterloo_station = EndPlace(
        name='WaterLoo (London), London Waterloo Rail Station',
        arrival_time='2019/05/15 12:50')

    def test_invalid_end_times_is_detected(self):
        """A ValueError is raised if a journey does not end after it starts."""

        narnia = EndPlace(
            name='Narnia',
            arrival_time='2019/05/15 10:20')
        with self.assertRaises(ValueError) as cm:
            journey.Journey(self.southampton_station, narnia)
        self.assertEqual(
                'Journey must end after the start time', str(cm.exception))

    def test_valid_end_time_is_accepted(self):
        """A valid end time allows a Journey to be created."""

        trip = journey.Journey(self.southampton_station, self.waterloo_station)

    def test_places_and_times_are_available(self):
        """The journey details avalable as properties include:

        - start_place
        - end_place
        - start_time
        - end_time

        All are strings.
        """
        trip = journey.Journey(self.southampton_station, self.waterloo_station)
        self.assertEqual(
            'Eastleigh Southampton Airport, Train Station', trip.start_place)
        self.assertEqual(
            'WaterLoo (London), London Waterloo Rail Station', trip.end_place)
        self.assertEqual('2019/05/15 10:20', trip.start_time)
        self.assertEqual('2019/05/15 12:50', trip.end_time)

    def test_total_journey_time(self):
        """The total journey time can be calculated.

        The calculated time is atuple of hours, minutes.
        """
        trip = journey.Journey(self.southampton_station, self.waterloo_station)
        self.assertEqual((2, 30), trip.time())


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()

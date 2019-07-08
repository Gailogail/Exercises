"""Unit tests for the TravelPoint class.

A TravelPoint stores information about a given location that is part of a
journey. The attributes include name, departure_time and arrival_time.
"""

import unittest   # Standard unittest framework.

import location   # The module implementing the TravelPoint class.


class TestTravelPoint(unittest.TestCase):
    """Tests for the TravelPoint class."""

    def test_invalid_arrival_time_is_rejected(self):
        """A ValueError is raised if the arrival time is not valid."""

        with self.assertRaises(ValueError) as cm:
            location.TravelPoint(
                'Narnia', '2019/13/15 10:20', '2019/10/15 10:00')
        self.assertEqual(
                'The departure_time must have the format YYYY/MM/DD HH:MM',
                str(cm.exception))

    def test_invalid_departure_time_is_rejected(self):
        """A ValueError is raised if the departure time is not valid."""

        with self.assertRaises(ValueError) as cm:
            location.TravelPoint(
                'Narnia', '2019/10/15 10:20', '2019/10/15 10:')
        self.assertEqual(
                'The arrival_time must have the format YYYY/MM/DD HH:MM',
                str(cm.exception))

    def test_departure_time_may_be_none(self):
        """The departure time may be None."""
        location.TravelPoint(
            'Narnia', arrival_time='2019/10/15 10:00', departure_time=None)

    def test_arrival_time_may_be_none(self):
        """The departure time may be None."""
        location.TravelPoint(
            'Narnia', departure_time='2019/10/15 10:20', arrival_time=None)

    def test_only_time_may_be_none(self):
        """Both times cannot be None."""
        with self.assertRaises(ValueError) as cm:
            location.TravelPoint(
                'Narnia', arrival_time=None, departure_time=None)
        self.assertEqual(
                'At least one of arrival or departure time must be set',
                str(cm.exception))


if __name__ == '__main__':
    unittest.main()


"""Unit tests for the JourneyOptions class.

A JourneyOptions class stores one or more ways to get from a given A to B.
"""

import unittest                # Standard unittest framework.
import unittest.mock as mock   # Standard mocking framework.

import planning   # The module implementing JourneyOptions class.


class TestJourneyOptions(unittest.TestCase):
    """Tests for the JourneyOptions class."""

    def test_can_use_single_journey(self):
        """A JourneyOptions with a single journey is allowed."""
        journey = unittest.mock.MagicMock()
        options = planning.JourneyOptions(journey)

    def test_must_include_a_default_journey(self):
        """A default journey is required for construction.

        The __init__ should not provide a default value.
        """
        with self.assertRaises(TypeError) as cm:
            planning.JourneyOptions()
        self.assertTrue('__init__() missing 1 required positional argument:'
                   in str(cm.exception))

    def test_can_include_alternatives(self):
        """A JourneyOptions alternatives journey is supported."""
        journey = unittest.mock.MagicMock()
        alt_journeys = (
            unittest.mock.MagicMock(),
            unittest.mock.MagicMock())
        options = planning.JourneyOptions(journey, alternatives=alt_journeys)

    def test_default_attr(self):
        first, second, third = _make_three_mocks()
        alt_journeys = (first, third)
        options = planning.JourneyOptions(second, alternatives=alt_journeys)
        self.assertTrue(options.default is second)

    def test_the_earliest_journey_is_available(self):
        first, second, third = _make_three_mocks()
        alt_journeys = (first, third)
        options = planning.JourneyOptions(second, alternatives=alt_journeys)
        self.assertTrue(options.earliest_arrival() is first)

    def test_the_latest_journey_is_available(self):
        first, second, third = _make_three_mocks()
        alt_journeys = (first, third)
        options = planning.JourneyOptions(second, alternatives=alt_journeys)
        self.assertTrue(options.latest_arrival() is third)

    def test_the_default_may_be_the_earliest(self):
        first, second, third = _make_three_mocks()
        alt_journeys = (second, third)
        options = planning.JourneyOptions(first, alternatives=alt_journeys)
        self.assertTrue(options.earliest_arrival() is first)

    def test_the_default_may_be_the_latest(self):
        first, second, third = _make_three_mocks()
        alt_journeys = (first, second)
        options = planning.JourneyOptions(third, alternatives=alt_journeys)
        self.assertTrue(options.latest_arrival() is third)

    def test_no_alternatives_default_is_latest_and_earliest(self):
        _, default, _ = _make_three_mocks()
        options = planning.JourneyOptions(default)
        self.assertTrue(options.earliest_arrival() is default)
        self.assertTrue(options.latest_arrival() is default)


def _make_three_mocks():
    first = unittest.mock.MagicMock()
    second = unittest.mock.MagicMock()
    third = unittest.mock.MagicMock()
    first.configure_mock(**{'time.return_value': '2019/05/01 12:00'})
    second.configure_mock(**{'time.return_value': '2019/05/01 13:00'})
    third.configure_mock(**{'time.return_value': '2019/05/01 14:00'})

    return first, second, third


if __name__ == '__main__':
    unittest.main()


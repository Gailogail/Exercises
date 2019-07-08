"""Unit tests for the utils module."""

import datetime
import os
import unittest   # Standard unittest framework.

import utils   # The module implementing JourneyOptions class.


class TestTimeToDatetime(unittest.TestCase):
    """Tests for the time_to_datetime function."""

    def test_invalid_time_is_rejected(self):
        with self.assertRaises(ValueError) as cm:
            utils.time_to_datetime('2019/06/09 12:60')
        self.assertEqual(
            'The time must have the format YYYY/MM/DD HH:MM',
            str(cm.exception))

    def test_valid_time_yields_a_dattime_object(self):
        d = utils.time_to_datetime('2019/06/09 12:59')
        self.assertTrue(isinstance(d, datetime.datetime))


class TestLoadPrevJourneySpec(unittest.TestCase):
    """Tests for the load_prev_plan_spec function."""

    PATH = os.path.expanduser('~/test_prev_plan_spec.txt')

    def test_missing_file_is_handled(self):
        if os.path.exists(self.PATH):
            os.unlink(self.PATH)
        plan = utils.load_prev_plan_spec(self.PATH)
        self.assertEqual(3, len(plan))
        self.assertEqual(plan, (None, None, None))

    def test_spec_loads_ok(self):
        from_ = 'Bournemouth'
        to = 'Southampton'
        arrive_at = '2019/04/20 13:30'
        with open(self.PATH, 'wt') as f:
            f.write('{}\n{}\n{}\n'.format(from_, to, arrive_at))
        plan = utils.load_prev_plan_spec(self.PATH)
        self.assertEqual(3, len(plan))
        self.assertEqual(from_, plan[0])
        self.assertEqual(to, plan[1])
        self.assertEqual(arrive_at, plan[2])

    def test_short_spec_is_ignored(self):
        from_ = 'Bournemouth'
        to = 'Southampton'
        with open(self.PATH, 'wt') as f:
            f.write('{}\n{}\n'.format(from_, to))
        plan = utils.load_prev_plan_spec(self.PATH)
        self.assertEqual(3, len(plan))
        self.assertEqual(plan, (None, None, None))

        with open(self.PATH, 'wt') as f:
            f.write('{}\n'.format(from_))
        plan = utils.load_prev_plan_spec(self.PATH)
        self.assertEqual(3, len(plan))
        self.assertEqual(plan, (None, None, None))

    def test_empty_line_is_handled(self):
        from_ = 'Bournemouth'
        to = ''
        arrive_at = '2019/04/20 13:30'
        with open(self.PATH, 'wt') as f:
            f.write('{}\n{}\n{}\n'.format(from_, to, arrive_at))
        plan = utils.load_prev_plan_spec(self.PATH)
        self.assertEqual(3, len(plan))
        self.assertEqual(plan, (None, None, None))

    def test_bad_data_line_is_handled(self):
        from_ = 'Bournemouth'
        to = 'Southampton'
        arrive_at = '2019/04/20 13:60'
        with open(self.PATH, 'wt') as f:
            f.write('{}\n{}\n{}\n'.format(from_, to, arrive_at))
        plan = utils.load_prev_plan_spec(self.PATH)
        self.assertEqual(3, len(plan))
        self.assertEqual(plan, (None, None, None))


if __name__ == '__main__':
    unittest.main()

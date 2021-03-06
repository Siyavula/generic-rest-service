import unittest
import datetime
from dateutil.tz import tzutc
from rest.utils import force_utc, parse_iso8601

class TestUtils(unittest.TestCase):
    def test_force_utc(self):
        dt = datetime.datetime(2012, 1, 2, 12, 34, 56)
        self.assertIsNone(dt.tzinfo)
        dt2 = force_utc(dt)
        self.assertIsNotNone(dt2.tzinfo)
        self.assertEquals(dt2.tzinfo, tzutc())

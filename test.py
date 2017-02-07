"""


"""
from drparse import parse

import unittest
import logging

log = logging.getLogger('drparse')
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

class TestDateRangeParsing(unittest.TestCase):
    """
    Date Range Parsing
    """

    def assertExpectedResult(self, text, expected_date_strings, expected_dates):

        result = parse(text)

        if expected_dates is None and result is None:
            return

        self.assertListEqual(result.dates, expected_date_strings)

        log.debug(result.dates)

        if len(expected_dates) == 1:
            self.assertIsNone(result.end)
            self.assertEqual(result.start.strftime('%Y-%m-%d %H:%M'), expected_dates[0])

        else:
            self.assertEqual(result.start.strftime('%Y-%m-%d'), expected_dates[0])
            self.assertEqual(result.end.strftime('%Y-%m-%d'), expected_dates[1])

    def testDateRanges(self):

        self.assertExpectedResult("August 29, 2006 - September 2, 2006", ['August 29, 2006', 'September 2, 2006'], ['2006-08-29', '2006-09-02'])
        self.assertExpectedResult("Thu, 6 -  Sun, 16 Oct 2016", ['Thu, 6 Oct 2016', 'Sun, 16 Oct 2016'], ['2016-10-06', '2016-10-16'])
        self.assertExpectedResult("Sat, 4 Jun 2016", ['Sat, 4 Jun 2016'], ['2016-06-04 00:00'])
        self.assertExpectedResult("2016-08-10 10pm", ['2016-08-10'], ['2016-08-10 22:00'])
        self.assertExpectedResult("Sat May 28, 2016 to Sun May 29, 2016, 10PM till late", ['Sat May 28, 2016', 'Sun May 29, 2016'], ['2016-05-28', '2016-05-29'])

        self.assertExpectedResult("Thursday, July 28 at 8 PM - 11 PM", ['Thursday, July 28 at'], ['2017-07-28 00:00'])
        self.assertExpectedResult("Saturday, June 11 at 12 PM - 10 PM in UTC+02", ['Saturday, June 11 at in UTC+0', '10 PM in UTC+0'], ['2017-06-11 00:00'])
        self.assertExpectedResult("Saturday, 30 April 2016 & 5 May 2016", ['Saturday, 30 April 2016', '5 May 2016'], ['2016-04-30', '2016-05-05'])
        self.assertExpectedResult("Sat, 9 Jul 2016 8pm", ['Sat, 9 Jul 2016'], ['2016-07-09 20:00'])


if __name__ == '__main__':
    unittest.main()

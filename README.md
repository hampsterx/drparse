# Date Range Parser

Crudely extends [dateparser](https://github.com/scrapinghub/dateparser) to extract out one or two dates from a string.
Times are deliberately ignored, it *only* extracts the dates.

### Why Only dates?

Because that is all I needed

### Examples

    from daterangeparser import parse_dates

Single Date with time range

    dates = parse_dates("Thursday, July 28 at 8 PM - 11 PM")

    dates.start => datetime.datetime(2016, 7, 28, 0, 0)

Date range without time

    dates = parse_dates("Thu, 6 -  Sun, 16 Oct 2016")

    dates.start => datetime.datetime(2016, 10, 6, 0, 0)
    dates.end => datetime.datetime(2016, 10, 16, 0, 0)

Date range with time

    dates = parse_dates("Sat May 28, 2016 to Sun May 29, 2016, 10PM till late")

    dates.start => datetime.datetime(2016, 5, 28, 0, 0)
    dates.end => datetime.datetime(2016, 5, 29, 0, 0)

### Further info

    How to work with time/date ranges, changing default values, etc
    https://github.com/bear/parsedatetime/issues/162

    Search text for dates
    https://github.com/scrapinghub/dateparser/issues/82





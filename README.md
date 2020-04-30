# FlightStatsScraper
A tool for scraping flight data from the FLIGHSTATS official website, based on the airport selected for arrival and departure data which can be retrieved up to 3 days from the date of collection.

How to use:
- Clone this repository, and install scrapy on your Python.
- Change directory to "FS"
- Determine which airports to take data from
- Run "scrapy crawl flightStatus" for arrival data
- And run "scrapy crawl flightstatusdep" for departure data
- Automatically this tool will retrieve the data of yesterday's flight

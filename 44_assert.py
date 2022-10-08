import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert len(self.title) != 0, "Title is empty!"
        assert self.start <= self.end, "Start date is later than end date!"

    @classmethod
    def publish_offer(cls, trip_list:list):
        list_of_errors = []
        for a_trip in trip_list:
            try:
                a_trip.check_data()
            except ValueError as ve:
                list_of_errors.append("ValueError in {0}: {1}".format(a_trip.symbol, ve))
            except Exception as ve:
                list_of_errors.append("GeneralError in {0}: {1}".format(a_trip.symbol, ve))

        assert len(list_of_errors) == 0, list_of_errors
        print("List of offers will be published")


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print("Initiating pre-publish check...")
    Trip.publish_offer(trips)
    print("Pre-publishing done.")
except Exception as e:
    print("One or more errors have occurred while processing your data: {0}".format(e))

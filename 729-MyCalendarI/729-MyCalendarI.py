# Last updated: 8/1/2025, 6:26:21 PM
class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        for stime,etime in self.booking:
            if start < etime and end > stime:
                return False

        self.booking.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour % 12
        self.minutes = minute % 60
        self.second = second % 60

    def displayClock(self):
        print(f'{self.hour}:{self.minutes}:{self.second}')

    def __add__(self, other):
        seconds = self.second + other.second
        minutes = self.minutes + other.minutes
        hours = self.hour + other.hour

        if seconds >= 60:
            seconds -= 60
            minutes += 1

        if minutes >= 60:
            minutes -= 60
            hours += 1

        if hours >= 12:
            hours -= 12

        return Clock(hours, minutes, seconds)

    def addSecond(self, seconds):
        self.second += seconds

        while self.second >= 60:
            self.second -= 60
            self.minutes += 1
            if self.minutes >= 60:
                self.minutes -= 60
                self.hour += 1

        self.hour = self.hour % 12


a = Clock(7, 13, 72)
b = Clock(9, 45, 19)
a.displayClock()
b.displayClock()

(a + b).displayClock()

a.addSecond(454650)
a.displayClock()

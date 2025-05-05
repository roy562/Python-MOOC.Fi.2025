# Write your solution here:
class Clock():
    def __init__(self, hours:int, minutes:int, seconds:int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    
    def set(self, hours:int, minutes:int, seconds:int=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        if self.seconds < 59:
            self.seconds+=1
        elif self.minutes<59:
            self.seconds = 0
            self.minutes+=1
        elif self.hours <23:
            self.seconds = 0
            self.minutes = 0
            self.hours+=1
        else:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0


def main():
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)

#main()
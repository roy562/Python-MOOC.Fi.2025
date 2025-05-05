# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name:str):
        if name == "":
            raise ValueError("Name of the weather station can't be empty")
        self.__name = name
        self.__obs = []

    def __str__(self):
        return f"{self.__name}, {len(self.__obs)} observations"

    def add_observation(self, observation:str):
        if observation == "":
            raise ValueError("Observation can't be empty string")
        self.__obs.append(observation)
    
    def latest_observation(self):
        if len(self.__obs) == 0:
            return ""
        else:
            return self.__obs[-1]
        
    def number_of_observations(self):
        return len(self.__obs)

def main():
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)

#main()
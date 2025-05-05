# Write your solution here
def get_station_data(filename: str):
    stations = {}
    with open(filename) as file:
        for line in file:
            fields = line.split(";")
            if fields[0] == 'Longitude':
                continue
            else:
                stations[fields[3]] = (float(fields[0]),float(fields[1]))
    return stations

def calc_dist(longitude1:float,latitude1:float,longitude2:float,latitude2:float):
    import math

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def distance(stations: dict, station1: str, station2: str):
    longitude1,latitude1 = stations[station1]
    longitude2,latitude2 = stations[station2]
    distance_km = calc_dist(longitude1,latitude1,longitude2,latitude2)
    
    return distance_km

def greatest_distance(stations: dict):
    greatest = 0
    station1 = ""
    station2 = ""
    for key1, values1 in stations.items():
        #station1 = key1
        for key2,values2 in stations.items():
            #station2 = key
            if key1 == key2:
                continue
            
            distance = calc_dist(values1[0], values1[1], values2[0], values2[1])
            if distance > greatest:
                greatest = distance
                station1 = key1
                station2 = key2

    return station1, station2, greatest

    

def main():
    stations = get_station_data('stations1.csv')
    print(stations)

    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)

    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)

#main()
# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new_dict = {}
    new_dict["name"] = name
    new_dict["director"] = director
    new_dict["year"] = year
    new_dict["runtime"] = runtime
    database.append(new_dict)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)
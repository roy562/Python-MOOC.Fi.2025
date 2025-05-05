# Write your solution here:
class Series():
    def __init__(self, title:str, seasons:int, genres:list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
    
    def rate(self, rating: int):
        if rating >=0 and rating <=5:
            self.ratings.append(rating)

    def average_rating(self):
        return sum(self.ratings)/len(self.ratings)

    def __str__(self):
        series_str = f"{self.title} ({self.seasons} seasons)\n"
        series_str+= "genres: "+ ", ".join(self.genres)+"\n"
        if len(self.ratings) == 0:
            series_str+="no ratings"
        else:
            average_rating = self.average_rating()
            series_str+=f"{len(self.ratings)} ratings, average {average_rating:.1f} points"
        return series_str

def minimum_grade(rating: float, series_list: list):
    results = []
    for series in series_list:
        if series.average_rating() >= rating:
            results.append(series)

    return results

def includes_genre(genre: str, series_list: list):
    results = []
    for series in series_list:
        if genre in series.genres:
            results.append(series)

    return results

def main():
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

#main()
# Write your solution here
import json

class Player:
    def __init__(self, record:dict):
        self.name = record['name']
        self.nationality = record['nationality']
        self.assists = record['assists']
        self.goals = record['goals']
        self.penalties = record['penalties']
        self.team = record['team']
        self.games = record['games']

    def __str__(self):
        return f"{self.name:21}{self.team:4}{self.goals:3} +{self.assists:3} ={self.goals+self.assists:4}"   

class PlayerStats:
    def __init__(self):
        self.__players = []
    
    def add_player(self, record:dict):
        player = Player(record)
        self.__players.append(player)
    
    def total_players(self):
        return len(self.__players)
    
    def search_player_by_name(self, player_name:str):
        player = [p for p in self.__players if p.name == player_name]
        return player[0]
    
    def get_all_teams(self):
        return list(set([player.team for player in self.__players]))
    
    def get_all_countries(self):
        return list(set([player.nationality for player in self.__players]))
    
    def __by_points(self, player:"Player"):
        return player.assists+player.goals

    def get_players_by_team(self, team_name:str):
        players_list_by_team = [player for player in self.__players if player.team == team_name]
        sorted_players_list = sorted(players_list_by_team, key=self.__by_points, reverse=True)
        return sorted_players_list

    def get_players_by_country(self, country_name:str):
        players_list_by_country = [player for player in self.__players if player.nationality == country_name]
        sorted_players_list = sorted(players_list_by_country, key=self.__by_points, reverse=True)
        return sorted_players_list

    def get_players_by_points(self):
        return sorted(self.__players, key=lambda p: (p.goals+p.assists, p.goals), reverse=True)
    
    def get_players_by_goals(self):
        return sorted(self.__players, key=lambda p: (p.goals, p.goals-p.games), reverse=True)


class HockeyApplication:
    def __init__(self):
        self.__playerstats = PlayerStats()
    
    def __initial_prompt(self):
        print('commands:')
        print('0 quit')
        print('1 search for player')
        print('2 teams')
        print('3 countries')
        print('4 players in team')
        print('5 players from country')
        print('6 most points')
        print('7 most goals')
            
    def __read_file(self):
        filename = input("file name: ")
        #filename = 'partial.json'
        with open(filename) as file:
            data = file.read()

        json_list = json.loads(data)

        for record in json_list:
            self.__playerstats.add_player(record)
        
        print(f"read the data of {self.__playerstats.total_players()} players")
        print()

    def __search_for_player(self, player_name:str):
        #print("In application search method")
        player = self.__playerstats.search_player_by_name(player_name)
        print(player)

    def __list_teams(self):
        all_teams = sorted(self.__playerstats.get_all_teams())
        for team in all_teams:
            print(team)
    
    def __list_countries(self):
        all_countries = sorted(self.__playerstats.get_all_countries())
        for country in all_countries:
            print(country)
    
    def __players_in_team(self, team_name:str):
        players_list = self.__playerstats.get_players_by_team(team_name)
        print()
        for player in players_list:
            print(player)

    def __players_from_country(self, country_name:str):
        players_list = self.__playerstats.get_players_by_country(country_name)
        print()
        for player in players_list:
            print(player)
    
    def __players_by_most_points(self, how_many:int):
        players_list = self.__playerstats.get_players_by_points()
        print()
        for i in range(how_many):
            print(players_list[i])

    def __players_by_most_goals(self, how_many:int):
        players_list = self.__playerstats.get_players_by_goals()
        print()
        for i in range(how_many):
            print(players_list[i])


    def execute(self):
        self.__read_file()
        self.__initial_prompt()

        while True:
            print()
            try:
                option = int(input("command: "))
            
                if option == 0:
                    break
                elif option == 1:
                    player_name = input("name: ")
                    print()
                    self.__search_for_player(player_name)
                elif option == 2:
                    self.__list_teams()
                elif option == 3:
                    self.__list_countries()
                elif option == 4:
                    team = input("team: ")
                    self.__players_in_team(team)
                elif option == 5:
                    country_name = input("country: ")
                    self.__players_from_country(country_name)
                elif option == 6:
                    how_many = int(input("how many: "))
                    self.__players_by_most_points(how_many)
                elif option == 7:
                    how_many = int(input("how many: "))
                    self.__players_by_most_goals(how_many)
                else:
                    raise ValueError("Incorrect input")
            except:
                #print("erroneous input")
                continue


app = HockeyApplication()
app.execute()




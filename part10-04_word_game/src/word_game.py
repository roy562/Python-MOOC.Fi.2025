# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            pass

class MostVowels(WordGame):
    vowels = 'aeiou'

    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word:str, player2_word:str):
        vowel_count_player1 = sum([player1_word.count(char) for char in MostVowels.vowels])
        vowel_count_player2 = sum([player2_word.count(char) for char in MostVowels.vowels])
        if vowel_count_player1 > vowel_count_player2:
            return 1
        elif vowel_count_player2 > vowel_count_player1:
            return 2
        else:
            pass

class RockPaperScissors(WordGame):
    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word:str, player2_word:str):
        valid_words = ['rock', 'paper', 'scissors']
        if (player1_word == player2_word) or ((player1_word not in valid_words) and (player2_word not in valid_words)):
            pass
        elif player1_word not in valid_words:
            return 2
        elif player2_word not in valid_words:
            return 1 
        elif player1_word == 'rock':
            if player2_word == 'paper':
                return 2
            else:
                return 1
        elif player1_word == 'paper':
            if player2_word == 'scissors':
                return 2
            else:
                return 1
        else: #scissors
            if player2_word == 'rock':
                return 2
            else:
                return 1

def main():
    p = RockPaperScissors(4)
    p.play()

#main()
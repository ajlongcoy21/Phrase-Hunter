import random

from .phrase import Phrase

# Define phrases constant

GAME_PHRASES = [
    'Life is like a box of chocloates',
    'Knock it out of the park',
    'Down for the count',
    'Throw in the towel',
    'Birds of a feather flock together'
]

class Game():

    # Define class attributes 
    missed = None
    phrases = None
    active_phrase = None
    guesses = []

    def __init__(self):

        self.missed = 0
        self.guesses = []
        self.phrases = []

        for string_phrase in GAME_PHRASES:
            self.phrases.append(Phrase(string_phrase))

        self.active_phrase = self.phrases[0]

    def start(self):
        """
        Calls the welcome method, creates the game loop, calls the get_guess method, 
        adds the user's guess to guesses, increments the number of missed by one if 
        the guess is incorrect, calls the game_over method.
        """

        # Setup rounds to loop until the user is done playing the game
        continue_rounds = True

        # Display the welcome information
        self.welcome()

        # while the user wants to continue playing 
        while continue_rounds:

            # Each time the player wants to play reset game information to start a fresh game
            self.reset_game()
            continue_game = True
            player_won = False

            # contintue to play the game until the user runs out of lives or guesses the phrase
            while continue_game and self.missed < 5:

                # Show the phrase and get user guess
                self.active_phrase.display(self.guesses)
                self.get_guess()

                # Check the player guess
                if self.active_phrase.check_letter(self.guesses[-1]):
                    # Check to see if user guessed the phrase completly
                    if self.active_phrase.check_complete(self.guesses):
                        # player won
                        player_won = True
                        continue_game = False
                    else:
                        # player needs to continue to guess
                        pass
                else:
                    # guess was incorrect reduce lives and display message
                    self.missed += 1
                    print("\nYou have {} out of 5 lives remaining!".format(5-self.missed))

            # Check to see if the player won
            if player_won:
                self.active_phrase.display(self.guesses)
                self.game_over("\nCongratulations you won!")
            else:
                self.game_over("\nSorry you lost!")

            # ask the user if they want to play again
            continue_rounds = self.ask_play_again()

        # Display exit message to the user
        self.game_over("\nThank you for playing this game! Hope to see you back soon :)\n")

    def get_random_phrase(self):
        """
        This method randomly retrieves one of the phrases stored in the phrases list and returns it.
        """
        return random.choice(self.phrases)

    def welcome(self):
        """
        This method prints a friendly welcome message to the user at the start of the game
        """
        print("\n")
        print("*"*120)
        print("""
        Welcome to Phrase Hunter Game! We will select a random phrase for you to guess until you
        get the correct answer or run out of chances (5 in total). After each guess, if it is correct
        we update the phrase with the letter shown, if it is wrong we will let you know and how many
        chances you have left. Good luck and have fun!
            """)
        print("*"*120)
        print("\n")

    def get_guess(self):
        """
        This method gets the guess from a user and records it in the guesses attribute.
        """

        guess_ok = False

        # Check user guess before returing the value to the game
        while not guess_ok:
            user_guess = input("\nGuess a letter: ")

            if len(user_guess) > 1:
                print("Sorry, your guess has too many characters. Please retry.")
            elif not user_guess.isalpha():
                print("Sorry, your guess is not a letter from a-z. Please retry.")
            else:
                self.guesses.append(user_guess.lower())
                guess_ok = True
        

    def game_over(self, message):
        """
        docstring
        """
        print(message)

    def reset_game(self):
        self.missed = 0
        self.active_phrase = self.get_random_phrase()
        self.guesses = []

    def ask_play_again(self):
        """
        Asks the user if they want to play again
        """
        
        asking = True
        question = "\nWould you like to play again (Y/N): "

        while asking:
            player_answer = input(question)
            if player_answer.upper() == "N":
                return False
            elif player_answer.upper() == "Y":
                return True
            else:
                question = "Sorry I did not understand your reply, would you like to play again (Y/N): "
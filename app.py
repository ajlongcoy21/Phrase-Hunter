# Import your Game class

from phrasehunter.game import Game

# Create your Dunder Main statement.

def main():
    my_game = Game()
    my_game.start()
    

if __name__ == '__main__':
    main()

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop

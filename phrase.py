# Create your Phrase class logic here.

class Phrase():

    phrase = None

    def __init__(self, phrase):

        self.phrase = phrase.lower()

    def display(self, guessed_letters):
        """
        This prints out the phrase to the console with guessed letters 
        visibile and unguessed letters as underscores.

        parameters:
        guessed_letters - List of letters guessed by the user

        returns: 
        N/A
        """

        # Set display string blank
        display_string = "\n"

        # Loop through each character in the phrase
        for character in self.phrase:

            # If the character is in the guessed_letters list or it is a space add the character to the display_string else add an "_"
            if (character in guessed_letters):
                display_string += character
            elif character == " ":
                display_string += "  "
            else:
                display_string += " _ "    

        # Display the phrase with updated information
        print(display_string)

    def check_letter(self, letter):
        """
        Checks to see if the letter selected by the user matches a letter in the phrase.

        parameters:
        letter - string with single character (a-z)

        returns: 
        Bool
        """
        # Loop through each character in the phrase
        for character in self.phrase:
            # If the letter is in the phrase return true else return false
            if character == letter.lower():
                return True
        
        return False      

    def check_complete(self, guessed_letters):
        """
        Checks to see if the whole phrase has been guessed.

        parameters:
        guessed_letters - List of letters guessed by the user

        returns: 
        Bool
        """

        # Loop through each character in the phrase
        for character in self.phrase:

            # If the character is not in the guessed_letters list return false
            if (character not in guessed_letters) and character != " ":
                return False

        # All letters guess so return true
        return True    

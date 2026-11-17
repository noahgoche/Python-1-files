"""
* Name         : M13 T1: GUI Assignment
* Author       : Noah Goche
* Created      : 7/29/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Class creates a game that has a gui with buttons from 1 to max, a value given by the user, and the user must click buttons
to guess the value
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

import tkinter
import random

class NumberGuesser:

    def __init__(self, max):
        """Creates the Number Guesser game, creating the window and buttons from 1 to max that are used for guessing a random value from 1 to max
        """
        if not isinstance(max, int) or not 0 < max:
            raise ValueError
        
        self.max = max
        self.guessed_list = []
        self.random_number = 0
        self.m = tkinter.Tk() # where m is the name of the main window object
        self.m.title("Number Guesser Game")
        self.label = tkinter.Label(self.m, text="Start the game or click exit to close")
        self.label.grid(row=0)
        #Creates exit and start game buttons side by side
        self.exit_Button = tkinter.Button(self.m, text='Exit', width=25, command=self.m.destroy).grid(row=1, column=0)
        self.start_Button = tkinter.Button(self.m, text='Start Game', width=25, command=self.start_game).grid(row=1, column=1)

        #Following code creates buttons 1 to max in rows of 5 and stores them in the button_list
        self.button_list = []
        count = 1
        while(count <= max):
            button = tkinter.Button(self.m, text = str(count), width=25)
            button.grid(row=((count-1)//5+2), column=((count-1)%5))
            button.config(command=lambda button_this = button: self.check_button_val(button_this))
            self.button_list.append(button)
            count = count + 1

        self.m.mainloop()

    def start_game(self):
        """Starts/resets the game by setting a new random value, clearing the guessed list, and enabling the buttons
        """
        self.random_number = random.randint(1, self.max)
        self.label.config(text="Pick a number")
        self.guessed_list = []
        for widget in self.m.winfo_children():
            if isinstance(widget, tkinter.Button):
                widget.config(state="normal")        

    def winner(self):
        """If the user guesses the correct value then a window will open displaying a winning message 
        along with the values the user guessed. The game will then be reset by calling the start game function
        """
        self.label.config(text="Winner!")
        winner_window = tkinter.Tk()
        winner_window.geometry("300x50")
        winner_window.title("WINNER")

        winner_window_label = tkinter.Label(winner_window, text="You win").grid(column=0)

        guessed_numbers = ", ".join(self.guessed_list)

        guessed_label = tkinter.Label(winner_window, text="Guessed numbers: " + guessed_numbers).grid(column=1)
        self.start_game()

    def check_button_val(self, button):
        """Takes a button pressed and if the button's text matches the value of the random number
        it triggers the winner function otherwise it deactivates the button and adds the text value
        to the list of guesses
        Param: button takes the current button pressed 
        """
        if(button.cget("text") == str(self.random_number)):
            self.winner()
        else:
            button.config(state="disabled")
            self.add_guess(button.cget("text"))
            
    def add_guess(self, guess):
        """Adds the guess value to the list of guessed values
        Param: guess is the text of the value the user incorrectly guessed when pressing a button
        """
        self.guessed_list.append(guess)


def main():
    game = NumberGuesser(2)


if __name__ == '__main__':
    main()
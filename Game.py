from model.Snake import Snake
from model.Board import Board
from tkinter import Tk, Label, Button
import tkinter as tk

snake = Snake(0, 0, 3, 2)
board = Board(20, 20)

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("PythonGame - Snake inspired")

        self.label = Label(master, text="Hello in PythonGame!")
        self.label.pack()

        self.greet_button = Button(master, text="Start!", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Hall Of Fame", command=self.hall_of_fame)
        self.close_button.pack()

        self.close_button = Button(master, text="Exit", command=master.quit)
        self.close_button.pack()


    def greet(self):
        print("Greetings!")


    def play_game(self):
        print("Game is being played!")


    def hall_of_fame(self):
        print("Hall of fame displayed!")


root = Tk()
root.wm_minsize(500, 500)
my_gui = MyFirstGUI(root)
root.mainloop()

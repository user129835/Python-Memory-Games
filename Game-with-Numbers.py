'''
This game was created for purpose of training your brain (specifically your hipocampus (part of the brain thats responsible for short-term memory)).
When program is started Python creates a 777x420px window from tkinter library, it welcoms user with a title and two buttons - to Start or to Exit the program.
When guessing game is started Python generates 6 random numbers from 1-10 and showes them on screen for 1sec and the hides them. Asks user to enter them in the input box,
and if the answer is correct, Python then shows another tkinter window showing if user has entered numbers correctly or incorrectly. 
Code is free to use. Ofc right?! its on Github :D
    --- Made by userinwoods --- 
'''

import tkinter as tk
from tkinter import messagebox
import random
import time


class MemoryGame:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Memory Game")
        self.master.geometry("777x420")

        self.numbers = []

        # Create greeting label
        self.greeting_label = tk.Label(self.master, text="Welcome to Memory Game!", font=("Arial", 25))
        self.greeting_label.pack(pady=20)

        # Create sub label
        self.greeting_label = tk.Label(self.master, text=" --- Made by userinwoods :) --- ", font=("Arial", 12))
        self.greeting_label.pack(pady=5)

        # Create start button
        self.start_button = tk.Button(self.master, text="Start", font=("Arial", 16), command=self.start_game)
        self.start_button.pack(pady=10)

        # Create exit button
        self.exit_button = tk.Button(self.master, text="Exit", font=("Arial", 16), command=self.master.quit)
        self.exit_button.pack(pady=10)

    def create_widgets(self):
        self.numbers_label = tk.Label(self.master, text="", font=("Arial", 32))
        self.numbers_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.master, font=("Arial", 16))
        self.answer_entry.pack(pady=10)

        self.check_button = tk.Button(self.master, text="Check", font=("Arial", 16), command=self.check_answer)
        self.check_button.pack(pady=10)

        # Hide exit button until game is started
        self.exit_button.pack_forget()

    def create_numbers(self):
        self.numbers = random.sample(range(1, 10), 6)
        self.numbers_label.config(text=" ".join(map(str, self.numbers)))
        self.master.after(3000, self.hide_numbers)

    def hide_numbers(self):
        self.numbers_label.config(text="")
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        answer = self.answer_entry.get()
        if len(answer) != 6:
            messagebox.showerror("Error", "Please enter 6 numbers.")
            return
        try:
            answer = [int(x) for x in answer]
        except ValueError:
            messagebox.showerror("Error", "Please enter only numbers.")
            return
        if answer == self.numbers:
            messagebox.showinfo("Result", "Correct")
        else:
            messagebox.showinfo("Result", "Incorrect")
        self.reset_game()

    def reset_game(self):
        self.answer_entry.delete(0, tk.END)
        self.create_numbers()
        self.answer_entry.focus_set()

    def start_game(self):
        self.create_widgets()
        self.create_numbers()

        # Show exit button
        self.exit_button.pack(pady=10)

        # Hide start button
        self.start_button.pack_forget()

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    game = MemoryGame()
    game.run()

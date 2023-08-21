import random
import tkinter as tk
from tkinter import messagebox

count=0
size=16
class NumberGuessingGame:
    def __init__(self, window):
        self.window = window
        window.geometry("600x400")
        window.resizable(width=False, height=False)
        window.title("Number Guessing Game")
        window.config(bg="#3b5998")
        self.random_number = 0
        self.guessed_number_value = 0
        self.number_of_guesses = 0
        self.user_name = ""
        self.show_main_page()
    def increase_animation(self):
        global size,count
        if count <10:
            size +=2

            count +=1
            window.after()
        pass
    def decrease_animation(self):
        pass
    def show_instructions(self):
        instructions = """ **** Game Instructions ****
    1. Write two numbers for the range in which the random number will be generated.
    2. Write a number to guess.
    3. Continue according to the messages in the game. Have Fun!
    """
        messagebox.showinfo("Game Instructions", instructions)

    def create_menu(self):
        menu = tk.Menu(self.window)
        instructions_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Game Instructions", menu=instructions_menu)
        instructions_menu.add_command(
            label="Show Instructions", command=self.show_instructions
        )
        self.window.configure(menu=menu)

    def show_main_page(self):
        self.clear_frame()
        self.create_menu()

        # Title
        title = tk.Label(
            self.window,
            text="*** Number Guessing Game ***",
            font=("Times New Roman", 15, "bold"),
            fg="#3b5998",
            bg="#FAC43C",
        )
        title.place(x=140, y=30)

        user_name_label = tk.Label(
            self.window,
            text="Hi, what is your name?  ",
            font=("Times New Roman", 13, "bold", "italic"),
            fg="#3b5998",
            bg="#FAC43C",
        )
        user_name_label.place(x=171, y=100)

        self.name_entry = tk.Entry(self.window, font=("Times New Roman", 13, "italic"))
        self.name_entry.place(x=170, y=150)

        show_greeting_button = tk.Button(
            self.window,
            text=" Save the name ->",
            font=("Times New Roman", 13,),
            fg="#3b5998",
            command=self.display_greeting,
        )
        show_greeting_button.place(x=400, y=150)

        self.show_greeting_label = tk.Label(self.window, text="", bg="#3b5998")
        self.show_greeting_label.place(x=100, y=200)

        self.show_play_game_label = tk.Label(self.window, text="", bg="#3b5998")
        self.show_play_game_label.place(x=170, y=240)

        # Buttons
        exit_button = tk.Button(
            self.window,
            text="Exit Game",
            font=("Times New Roman", 14, "bold"),
            fg="#3b5998",
            bg="#FAC43C",
            command=exit,
        )
        exit_button.place(x=300, y=320)

        play_button = tk.Button(
            self.window,
            text="Play Game",
            font=("Times New Roman", 14, "bold"),
            fg="#3b5998",
            bg="#FAC43C",
            command=self.show_second_page,
        )
        play_button.place(x=170, y=320)

    def display_greeting(self):
        self.user_name = self.name_entry.get()
        self.show_greeting_label.config(
            text=f"Nice to meet you {self.user_name}, I am your game guide now :)",
            font=("Times New Roman", 13, "bold", "italic"),
            fg="#3b5998",
            bg="#FAC43C",
        )
        self.show_play_game_label.config(
            text="Press play game button to start! ",
            font=("Times New Roman", 13, "bold"),
            fg="#3b5998",
            bg="#FAC43C",
        )

    def show_second_page(self):
        self.clear_frame()
        self.create_menu()

        title = tk.Label(
            self.window,
            text="*** Number Guessing Game ***",
            font=("Times New Roman", 15, "bold"),
            fg="#3b5998",
            bg="#FAC43C",
        )
        title.place(x=140, y=30)

        self.range_label = tk.Label(
            self.window,
            text=f"Enter 2 value for range to guess {self.user_name}: (e.g., 1-100) ",
            font=("Times New Roman", 13, "bold", "italic"),
            fg="#3b5998",
            bg="#FAC43C",
        )
        self.range_label.place(x=130, y=100)

        self.show_guessing_widgets_button = tk.Button(
            self.window,
            text=" Save the range ->",
            font=("Times New Roman", 13),
            fg="#3b5998",
            command=self.display_guessing_widgets,
        )
        self.show_guessing_widgets_button.place(x=400, y=150)

        self.range_entry = tk.Entry(self.window, font=("Times New Roman", 13))
        self.range_entry.place(x=170, y=150)

        self.show_message_label = tk.Label(
            self.window,
            text="",
            font=("Times New Roman", 13, "bold", "italic"),
            bg="#3b5998",
        )
        self.show_message_label.place(x=130, y=210)

        # Buttons
        exit_button = tk.Button(
            self.window,
            text="Exit Game",
            font=("Times New Roman", 14, "bold"),
            fg="#3b5998",
            bg="#FAC43C",
            command=exit,
        )
        exit_button.place(x=300, y=320)

        play_button = tk.Button(
            self.window,
            text="Play Game",
            font=("Times New Roman", 14, "bold"),
            fg="#3b5998",
            bg="#FAC43C",
            command=self.show_main_page,
        )
        play_button.place(x=170, y=320)

        self.user_name = ""

    def calculate_guess_result(self):
        self.save_guess_button.configure(state="normal")

        self.number_of_guesses += 1

        self.guessed_number_value = self.guess_entry.get()
        if not self.guessed_number_value:
            self.show_message_label.config(
                text="Please enter a guess before submitting.",
                font=("Times New Roman", 13, "bold", "italic"),
                fg="#3b5998",
                bg="#FAC43C",
            )
            return

        if self.guessed_number_value.isdigit():
            self.guessed_number_value = int(self.guessed_number_value)
        else:
            self.show_message_label.config(
                text="Guess is not a valid number.",
                font=("Times New Roman", 13, "bold", "italic"),
                fg="#3b5998",
                bg="#FAC43C",
            )

        if self.guessed_number_value == self.random_number:
            message = "Congratulations! Your guess is correct!\n"
            message += (
                f"You guessed the correct number after {self.number_of_guesses} retries"
            )
            self.save_guess_button.configure(state="disabled")
            message += "\n" + "Click on Play to start a new game"

        elif self.guessed_number_value > self.random_number:
            message = "Your guess is too high. Try again."
        else:
            message = "Your guess is too low. Try again."
        self.show_message_label.config(
            text=message,
            font=("Times New Roman", 13, "bold", "italic"),
            fg="#3b5998",
            bg="#FAC43C",
        )
        self.show_message_label.place(x=140, y=210)

    def display_guessing_widgets(self):
        range_text = self.range_entry.get()
        if "-" not in range_text:
            self.show_message_label.config(
                text="Invalid range format. Please use format like '1-100'",
                font=("Times New Roman", 13, "bold", "italic"),
                fg="#3b5998",
                bg="#FAC43C",
            )

            return
        try:
            bottom_range, top_range = list(map(int, self.range_entry.get().split("-")))

        except ValueError:
            self.show_message_label.config(
                text="Invalid range values. Please enter valid integers.",
                font=("Times New Roman", 13, "bold", "italic"),
                fg="#3b5998",
                bg="#FAC43C",
            )
            return

        if bottom_range >= top_range:
            self.show_message_label.config(
                text="Please enter a valid range.Bottom range must be smaller",
                font=("Times New Roman", 13, "bold", "italic"),
                fg="#3b5998",
                bg="#FAC43C",
            )

            return

        self.random_number = random.randint(bottom_range, top_range)

        self.range_entry.destroy()
        self.range_label.destroy()
        self.show_guessing_widgets_button.destroy()

        self.show_message_label.config(text="", fg="#3b5998", bg="#3b5998")
        guess_label = tk.Label(
            self.window,
            text="Enter your guess: ",
            font=("Times New Roman", 13, "bold", "italic"),
            fg="#3b5998",
            bg="#FAC43C",
        )
        guess_label.place(x=170, y=100)

        self.guess_entry = tk.Entry(self.window, font=("Times New Roman", 13))
        self.guess_entry.place(x=170, y=155)

        self.save_guess_button = tk.Button(
            self.window,
            text=" Submit guess ->",
            font=("Times New Roman", 13,),
            fg="#3b5998",
            command=lambda: self.calculate_guess_result(),
        )
        self.save_guess_button.place(x=400, y=155)

        # Buttons
        exit_button = tk.Button(
            self.window,
            text="Exit Game",
            font=("Times New Roman", 14, "bold"),
            fg="#3b5998",
            bg="#FAC43C",
            command=exit,
        )
        exit_button.place(x=300, y=320)

        play_button = tk.Button(
            self.window,
            text="Play Again",
            font=("Times New Roman", 14, "bold"),
            fg="#3b5998",
            bg="#FAC43C",
            command=self.show_main_page,
        )
        play_button.place(x=170, y=320)

    # It destroys all widgets:
    def clear_frame(self):
        for widget in self.window.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    app = NumberGuessingGame(window)
    window.mainloop()

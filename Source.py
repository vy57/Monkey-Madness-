import random
import time
from tkinter import Tk, Label, Button, Text, Scrollbar, END, INSERT
from PIL import ImageTk, Image

# Monkey class
class Monkey:
    def __init__(self, name, banana_count=0, health=100):
        self.name = name
        self.banana_count = banana_count
        self.health = health

    def eat_banana(self):
        self.banana_count += 1
        output_text.config(state="normal")
        output_text.insert(INSERT, f"{self.name} ate a banana!\n")
        output_text.config(state="disabled")

    def display_stats(self):
        output_text.config(state="normal")
        output_text.insert(INSERT, f"{self.name}'s Banana Count: {self.banana_count}\n")
        output_text.insert(INSERT, f"{self.name}'s Health: {self.health}%\n")
        output_text.config(state="disabled")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            output_text.config(state="normal")
            output_text.insert(INSERT, f"{self.name} is out of health!\n")
            output_text.config(state="disabled")
            return True
        return False

    def play_game(self):
        output_text.config(state="normal")
        output_text.insert(INSERT, f"{self.name} wants to play a game!\n")
        output_text.config(state="disabled")
        time.sleep(1)
        result = random.choice(["win", "lose"])
        if result == "win":
            output_text.config(state="normal")
            output_text.insert(INSERT, f"{self.name} won the game! You received a banana.\n")
            output_text.config(state="disabled")
            self.eat_banana()
        else:
            output_text.config(state="normal")
            output_text.insert(INSERT, f"{self.name} lost the game!\n")
            output_text.config(state="disabled")

# Game initialization
monkeys = []
monkey_names = ["Jack", "Charlie", "Oliver", "Max", "Leo"]
for name in monkey_names:
    monkeys.append(Monkey(name))

obstacles = ["Snake", "Tiger", "Crocodile", "Bee", "Spider"]

# Create a Tkinter window
window = Tk()
window.title("Monkey Madness")
window.attributes('-fullscreen', True)  # Set fullscreen mode
window.configure(bg="blue")  # Set the background color to blue

# Function to display monkey image
def display_monkey_image():
    image = Image.open("monkey.png")
    image = image.resize((200, 200), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    image_label = Label(window, image=image)
    image_label.image = image
    image_label.place(x=150, y=100)

# Function to handle menu choice
def handle_choice(choice):
    if not buttons_enabled:
        return

    disable_buttons()  # Disable buttons during cooldown

    if choice == "1":
        monkey = random.choice(monkeys)
        monkey.eat_banana()
    elif choice == "2":
        for monkey in monkeys:
            monkey.display_stats()
    elif choice == "3":
        obstacle = random.choice(obstacles)
        output_text.config(state="normal")
        output_text.insert(INSERT, f"You encountered a {obstacle}!\n")
        output_text.config(state="disabled")
        time.sleep(1)

        monkey = random.choice(monkeys)
        damage = random.randint(10, 30)
        if monkey.take_damage(damage):
            monkeys.remove(monkey)
    elif choice == "4":
        output_text.config(state="normal")
        output_text.insert(INSERT, "You enter a dense jungle...\n")
        output_text.config(state="disabled")
        time.sleep(1)
        event = random.random()
        if event < 0.3:
            output_text.config(state="normal")
            output_text.insert(INSERT, "You found a banana tree!\n")
            output_text.config(state="disabled")
            monkey = random.choice(monkeys)
            monkey.eat_banana()
        elif event < 0.6:
            output_text.config(state="normal")
            output_text.insert(INSERT, "You stumbled upon a hidden cave!\n")
            output_text.config(state="disabled")
            monkey = random.choice(monkeys)
            monkey.health += 20
            if monkey.health > 100:
                monkey.health = 100
            output_text.config(state="normal")
            output_text.insert(INSERT, f"{monkey.name}'s health has increased to {monkey.health}%.\n")
            output_text.config(state="disabled")
        else:
            output_text.config(state="normal")
            output_text.insert(INSERT, "You got lost in the jungle and found nothing.\n")
            output_text.config(state="disabled")
    elif choice == "5":
        monkey = random.choice(monkeys)
        monkey.play_game()
    elif choice == "6":
        output_text.config(state="normal")
        output_text.insert(INSERT, "Thank you for playing Monkey Madness!\n")
        output_text.config(state="disabled")
        window.after(2000, window.quit)  # Close the window after 2 seconds

    window.after(2000, enable_buttons)  # Enable buttons after cooldown
    window.after(2000, clear_output_text)  # Clear output text after 2 seconds

# Function to disable buttons during cooldown
def disable_buttons():
    global buttons_enabled
    buttons_enabled = False
    button1.config(state="disabled")
    button2.config(state="disabled")
    button3.config(state="disabled")
    button4.config(state="disabled")
    button5.config(state="disabled")
    button6.config(state="disabled")

# Function to enable buttons after cooldown
def enable_buttons():
    global buttons_enabled
    buttons_enabled = True
    button1.config(state="normal")
    button2.config(state="normal")
    button3.config(state="normal")
    button4.config(state="normal")
    button5.config(state="normal")
    button6.config(state="normal")

# Function to clear the output text
def clear_output_text():
    output_text.config(state="normal")
    output_text.delete(1.0, END)
    output_text.config(state="disabled")

# Create a text box to display the output
output_text = Text(window, height=10, width=40, state="disabled", bg="white")
output_text.place(x=500, y=100)

# Create a scrollbar for the output text box
scrollbar = Scrollbar(window)
scrollbar.pack(side="right", fill="y")
output_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output_text.yview)

# Display the monkey image in the Tkinter window
display_monkey_image()

# Create buttons for menu options
button1 = Button(window, text="Feed a banana", width=20, command=lambda: handle_choice("1"))
button2 = Button(window, text="Display monkey stats", width=20, command=lambda: handle_choice("2"))
button3 = Button(window, text="Encounter an obstacle", width=20, command=lambda: handle_choice("3"))
button4 = Button(window, text="Explore the jungle", width=20, command=lambda: handle_choice("4"))
button5 = Button(window, text="Play a game with a monkey", width=20, command=lambda: handle_choice("5"))
button6 = Button(window, text="Quit", width=20, command=lambda: handle_choice("6"))

# Position the buttons
button1.place(x=500, y=300)
button2.place(x=700, y=300)
button3.place(x=500, y=350)
button4.place(x=700, y=350)
button5.place(x=500, y=400)
button6.place(x=700, y=400)

buttons_enabled = True  # Variable to track button enable/disable state

window.mainloop()

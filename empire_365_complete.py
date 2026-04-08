import tkinter as tk
import random
import os
import pickle
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence

class Empire365:
    def __init__(self, root):
        self.root = root
        self.root.title("Empire 365")
        self.root.geometry("1000x700")

        # Game variables
        self.cash = 100000
        self.gold = 100
        self.diamonds = 100
        self.drugs = {"Weed": 100, "UFO": 100, "FreeJack": 100}
        self.tier = 1
        self.days_remaining = 365
        self.supermodel = "Kelly Blue Eyes"
        self.sports_cars = []
        self.current_city = "Fresno"
        self.health = 6

        self.supermodels = {
            1: "Kelly Blue Eyes",
            5: "Allotta Fagina",
            7: "Daizy Duke"
        }

        self.sports_car_list = [
            "Ferrari", "Lamborghini", "Bugatti", "Porsche", "Rolls Royce",
            "Maserati", "Bentley", "Aston Martin", "Tesla Roadster", "McLaren",
            "Jaguar F-Type", "Koenigsegg"
        ]

        self.city_gangs = {
            "Fresno": "La Familia",
            "Gotham": "The Jokers",
            "Hazard County": "The Moonshiners",
            "Hell's Kitchen": "El Diablos",
            "Las Vegas": "The Holy Rollers",
            "Los Angeles": "The Nightmare",
            "New York": "N.Y.C. Ninjas",
            "The Bronx": "The Dukes",
            "Tombstone": "The Docs",
            "Washington DC": "The Grey"
        }

        self.drug_price_ranges = {
            "Fresno": {"Weed": (100, 200), "UFO": (1000, 2000), "FreeJack": (500, 1000)},
            "Gotham": {"Weed": (150, 300), "UFO": (1200, 2500), "FreeJack": (600, 1200)},
            "Hazard County": {"Weed": (80, 160), "UFO": (900, 1800), "FreeJack": (450, 900)},
            "Hell's Kitchen": {"Weed": (130, 260), "UFO": (1100, 2200), "FreeJack": (550, 1100)},
            "Las Vegas": {"Weed": (140, 280), "UFO": (1300, 2600), "FreeJack": (650, 1300)},
            "Los Angeles": {"Weed": (160, 320), "UFO": (1400, 2800), "FreeJack": (700, 1400)},
            "New York": {"Weed": (170, 340), "UFO": (1500, 3000), "FreeJack": (750, 1500)},
            "The Bronx": {"Weed": (180, 360), "UFO": (1600, 3200), "FreeJack": (800, 1600)},
            "Tombstone": {"Weed": (90, 180), "UFO": (950, 1900), "FreeJack": (475, 950)},
            "Washington DC": {"Weed": (155, 310), "UFO": (1350, 2700), "FreeJack": (675, 1350)}
        }

        self.load_start_screen()

    def load_start_screen(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        gif_path = os.path.join(base_dir, "start.gif")
        if not os.path.exists(gif_path):
            messagebox.showerror("GIF Error", f"Could not find start.gif at {gif_path}")
            self.root.destroy()
            return

        self.canvas = tk.Canvas(self.root, width=1000, height=700)
        self.canvas.pack()

        self.frames = [ImageTk.PhotoImage(img.copy().resize((500, 350)))
                       for img in ImageSequence.Iterator(Image.open(gif_path))]
        self.gif_frame = self.canvas.create_image(500, 350, anchor="center", image=self.frames[0])
        self.animate(0)

        self.canvas.bind("<Button-1>", self.on_start_click)

    def animate(self, counter):
        self.canvas.itemconfig(self.gif_frame, image=self.frames[counter])
        self.root.after(100, self.animate, (counter + 1) % len(self.frames))

    def on_start_click(self, event):
        self.start_game()

    def start_game(self):
        print("Game has started!")
        # Placeholder for starting the game logic

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = Empire365(root)
    root.mainloop()

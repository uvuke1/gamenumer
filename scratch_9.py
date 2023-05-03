import random
import tkinter as tk
from tkinter import messagebox

class GameGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Adivina el Número")
        self.master.geometry('350x250')

        self.mode_label = tk.Label(self.master, text='Seleccione un modo (1 para un solo jugador, 2 para multijugador): ')
        self.mode_label.grid(row=0, column=0, sticky='W')

        self.mode_entry = tk.Entry(self.master)
        self.mode_entry.grid(row=1, column=0, padx=10, pady=10)

        self.select_button = tk.Button(self.master, text='Seleccionar', command=self.select_mode)
        self.select_button.grid(row=2, column=0, padx=10, pady=10)

    def select_mode(self):
        mode = int(self.mode_entry.get())
        if mode == 1:
            self.play_singleplayer()
        elif mode == 2:
            self.play_multiplayer()
        else:
            messagebox.showerror("Error","Modo inválido. Saliendo del juego...")

    def play_singleplayer(self):
        level_window = tk.Toplevel(self.master)
        level_window.title("Nivel")
        level_label = tk.Label(level_window, text="Selecciona un nivel (1, 2 o 3): ")
        level_label.pack()

        level_entry = tk.Entry(level_window)
        level_entry.pack()

        level_submit = tk.Button(level_window, text="Enviar", command=lambda: self.start_singleplayer(level_entry.get()))
        level_submit.pack()

    def start_singleplayer(self, level):
        level = int(level)
        if level == 1:
            start = 1
            end = 50
            attempts = 5
        elif level == 2:
            start = 1
            end = 100
            attempts = 4
        else:
            start = 1
            end = 1000
            attempts = 3

        number = self.generate_number(start, end)

        guess_window = tk.Toplevel(self.master)
        guess_window.title("Adivina")
        guess_label = tk.Label(guess_window, text="Adivina el número: ")
        guess_label.pack()

        guess_entry = tk.Entry(guess_window)
        guess_entry.pack()

        guess_submit = tk.Button(guess_window, text="Enviar", command=lambda: self.check_guess(int(guess_entry.get()), number, attempts, guess_window))
        guess_submit.pack()

    def play_multiplayer(self):
        player1_window = tk.Toplevel(self.master)
        player1_window.title("Jugador 1")
        player1_label = tk.Label(player1_window, text="Jugador 1, introduce un número secreto: ")
        player1_label.pack()

        player1_entry = tk.Entry(player1_window)
        player1_entry.pack()

        player1_submit = tk.Button(player1_window, text="Enviar",
                                   command=lambda: self.start_multiplayer(player1_entry.get(), player1_window))
        player1_submit.pack()

    def start_multiplayer(self, secret_number, player1_window):
        player2_window = tk.Toplevel(self.master)
        player2_window.title("Jugador 2")
        player2_label = tk.Label(player2_window, text="Jugador 2, intenta adivinar el número: ")
        player2_label.pack()

        player2_entry = tk.Entry(player2_window)
        player2_entry.pack()

        player2_submit = tk.Button(player2_window, text="Enviar",
                                   command=lambda: self.check_multiplayer_guess(int(player2_entry.get()),
                                                                                int(secret_number), player2_window))
        player2_submit.pack()

        player1_window.destroy()

    def check_multiplayer_guess(self, guess, secret_number, window):
        if guess == secret_number:
            messagebox.showinfo("Ganaste", "¡Felicidades! Adivinaste el número secreto.")
            window.destroy()
        elif guess < secret_number:
            messagebox.showwarning("Intenta de nuevo", "Demasiado bajo, inténtalo de nuevo.")
        else:
            messagebox.showwarning("Intenta de nuevo", "Demasiado alto, inténtalo de nuevo.")

    def generate_number(self, start, end):
        return random.randint(start, end)

    def check_guess(self, guess, number, attempts, window):
        if attempts > 0:
            if guess == number:
                messagebox.showinfo("Ganaste", f"Felicidades! Adivinaste el número en {attempts} intentos!")
                window.destroy()
            elif guess < number:
                attempts -= 1
                if number - guess <= 5:
                    messagebox.showwarning("Cerca", "Uff, estás muy cerca! Pero un poco más alto...")
                else:
                    messagebox.showwarning("Bajo", "Demasiado Bajo!")
            else:
                attempts -= 1
                if guess - number <= 5:
                    messagebox.showwarning("Cerca", "Uff, estás muy cerca! Pero un poco más bajo...")
                else:
                    messagebox.showwarning("Alto", "Demasiado Alto!")
        else:
            messagebox.showerror("Perdiste", f"Lo siento, has agotado tus intentos. El número era: {number}")
            window.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    game_app = GameGui(root)
    root.mainloop()
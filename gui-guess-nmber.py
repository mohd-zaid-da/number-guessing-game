import tkinter as tk
import random
import time

# basic variables
target = 0
attempt_left = 0
time_limit = 0
start_time = 0

def start_game(level):
    global target, attempt_left, time_limit, start_time

    if level == 1:
        attempt_left = 10
        time_limit = 60
    elif level == 2:
        attempt_left = 7
        time_limit = 45
    else:
        attempt_left = 5
        time_limit = 30

    target = random.randint(1, 100)
    start_time = time.time()

    status_lbl.config(text="Game started")
    result_lbl.config(text="")
    entry.delete(0, tk.END)

    update_timer()

def update_timer():
    elapsed = int(time.time() - start_time)
    left = time_limit - elapsed

    if left <= 0:
        timer_lbl.config(text="Time over")
        result_lbl.config(text=f"Number was {target}")
        return
    else:
        timer_lbl.config(text=f"Time left: {left}s")
        root.after(1000, update_timer)

def check():
    global attempt_left

    val = entry.get()

    if val == "":
        result_lbl.config(text="Enter something")
        return

    try:
        guess = int(val)
    except:
        result_lbl.config(text="Invalid input")
        return

    if guess < 1 or guess > 100:
        result_lbl.config(text="Enter 1-100 only")
        return

    attempt_left -= 1

    if guess == target:
        total_time = round(time.time() - start_time, 2)
        result_lbl.config(text=f"Correct! Time: {total_time}s")
        status_lbl.config(text="")
        return

    if guess > target:
        msg = "Too high"
    else:
        msg = "Too low"

    if attempt_left <= 0:
        result_lbl.config(text=f"Game over, number was {target}")
        status_lbl.config(text="")
    else:
        result_lbl.config(text=msg)
        status_lbl.config(text=f"Attempts left: {attempt_left}")

# UI
root = tk.Tk()
root.title("Guess Game")
root.geometry("350x350")

title = tk.Label(root, text="Number Guess Game", font=("Arial", 14))
title.pack(pady=10)

tk.Button(root, text="Easy", command=lambda: start_game(1)).pack(pady=3)
tk.Button(root, text="Medium", command=lambda: start_game(2)).pack(pady=3)
tk.Button(root, text="Hard", command=lambda: start_game(3)).pack(pady=3)

entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Check", command=check).pack()

status_lbl = tk.Label(root, text="")
status_lbl.pack()

timer_lbl = tk.Label(root, text="")
timer_lbl.pack()

result_lbl = tk.Label(root, text="")
result_lbl.pack(pady=10)

root.mainloop()

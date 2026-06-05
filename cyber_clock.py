import tkinter as tk
from time import strftime

def update_time():
    """Function to update the time, date, and day in real-time."""
    # Fetching current time, date, and day strings
    time_string = strftime('%H:%M:%S %p')
    date_string = strftime('%B %d, %Y')
    day_string = strftime('%A')
    
    # Updating the text of the labels
    time_label.config(text=time_string)
    date_label.config(text=f"📅 {date_string}  |  ✨ {day_string}")
    
    # Calling this function again after 1000 milliseconds (1 second)
    time_label.after(1000, update_time)

# --- GUI Windows Setup ---
root = tk.Tk()
root.title("Cyberpunk Digital Clock")
root.geometry("500x200")
root.configure(bg="#0a0a0c")  # Deep cyber-dark background
root.resizable(False, False)  # Keeps the window size fixed

# --- UI Styling & Widgets ---
# Neon Cyan Cyberpunk Theme
NEON_CYAN = "#00f0ff"
DARK_GRAY = "#1e1e24"

# Heading Label
heading = tk.Label(root, text="SYSTEM TIME", font=("Arial", 10, "bold"), fg="#555566", bg="#0a0a0c")
heading.pack(pady=(15, 0))

# Main Time Display Label
time_label = tk.Label(
    root, 
    font=("Courier New", 40, "bold"), 
    fg=NEON_CYAN, 
    bg="#0a0a0c",
    bd=10
)
time_label.pack()

# Date and Day Display Label
date_label = tk.Label(
    root, 
    font=("Arial", 12, "italic"), 
    fg="#ff007f",  # Neon Pink contrast
    bg="#0a0a0c"
)
date_label.pack(pady=(0, 15))

# --- Initialize Clock ---
update_time()

# Starts the Tkinter event loop to keep the window running
root.mainloop()

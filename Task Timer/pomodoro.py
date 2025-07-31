import tkinter as tk  # Import the Tkinter library for making GUIs (windows, buttons, etc.)
import time  # Import time library (not used here, but often used for timing)

def start_pomodoro():
    countdown(25 * 60)  # Start the countdown for 25 minutes (converted to seconds)

def countdown(time_left):
    mins, secs = divmod(time_left, 60)  # Split time_left into minutes and seconds
    work_label.config(text=f"Working: {mins:02d}:{secs:02d} left")  # Show time left in the label
    if time_left > 0:  # If there is still time left
        root.after(1000, countdown, time_left - 1)  # Wait 1 second, then call countdown again with 1 less second
    else:  # If time is up
        start_break()  # Start the break timer

def start_break():
    countdown_break(5 * 60)  # Start the break countdown for 5 minutes (in seconds)

def countdown_break(time_left):
    mins, secs = divmod(time_left, 60)  # Split break time into minutes and seconds
    work_label.config(text=f"Break: {mins:02d}:{secs:02d} left")  # Show break time left in the label
    if time_left > 0:  # If break time is not finished
        root.after(1000, countdown_break, time_left - 1)  # Wait 1 second, then call countdown_break again
    else:  # If break is finished
        reset_timer()  # Show the finished message

def reset_timer():
    work_label.config(text="Pomodoro complete! Wanna start again?")  # Update label to show session is done

root = tk.Tk()  # Create the main window for the app
root.title("Pomodoro Task Timer")  # Set the window title

work_label = tk.Label(root, text="Click Start to Begin!", font=("Arial", 18))  # Create a label to show messages/timer
work_label.pack(pady=20)  # Add the label to the window with some space around it

start_button = tk.Button(root, text="Start Pomodoro", command=start_pomodoro)  # Create a button to start the timer
start_button.pack(pady=10)  # Add the button to the window with some space

root.mainloop()  # Start the Tkinter event loop (keeps the window open and
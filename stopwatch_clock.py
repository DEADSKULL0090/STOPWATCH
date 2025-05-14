
import tkinter as tk
from datetime import datetime
import time
import threading

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch & Clock")

        self.clock_label = tk.Label(root, text="", font=("Arial", 24), fg="blue")
        self.clock_label.pack(pady=10)

        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 36), fg="green")
        self.stopwatch_label.pack(pady=20)

        button_frame = tk.Frame(root)
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Start", command=self.start_stopwatch, width=10)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_stopwatch, width=10)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_stopwatch, width=10)
        self.reset_button.grid(row=0, column=2, padx=5)

        self.running = False
        self.counter = 0

        self.update_clock()

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text="Current Time: " + now)
        self.root.after(1000, self.update_clock)

    def update_stopwatch(self):
        if self.running:
            self.counter += 1
            formatted_time = time.strftime('%H:%M:%S', time.gmtime(self.counter))
            self.stopwatch_label.config(text=formatted_time)
            self.root.after(1000, self.update_stopwatch)

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.update_stopwatch()

    def stop_stopwatch(self):
        self.running = False

    def reset_stopwatch(self):
        self.running = False
        self.counter = 0
        self.stopwatch_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchClockApp(root)
    root.mainloop()

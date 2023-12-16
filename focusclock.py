import time
import tkinter as tk

class FocusTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("专注时钟")
        self.master.geometry("300x150")

        self.time_remaining = 1500  # 初始时间为25分钟，以秒为单位
        self.is_running = False

        self.label = tk.Label(self.master, text=self.format_time(self.time_remaining), font=("Helvetica", 20))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.master, text="开始", command=self.start_timer)
        self.start_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(self.master, text="重置", command=self.reset_timer)
        self.reset_button.pack(side="right", padx=10)

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02}:{seconds:02}"

    def update_display(self):
        self.label.config(text=self.format_time(self.time_remaining))

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.run_timer()

    def run_timer(self):
        if self.time_remaining > 0 and self.is_running:
            self.time_remaining -= 1
            self.update_display()
            self.master.after(1000, self.run_timer)
        elif self.time_remaining == 0:
            self.is_running = False
            self.update_display()

    def reset_timer(self):
        self.is_running = False
        self.time_remaining = 1500
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusTimer(root)
    root.mainloop()

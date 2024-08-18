import tkinter as tk
from tkinter import ttk
import datetime

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Таймер відсотка залишкового часу")
        self.root.geometry("500x200")
        self.root.configure(bg='white')

        # Поля вводу часу
        self.start_time_label = tk.Label(root, text="Час початку (ГГ:ХХ):", bg='white')
        self.start_time_label.grid(row=0, column=0, padx=10, pady=10)
        self.start_time_entry = tk.Entry(root)
        self.start_time_entry.grid(row=0, column=1, padx=10, pady=10)

        self.end_time_label = tk.Label(root, text="Час закінчення (ГГ:ХХ):", bg='white')
        self.end_time_label.grid(row=1, column=0, padx=10, pady=10)
        self.end_time_entry = tk.Entry(root)
        self.end_time_entry.grid(row=1, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(root, text="Підтвердити", command=self.start_timer)
        self.submit_button.grid(row=2, columnspan=2, pady=10)
        


        # Відображення часу
        self.time_display = tk.Label(root, text="", font=("Helvetica", 36), bg='white')
        self.time_display.grid(row=3, columnspan=2, pady=20)

    def start_timer(self):
        start_str = self.start_time_entry.get()
        end_str = self.end_time_entry.get()

        try:
            self.start_time = datetime.datetime.strptime(start_str, "%H:%M").time()
            self.end_time = datetime.datetime.strptime(end_str, "%H:%M").time()
            self.start_time_label.grid_forget()
            self.start_time_entry.grid_forget()
            self.end_time_label.grid_forget()
            self.end_time_entry.grid_forget()
            self.submit_button.grid_forget()
            self.update_timer()
        except ValueError:
            self.time_display.config(text="Помилка формату часу")

    def update_timer(self):
        now = datetime.datetime.now().time()
        start_time = datetime.datetime.combine(datetime.date.today(), self.start_time)
        end_time = datetime.datetime.combine(datetime.date.today(), self.end_time)
        now_time = datetime.datetime.combine(datetime.date.today(), now)

        if now_time < start_time:
            percentage = 100
        elif now_time > end_time:
            percentage = 0
        else:
            total_time = end_time - start_time
            elapsed_time = now_time - start_time
            remaining_time = total_time - elapsed_time
            percentage = (remaining_time / total_time) * 100

        self.time_display.config(text=f"Залишилося: {percentage:.2f}%")
        self.root.after(100, self.update_timer)  # Оновлювати кожні 100 мс

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

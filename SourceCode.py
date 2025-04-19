import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import webbrowser
from geopy.geocoders import Nominatim
from datetime import datetime
import random

class ScheduleManager:
    def __init__(self, filename="schedules.json"):
        self.filename = filename
        self.schedules = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                self.schedules = json.load(f)
                for schedule in self.schedules:
                    if "completed" not in schedule:
                        schedule["completed"] = False
                    if "color" not in schedule:
                        schedule["color"] = self.get_random_color()
        except FileNotFoundError:
            self.schedules = []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.schedules, f)

    def add_schedule(self, title, time, location, notes=""):
        schedule = {
            "title": title,
            "time": time,
            "location": location,
            "notes": notes,
            "timestamp": datetime.strptime(time, "%Y-%m-%d %H:%M").timestamp(),
            "completed": False,
            "color": self.get_random_color()
        }
        self.schedules.append(schedule)
        self.sort_schedules()
        self.save_data()

    def delete_schedule(self, index):
        if 0 <= index < len(self.schedules):
            del self.schedules[index]
            self.save_data()

    def sort_schedules(self):
        self.schedules.sort(key=lambda x: x["timestamp"])

    def mark_completed(self, index):
        if 0 <= index < len(self.schedules):
            self.schedules[index]["completed"] = True
            self.save_data()

    def edit_schedule(self, index, title, time, location, notes):
        if 0 <= index < len(self.schedules):
            self.schedules[index]["title"] = title
            self.schedules[index]["time"] = time
            self.schedules[index]["location"] = location
            self.schedules[index]["notes"] = notes
            self.save_data()

    def get_random_color(self):
        return random.choice(["#e6f2ff", "#f2f2f2", "#e6ffe6", "#ffe6e6", "#e6e6ff"])

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Schedule Manager")
        self.geometry("800x600")
        self.configure(bg="white")
        self.schedule_manager = ScheduleManager()

        # GUI Components
        self.create_widgets()
        self.update_schedule_display()

    def create_widgets(self):
        # Schedule Display
        self.schedule_frame = tk.Frame(self, bg="white")
        self.schedule_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.scrollbar = tk.Scrollbar(self.schedule_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas = tk.Canvas(self.schedule_frame, yscrollcommand=self.scrollbar.set, bg="white", highlightthickness=0)
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.schedule_container = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.schedule_container, anchor="nw")

        # Buttons
        btn_frame = tk.Frame(self, bg="white")
        btn_frame.pack(side=tk.RIGHT, padx=10)

        # Custom style for buttons
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=6, background="#f0f0f0", foreground="#333333")

        ttk.Button(btn_frame, text="Add", command=self.add_dialog, style="TButton").pack(pady=5)
        ttk.Button(btn_frame, text="Sort", command=self.sort_schedules, style="TButton").pack(pady=5)

    def draw_rounded_rectangle(self, canvas, x, y, width, height, radius, color):
        canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline=color)
        canvas.create_arc(x + radius, y, x + radius * 2, y + radius * 2, start=180, extent=90, outline=color, fill=color)
        canvas.create_arc(x + width - radius * 2, y, x + width - radius, y + radius * 2, start=270, extent=90, outline=color, fill=color)
        canvas.create_arc(x + width - radius, y + height - radius * 2, x + width, y + height - radius, start=0, extent=90, outline=color, fill=color)
        canvas.create_arc(x, y + height - radius * 2, x + radius * 2, y + height, start=90, extent=90, outline=color, fill=color)

    def update_schedule_display(self):
        # Clear existing widgets
        for widget in self.schedule_container.winfo_children():
            widget.destroy()

        # Create new note widgets
        for i, schedule in enumerate(self.schedule_manager.schedules):
            color = schedule["color"] if not schedule["completed"] else "#d9d9d9"
            note_frame = tk.Frame(self.schedule_container, bg=color, padx=10, pady=10, bd=0, relief=tk.FLAT)
            note_frame.pack(fill=tk.X, pady=5, padx=10)

            # Create rounded rectangle background
            canvas = tk.Canvas(note_frame, width=300, height=200, bg=color, highlightthickness=0)
            canvas.pack()
            self.draw_rounded_rectangle(canvas, 10, 10, 280, 180, 10, color)

            # Add text labels
            current_time = datetime.now()
            time_left = datetime.strptime(schedule["time"], "%Y-%m-%d %H:%M") - current_time
            if time_left.total_seconds() > 0:
                days = time_left.days
                hours, remainder = divmod(time_left.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                time_left_str = f"{days}d {hours}h {minutes}m {seconds}s"
            else:
                time_left_str = "Time's up!"

            countdown_frame = tk.Frame(canvas, bg="white", width=280, height=40)
            countdown_frame.place(x=10, y=10)
            tk.Label(countdown_frame, text=time_left_str, font=("Arial", 12), bg="white").pack()

            canvas.create_text(150, 60, text=schedule["time"], font=("Arial", 12), fill="black" if not schedule["completed"] else "white", tags="text")
            canvas.create_text(150, 90, text=schedule["title"], font=("Arial", 14, "bold"), fill="black" if not schedule["completed"] else "white", tags="text")
            canvas.create_text(150, 115, text=schedule["location"], font=("Arial", 12), fill="black" if not schedule["completed"] else "white", tags="text")
            canvas.create_text(150, 140, text=schedule["notes"], font=("Arial", 12), fill="black" if not schedule["completed"] else "white", tags="text")

            # Add delete button
            delete_button = tk.Button(note_frame, text="Delete", bg="white", bd=0, highlightthickness=0,
                                       command=lambda idx=i: self.delete_schedule(idx))
            delete_button.place(x=270, y=5)

            # Add buttons at the bottom
            btn_row = tk.Frame(note_frame, bg=color)
            btn_row.pack(side=tk.BOTTOM, pady=5)

            ttk.Button(btn_row, text="Edit", command=lambda idx=i: self.edit_schedule(idx), style="TButton").pack(side=tk.LEFT, padx=2)
            ttk.Button(btn_row, text="Completed" if not schedule["completed"] else "Completed", command=lambda idx=i: self.mark_completed(idx), style="TButton").pack(side=tk.LEFT, padx=2)
            ttk.Button(btn_row, text="Location", command=lambda loc=schedule["location"]: self.show_location(loc), style="TButton").pack(side=tk.LEFT, padx=2)

        # Update canvas region
        self.schedule_container.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def mark_completed(self, index):
        self.schedule_manager.mark_completed(index)
        self.update_schedule_display()  # Refresh the display immediately

    def add_dialog(self):
        dialog = tk.Toplevel(self)
        dialog.title("Add Schedule")
        dialog.configure(bg="white")

        fields = ["Title:", "Time (YYYY-MM-DD HH:MM):", "Location:", "Notes:"]
        entries = []

        for i, field in enumerate(fields):
            tk.Label(dialog, text=field, bg="white").grid(row=i, column=0, sticky="e")
            entry = ttk.Entry(dialog, width=30)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        def submit():
            data = [e.get() for e in entries]
            try:
                datetime.strptime(data[1], "%Y-%m-%d %H:%M")
                self.schedule_manager.add_schedule(data[0], data[1], data[2], data[3])
                self.update_schedule_display()
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid time format!")

        ttk.Button(dialog, text="Submit", command=submit, style="TButton").grid(row=4, columnspan=2, pady=10)

    def delete_schedule(self, index):
        self.schedule_manager.delete_schedule(index)
        self.update_schedule_display()

    def sort_schedules(self):
        self.schedule_manager.sort_schedules()
        self.update_schedule_display()

    def edit_schedule(self, index):
        schedule = self.schedule_manager.schedules[index]
        dialog = tk.Toplevel(self)
        dialog.title("Edit Schedule")
        dialog.geometry("300x250")

        tk.Label(dialog, text="Title:").grid(row=0, column=0, padx=5, pady=5)
        title_entry = ttk.Entry(dialog)
        title_entry.grid(row=0, column=1, padx=5, pady=5)
        title_entry.insert(0, schedule["title"])

        tk.Label(dialog, text="Time (YYYY-MM-DD HH:MM):").grid(row=1, column=0, padx=5, pady=5)
        time_entry = ttk.Entry(dialog)
        time_entry.grid(row=1, column=1, padx=5, pady=5)
        time_entry.insert(0, schedule["time"])

        tk.Label(dialog, text="Location:").grid(row=2, column=0, padx=5, pady=5)
        location_entry = ttk.Entry(dialog)
        location_entry.grid(row=2, column=1, padx=5, pady=5)
        location_entry.insert(0, schedule["location"])

        tk.Label(dialog, text="Notes:").grid(row=3, column=0, padx=5, pady=5)
        notes_entry = ttk.Entry(dialog)
        notes_entry.grid(row=3, column=1, padx=5, pady=5)
        notes_entry.insert(0, schedule["notes"])

        def submit():
            self.schedule_manager.edit_schedule(index, title_entry.get(), time_entry.get(), location_entry.get(), notes_entry.get())
            self.update_schedule_display()
            dialog.destroy()

        ttk.Button(dialog, text="Submit", command=submit).grid(row=4, column=1, pady=10)

    def show_location(self, location):
        try:
            geolocator = Nominatim(user_agent="schedule_manager")
            location_data = geolocator.geocode(location)
            if location_data:
                url = f"https://www.openstreetmap.org/?mlat={location_data.latitude}&mlon={location_data.longitude}#map=15/{location_data.latitude}/{location_data.longitude}"
                webbrowser.open(url)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show location: {str(e)}")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

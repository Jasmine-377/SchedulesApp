import tkinter as tk
from tkinter import ttk, messagebox
import json
import webbrowser
from geopy.geocoders import Nominatim
from datetime import datetime

class ScheduleManager:
    def __init__(self, filename="schedules.json"):
        self.filename = filename
        self.schedules = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                self.schedules = json.load(f)
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
            "timestamp": datetime.strptime(time, "%Y-%m-%d %H:%M").timestamp()
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

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Schedule Manager")
        self.geometry("800x600")
        self.schedule_manager = ScheduleManager()
        
        # GUI Components
        self.create_widgets()
        self.update_listbox()
        
    def create_widgets(self):
        # Listbox
        self.listbox = tk.Listbox(self, width=50)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.show_location)

        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(side=tk.RIGHT, padx=10)
        
        ttk.Button(btn_frame, text="Add", command=self.add_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_schedule).pack(pady=5)
        ttk.Button(btn_frame, text="Sort", command=self.sort_schedules).pack(pady=5)

        # Map Display
        self.map_frame = tk.Frame(self)
        self.map_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for schedule in self.schedule_manager.schedules:
            self.listbox.insert(tk.END, f"{schedule['time']} - {schedule['title']}")

    def add_dialog(self):
        dialog = tk.Toplevel(self)
        dialog.title("Add Schedule")
        
        fields = ["Title:", "Time (YYYY-MM-DD HH:MM):", "Location:", "Notes:"]
        entries = []
        
        for i, field in enumerate(fields):
            tk.Label(dialog, text=field).grid(row=i, column=0)
            entry = ttk.Entry(dialog, width=30)
            entry.grid(row=i, column=1)
            entries.append(entry)
        
        def submit():
            data = [e.get() for e in entries]
            try:
                datetime.strptime(data[1], "%Y-%m-%d %H:%M")
                self.schedule_manager.add_schedule(data[0], data[1], data[2], data[3])
                self.update_listbox()
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid time format!")

        ttk.Button(dialog, text="Submit", command=submit).grid(row=4, columnspan=2)

    def delete_schedule(self):
        selected = self.listbox.curselection()
        if selected:
            self.schedule_manager.delete_schedule(selected[0])
            self.update_listbox()

    def sort_schedules(self):
        self.schedule_manager.sort_schedules()
        self.update_listbox()

    def show_location(self, event):
        selected = self.listbox.curselection()
        if selected:
            location = self.schedule_manager.schedules[selected[0]]["location"]
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
import tkinter as tk
import requests as req

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # city input
        self.city_input = tk.Entry(self)
        self.city_input.pack(side="top")
        
        # request button
        self.request_button = tk.Button(self, text="Request Weather Information", fg="green", command=self.info)
        self.request_button.pack(side="top")

        # info label
        self.info_label = tk.Entry(self)
        self.info_label.pack(side="top")

        # exit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    # reading the api key form a file
    def reading_api_key(self):
        f = open("./api_key.txt", "r")
        return f.read()

    # using the openweather api to get the current weather data
    def getting_weathe_information(self, city):
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={self.reading_api_key()}"
        r = req.get(URL).json()

        # returning only the current temprature
        return (r["main"]["temp"])
    
    def info(self):
        city = self.city_input.get()
        self.info_label.delete(0, "end")
        self.info_label.insert(0, self.getting_weathe_information(city))

root = tk.Tk()
app = Application(master=root)
app.mainloop()

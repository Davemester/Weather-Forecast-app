from tkinter import*
from WeatherForecast_GUI.WeatherScripts import *


class Application:
    def __init__(self):
        '''
        Main window settings
        '''
        self.root = Tk()
        self.root.title("Weather Forecast by Davemester")
        self.root.geometry("450x450")

        self.location_label = Label(self.root, text='Location:')
        self.date_label = Label(self.root, text="Date:")
        self.loc_entry = Entry(self.root)
        self.date_entry = Entry(self.root)

        self.frame_timezone = Label(self.root)
        self.frame_min_temp = Label(self.root)
        self.frame_max_temp = Label(self.root)
        self.frame_summary = Message(self.root)
        self.frame_precip = Label(self.root)

        self.photo = PhotoImage()
        self.icon = Canvas(self.root)
        self.icon.configure(width=190, height=190)
        self.icon.create_image(0, 0, image=self.photo)
        self.example = Label(self.root, text="(YY.MM.DD)")

        self.example.grid(row=1, column=2)
        self.location_label.grid(row=0, column=0, sticky='W')
        self.loc_entry.grid(row=0, column=1)
        self.date_label.grid(row=1, column=0, sticky='W')
        self.date_entry.grid(row=1, column=1)
        self.frame_timezone.grid(row=2, column=0, columnspan=2, sticky="W")
        self.frame_max_temp.grid(row=3, column=0, columnspan=2, sticky="W")
        self.frame_min_temp.grid(row=4, column=0, columnspan=2, sticky="W")
        self.frame_summary.grid(row=5, column=0, columnspan=2, sticky="W")
        self.frame_precip.grid(row=6, column=0, columnspan=2, sticky="W")
        self.icon.grid(row=0, column=3, rowspan=4, sticky="E")

        self.gomb1 = Button(self.root, text="Date weather" ,command=self.change_text)
        self.gomb1.grid(row=5, column=2)

        self.gomb3 = Button(self.root, text="Today weather",command=self.change_text_today)
        self.gomb3.grid(row=6, column=2)

        self.gomb2 = Button(self.root, text="Quit", command=self.root.quit)
        self.gomb2.grid(row=7, column=2)

        self.root.mainloop()

    def change_text(self):

        try:
            location = self.loc_entry.get()
            date = self.date_entry.get()
            cordinate = location_coordinates(location)
            weather = get_date_request(cordinate, date)

            self.photo = PhotoImage(file=weather_icon(weather))

            self.icon.create_image(120, 120, image=self.photo)

            self.frame_min_temp.configure(text=min_temp(weather))
            self.frame_max_temp.configure(text=max_temp(weather))
            self.frame_summary.configure(text=summary(weather))
            self.frame_timezone.configure(text=timezone(weather))
            self.frame_precip.configure(text=precip(weather))

        except:
            self.frame_timezone.configure(text="Invalid date or location format!")

    def change_text_today(self):  # TODO add more date options

        try:

            location = self.loc_entry.get()

            cordinate = location_coordinates(location)

            weather = get_request(cordinate)
            self.photo = PhotoImage(file=weather_icon(weather))

            self.icon.create_image(120, 120, image=self.photo)

            self.frame_min_temp.configure(text=min_temp(weather))
            self.frame_max_temp.configure(text=max_temp(weather))
            self.frame_summary.configure(text=summary(weather))
            self.frame_timezone.configure(text=timezone(weather))
            self.frame_precip.configure(text=precip(weather))

        except:
            self.frame_timezone.configure(text="Invalid location format")


app = Application()

from WeatherScripts import *
from tkinter import *


#def main():

    #TODO: convert to OOP style

def change_text():
    global photo
    global icon
    try:
        location = mezo.get()
        date = mezo2.get()
        cordinate = location_coordinates(location)
        weather = get_date_request(cordinate, date)

        photo = PhotoImage(file=weather_icon(weather))

        icon.create_image(120,120,image = photo)

        frame_min_temp.configure(text=min_temp(weather))
        frame_max_temp.configure(text=max_temp(weather))
        frame_summary.configure(text=summary(weather))
        frame_timezone.configure(text=timezone(weather))
        frame_precip.configure(text = precip(weather))

    except:
        frame_timezone.configure(text = "Invalid date or location format!")


def change_text_today():   #TODO add more date options
    global photo
    global icon
    try:

        location = mezo.get()

        cordinate = location_coordinates(location)

        weather = get_request(cordinate)
        photo = PhotoImage(file=weather_icon(weather))

        icon.create_image(120, 120, image=photo)

        frame_min_temp.configure(text=min_temp(weather))
        frame_max_temp.configure(text=max_temp(weather))
        frame_summary.configure(text=summary(weather))
        frame_timezone.configure(text=timezone(weather))
        frame_precip.configure(text = precip(weather))

    except:
        frame_timezone.configure(text="Invalid location format")


ablak = Tk()
ablak.title('Weather Forecast')
ablak.configure()
photo = PhotoImage()

ablak.geometry("450x450")

location_label = Label(ablak,text = 'Location:')
date_label = Label(ablak,text = "Date:")
mezo = Entry(ablak)
mezo2 = Entry(ablak)
frame_timezone = Label(ablak)
frame_min_temp = Label(ablak)
frame_max_temp = Label(ablak)
frame_summary = Message(ablak)
frame_precip = Label(ablak)
icon = Canvas(ablak)
icon.configure(width = 190,height = 190)
icon.create_image(0,0,image = photo)
example = Label(ablak,text = "(YY.MM.DD)")
example.grid(row = 1,column = 2)

location_label.grid(row = 0,column = 0,sticky = 'W' )
mezo.grid(row = 0, column = 1)
date_label.grid(row = 1,column = 0,sticky = 'W')
mezo2.grid(row = 1,column = 1)
frame_timezone.grid(row = 2,column = 0,columnspan = 2,sticky = "W")
frame_max_temp.grid(row = 3,column = 0,columnspan = 2,sticky = "W")
frame_min_temp.grid(row = 4,column = 0,columnspan = 2,sticky = "W")
frame_summary.grid(row = 5,column = 0,columnspan = 2,sticky = "W")
frame_precip.grid(row = 6,column = 0,columnspan = 2,sticky = "W")
icon.grid(row = 0,column = 3,rowspan = 4,sticky = "E")

gomb1 = Button(ablak,text = "Date weather",command = change_text)
gomb1.grid(row = 5,column = 2)

gomb3 = Button(ablak, text="Today weather", command=change_text_today)
gomb3.grid(row = 6,column = 2)

gomb2 = Button(ablak,text = "Quit",command = ablak.quit)
gomb2.grid(row = 7,column = 2)


ablak.mainloop()


#if __name__ == "__main__":
    #main()

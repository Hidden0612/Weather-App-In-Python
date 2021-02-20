import tkinter as tk
import requests
import time
#==============================#  @Hidden0612  #==============================#
def getweather(canvas):
    city=textfield.get()
    api="http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f84778c5cb76e1bdde236c2ecba140c1"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp'] - 273.15)
    min_temp=int(json_data['main']['temp_min'] - 273.15)
    max_temp=int(json_data['main']['temp_max'] - 273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S" , time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset=time.strftime("%I:%M:%S" , time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info=condition+'\n'+str(temp)+"ْ C"
    final_data='\n'+'Max Temp: '+str(max_temp)+'\n'+'Min Temp: '+str(min_temp)+'\n'+'Pressure: '+str(pressure)\
               +'\n'+'Humidity: '+str(humidity)+'\n'+'Wind speed: '+str(wind)+'\n'+'Sunrise: '\
               +str(sunrise)+'\n'+'Sunset: '+str(sunset)
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry('600x400') ; canvas.title("Weather")
textfield = tk.Entry(canvas , font=("tahoma",20)) ; textfield.pack(pady=20)
textfield.focus() ; textfield.bind('<Return>' , getweather)
label1=tk.Label(canvas,font=("tahoma",20)) ; label1.pack()
label2=tk.Label(canvas,font=("tahoma",15)) ; label2.pack()
canvas.mainloop()
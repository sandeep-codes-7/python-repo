from django.shortcuts import render   #type: ignore
from django.http import HttpResponse  # type: ignore
import requests,json  # type: ignore

from dotenv import load_dotenv #type: ignore
import os

load_dotenv()


# Create your views here.
def index(request):
    return render(request, 'weather_app/index.html',{})

def weather(request):

    icons = {
        232:'weather_app/images/thunderstorm.svg',
        321:'weather_app/images/drizzle.svg',
        531:'weather_app/images/rain.svg',
        622:'weather_app/images/snow.svg',
        781:'weather_app/images/atmosphere.svg',
        800:'weather_app/images/clear.svg',
        804:'weather_app/images/clouds.svg',
    }
    if request.method == 'POST':
        place = request.POST.get('city')
        open_cage_url = f"https://api.opencagedata.com/geocode/v1/json?q={place}&key={os.getenv("GEO_API")}"
        req = requests.get(open_cage_url)
        data_1 = req.json()
        longi = data_1['results'][0]['geometry']['lng']
        lati = data_1['results'][0]['geometry']['lat']
        API_key = "<API KEY>"
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lati}&lon={longi}&appid={os.getenv('API_KEY')}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['main']
            icon = data['weather'][0]['id']
            if icon in range(0,232+1):
                image = icons[232]
            elif icon in range(0,321+1):
                image = icons[321]
            elif icon in range(0,531+1):
                image = icons[531]
            elif icon in range(0,622+1):
                image = icons[622]
            elif icon in range(0,781+1):
                image = icons[781]
            elif icon in range(0,800+1):
                image = icons[800]
            else:
                image = icons[804]  
        else:
            return HttpResponse("Error")
        return render(request, 'weather_app/weather.html',{
            'place':place.capitalize(),
            'weather':data['weather'][0]['main'],
            'icon':icon,
            'image':icons[804],
            'data':data,
            'temperature':f"{data['main']['temp']} °C\n\n",
            'feels_like':f"{data['main']['feels_like']} °C\n\n",
            'min':f"{data['main']['temp_min']} °C\n\n",
            'max':f"{data['main']['temp_max']} °C\n\n",
            'humidity':f"{data['main']['humidity']} %",
            'pressure':f"{data['main']['pressure']} hPa",
            'wind_speed':f"{data['wind']['speed']} m/s",
            'visibility':f"{data['visibility']} m or {data['visibility']/1000} km",
            })

    
    



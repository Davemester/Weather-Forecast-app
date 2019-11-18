from geopy import Nominatim
from datetime import datetime
import requests



def location_coordinates(adress):

    """
    Return with the latitude and longitude coordinates
     of the adress parameter
    """
    location = Nominatim(user_agent="my-application").geocode(str(adress))
    lat = location.latitude
    long = location.longitude

    return str(lat), str(long)

def get_request(coordinates):
    """

    :param coordinates:
    :return: with the JSON response from Dark Sky server
    """

    DSAPI_KEY = 'c1dd372cfbc36733fc1e395cba083fe8'  # the API key to the request

    option_list = "exclude=currently,minutely,hourly,alerts&amp;units=si,lang=hu" #TODO: Units and language not work

    adress = coordinates
    req = f"https://api.darksky.net/forecast/{DSAPI_KEY}/{adress[0]},{adress[1]}?{option_list}"
    response = requests.get(req)
    json_res = response.json()
    return json_res

def get_date_request(coordinates,date):

        """

        :param coordinates,date:
        :return: with the JSON response (depend on the given day) from Dark Skye server
        """

        DSAPI_KEY = 'c1dd372cfbc36733fc1e395cba083fe8'  # the API key to the request

        option_list = "exclude=currently,minutely,hourly,alerts&amp;units=si,lang=hu"  # TODO: Units and language not work

        newdate = f"{date[:4]}-{date[5:7]}-{date[8::]}T00:00:00"

        adress = coordinates
        req = f"https://api.darksky.net/forecast/{DSAPI_KEY}/{adress[0]},{adress[1]},{newdate}?{option_list}"

        # requests.get("https://api.darksky.net/forecast/"+DARK_SKY_API_KEY+"/"+latitude+","+longitude+","+search_date+"?"+option_list)

        response = requests.get(req)
        json_res = response.json()
        return json_res


def F_To_C(temp):

    x = (temp-32)*5/9
    return x//1

def timezone(json_res):

    x = f'Timezone: {json_res["timezone"]}'
    return x

def min_temp(json_res):
    min_celsius = F_To_C(int(json_res['daily']['data'][0]['apparentTemperatureMin']))
    unit_type = '°F' if json_res['flags']['units'] == 'us' else '°C'
    min_t = "Min temperature: "+str(min_celsius)+'°C'
    return min_t


def max_temp(json_res):
    unit_type = '°F' if json_res['flags']['units'] == 'us' else '°C'
    max_celsius = F_To_C(int(json_res['daily']['data'][0]['apparentTemperatureMax']))
    max_t = "Max temperature: "+str(max_celsius)+'°C'
    return max_t


def summary(json_res):

    sumary = "Summary: " + json_res['daily']['data'][0]['summary']
    return sumary


def precip(json_res):
    precip_type = None
    precip_prob = None

    if'precipProbability' in json_res['daily']['data'][0] and 'precipType' in json_res['daily']['data'][0]:
        precip_type = json_res['daily']['data'][0]['precipType']
        precip_prob = json_res['daily']['data'][0]['precipProbability']

    if precip_type == 'rain' and precip_prob != None:
        precip_prob *= 100
        rain = "Chance of rain: %.0f%%" % (precip_prob)
        return rain


def weather_icon(json_res):
    icon_list = ["clear-day",
                 "clear-night",
                 "partly-cloudy-day",
                 "partly-cloudy-night",
                 "cloudy",
                 "rain",
                 "sleet",
                 "snow",
                 "wind",
                 "fog"
                 ]
    icon = ""
    for i in icon_list:
        if json_res['daily']['data'][0]['icon'] ==i:
            icon = i+".gif"

    return icon

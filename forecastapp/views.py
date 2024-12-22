from django.shortcuts import render , HttpResponse
import requests
# from django.views.generic import TemplateView

# # Create your views here.
# class Forecast(TemplateView):
#     template_name='index.html'

def index(request):
    city=request.GET.get('city')
    api_key='1bbb554ed12ee010f5cd79333485ad71'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response=requests.get(url)
    print(response)
    data=response.json()
    print(data)
    city=data['name']
    humidity=data['main']['humidity']
    windspeed=data['wind']['speed']
    tempr=data['main']['temp']
    tempr=tempr-273
    tempr=round(tempr,2)
    image=data['weather'][0]['icon']
    return render(request, 'index.html',{'city':city,'humidity':humidity,'windspeed':windspeed,'tempr':tempr,'image':image})
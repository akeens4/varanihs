from django.shortcuts import render
from django.http import HttpResponse
import requests

#Create your views here.
def index(request):
    print(request.POST)
    return render(request, 'index.html', {})

def contact(request):

        return render(request, 'contact.html', {})
    

def summary(request):
    API_key = "7f61950c7fcd41bb39210a7a11a12180"
    input_link = request.POST['input_list']
    input_number = request.POST['input_number']
    input_type = request.POST['input_type']

    #API_response = 0;
    if input_type == 'url':
        API_response = requests.get('https://api.meaningcloud.com/summarization-1.0?'
        + 'key=' + API_key + '&url=' + input_link
        + '&sentences=' + input_number)
    
    elif input_type == 'text':
        API_response = requests.get('https://api.meaningcloud.com/summarization-1.0?'
        + 'key=' + API_key + '&txt=' + input_link
        + '&sentences=' + input_number)
    elif input_type == 'doc':
        API_response = requests.get('https://api.meaningcloud.com/summarization-1.0?'
        + 'key=' + API_key + '&doc=' + input_link
        + '&sentences=' + input_number)

    return render(request, 'summary.html', {
        
        'summary': API_response.json(),
        
    })

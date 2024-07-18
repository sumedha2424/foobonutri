from django.shortcuts import render
import requests
#LFUaHRJxpcnA9YkFFaUMWg==oN7P5uSc2u3TbapZ

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    import json
    import requests
    from django.shortcuts import render
    if request.method == 'POST': 
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'LFUaHRJxpcnA9YkFFaUMWg==oN7P5uSc2u3TbapZ'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)

        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html',{'api': api})

    else:
        return render(request, 'home.html',{'query':'Enter a valid query'})


from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view 
from coinpaprika import client as Coinpaprika
import pandas as pd

# Create your views here.

@api_view(['GET'])
def home(request):

    return HttpResponse("Jai Shree Ram !!")

@api_view(['GET','POST'])
def dashboard(request):
    client = Coinpaprika.Client()

    if request.method == 'POST':
        f = request.POST
        print(f)
        instrument = f['instrument'] 
        print(instrument)
        if instrument in ('coins', 'exchange_list', 'global_market','tickers'):
            df = pd.DataFrame(getattr(client,instrument)())[0:5]
        
        context= {
            'df':df}
       
        return render(request, 'dashboard.html', context)

    return render(request, 'dashboard.html')

    
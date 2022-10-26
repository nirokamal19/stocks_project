from textwrap import indent
from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        #pk_e76e2a219440436ca382464a034431e3 - iexapis
        # RR3F5ESQ28BTNHUG - alphavantage
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +"/quote?token=pk_e76e2a219440436ca382464a034431e3")
        # api_request2 = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + ticker +"&apikey=RR3F5ESQ28BTNHUG")

        try:
            api = json.loads(api_request.content)
            # api2 = json.loads(api_request2.content)
        except Exception as e:
            api = "Error"
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})


def about(request):
    return render(request, 'about.html', {})

    
def portfolio(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added"))
            return redirect('portfolio')
    else:
        ticker = Stock.objects.all()
        output = []

        for ticker_item in ticker:
            # api_request = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + str(ticker) +"&apikey=RR3F5ESQ28BTNHUG")
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) +"/quote?token=pk_e76e2a219440436ca382464a034431e3")
            try:
                api = json.loads(api_request.content)
                output.append(api)

            except Exception as e:
                api = "Error"
        return render(request, 'portfolio.html', {'ticker': ticker, 'output':output})


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted"))
    return redirect(portfolio)





    
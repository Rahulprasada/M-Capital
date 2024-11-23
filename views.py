from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
import requests 
from .models import stock

# Example of another view
# Create your views here.

def user_login(request):  # Renamed the login view function to avoid conflict
    return render(request, 'login.html')

def start(request):
    starts = stock.objects.all()
    return render(request, 'index.html',{'starts':starts})

def calcis(request):
    return render(request, 'calculation.html')

def nserec(request):
    return render(request, 'nse.html')

def swp_(request):
    return render(request, 'SWP.html')

def invest(request):
    return render(request, 'investlog.html')

def signup(request):
    return render(request, 'signup.html')

def homes(request):
    return render(request, 'home.html')

def mfs(request):
    return render(request,'mf.html')

def get_stock_data(request):
    stock_symbol = request.GET.get('stock_symbol', '').upper()  # Convert stock symbol to uppercase
    from_date_str = request.GET.get('from_date')
    to_date_str = request.GET.get('to_date')

    if not stock_symbol:
        return JsonResponse({'success': False, 'message': 'Stock symbol is required'})

    # Convert from_date and to_date to datetime objects if they exist
    from_date = None
    to_date = None
    
    if from_date_str:
        try:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid from_date format. Use YYYY-MM-DD.'})
    
    if to_date_str:
        try:
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d')
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid to_date format. Use YYYY-MM-DD.'})

    # API Key and URL
    api_key = 'bc1SXQFdHuNkiU79vEEnPfktcSSxXGph'  # Replace with your actual API key
    api_url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{stock_symbol}?apikey={api_key}'

    try:
        # Fetch stock data
        response = requests.get(api_url)
        if response.status_code != 200:
            return JsonResponse({'success': False, 'message': 'Error fetching data from API.'})

        data = response.json()
        historical_data = data.get('historical', [])
        if not historical_data:
            return JsonResponse({'success': False, 'message': 'No historical data found for the stock.'})

        # Filter data by date range
        filtered_data = []
        for entry in historical_data:
            entry_date = datetime.strptime(entry['date'], '%Y-%m-%d')

            # Apply date range filter
            if from_date and entry_date > from_date:
                continue
            if to_date and entry_date < to_date:
                continue 

            filtered_data.append({
                'Symbol': stock_symbol,  # Add the symbol as a constant
                'Date': entry.get('date', 'N/A'),
                'Open': entry.get('open', 'N/A'),
                'High': entry.get('high', 'N/A'),
                'Low': entry.get('low', 'N/A'),
                'Close': entry.get('close', 'N/A'),
                'Adj Close': entry.get('adjClose', 'N/A'),
                'Volume': entry.get('volume', 'N/A'),
                'Unadjusted Volume': 'N/A',  # Placeholder if data is not available from API
                'Change': 'N/A',  # Placeholder for change in stock value
                'Change Percent': 'N/A',  # Placeholder for change percent
                'Vwap': 'N/A',  # Placeholder for VWAP
                'Label': 'N/A',  # Placeholder for any additional label
                'Change Over Time': 'N/A',  # Placeholder for change over time
            })

        return JsonResponse({'success': True, 'stock_data': filtered_data})

    except requests.exceptions.RequestException as e:
        return JsonResponse({'success': False, 'message': f'Error occurred: {str(e)}'})


    
def ssys(requests):
    return render(requests,'sy.html')

def graph(request):
    return render(request,'graph.html')

def epfs(request):
    return render(request,'epf.html')

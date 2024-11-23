from django.http import JsonResponse 
from datetime import datetime
import requests
def get_stock_data(request):
    stock_symbol = request.GET.get('stock_symbol','').upper()
    from_date_str = request.GET.get('from_date')
    to_date_str = request.GET.get('to_date')
    
    if not stock_symbol:
        return JsonResponse({'success' : False , 'message':'Stock Symbol is required'})
    
    
    from_date = None
    to_date = None
    
    if from_date_str:
        try:
            from_date = datetime.strptime(from_date,'%y-%m-%d')
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid from_date format. YYYY-MM-DD.'})
        
    if to_date_str:
        try:
            to_date = datetime.strptime(to_date,'%y-%m-%d')
        except ValueError:
            return JsonResponse({'Success':False , 'message':'Inavali to_date Formate. use YYYY-MM-DD.'})
        
    api_key = 'apikey'
    api_url = 'api_url'
    
    try:
        data1 = requests.get(api_url)
        if data1.status_code != 200:
            return JsonResponse({'success': False , 'message': 'error fetching data from api'})
        
        data2 = data1.json()
        data3 = data2.get('historical',[]) 
        if not data3:
            return JsonResponse({'success': False , 'message':'not workinh' })
        
        filtered_date = []
        for take in data3:
            entry_date = datetime.strptime(take['date'],'%y-%m-%d')
            
            if from_date and entry_date < from_date:
                continue
            if to_date and entry_date > to_date:
                continue
        
            
            
        
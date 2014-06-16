from django.shortcuts import render
from quotes.models import Quote

def home(request):
    recent_quote = Quote.objects.all().order_by('created_on')[0]
    context = {'recent_quote': recent_quote}
    return render(request, 'index.html', context)

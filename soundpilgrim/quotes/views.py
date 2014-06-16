from django.shortcuts import render
from quotes.models import Quote

def quotes(request):
    recent_quotes = Quote.objects.all().order_by('created_on')[:20]
    context = {'recent_quotes': recent_quotes}
    return render(request, 'quotes/base_quote.html', context)


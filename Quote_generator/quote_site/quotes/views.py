from django.shortcuts import render, redirect
from .models import Quote
import random
from .forms import QuoteForm
# Create your views here.

def random_quotes(request):
    quote = Quote.objects.order_by('?').first() # Random quote
    return render(request, 'quotes/home.html',{'quote': quote})


def submit_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') #After submission,redirect to the home
        else:
            form = QuoteForm()
        return render(request,'quotes/submit.html', {'form': form})
    
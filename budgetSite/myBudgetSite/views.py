from django.shortcuts import render

# Create your views here.
def bill_list(request):
    return render(request, 'myBudgetSite/bill_list.html', {})
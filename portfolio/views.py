from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum

#from easy_pdf.views import PDFTemplateResponseMixin
#from django.views.generic import DetailView
#from easy_pdf.views import PDFTemplateResponseMixin
#from django.views.generic import DetailView

from django.shortcuts import render, redirect
from .utils import render_to_pdf
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse


now = timezone.now()
def home(request):
   return render(request, 'portfolio/home.html',
                 {'portfolio': home})

@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/customer_list.html',
                 {'customers': customer})

@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/customer_list.html',
                         {'customers': customer})
   else:
        # edit
       form = CustomerForm(instance=customer)
   return render(request, 'portfolio/customer_edit.html', {'form': form})

@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('portfolio:customer_list')

@login_required
def stock_list(request):
   stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/stock_list.html', {'stocks': stocks})



@login_required
def stock_new(request):
   if request.method == "POST":
       form = StockForm(request.POST)
       if form.is_valid():
           stock = form.save(commit=False)
           stock.created_date = timezone.now()
           stock.save()
           stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/stock_list.html',
                         {'stocks': stocks})
   else:
       form = StockForm()
       # print("Else")
   return render(request, 'portfolio/stock_new.html', {'form': form})



@login_required
def stock_edit(request, pk):
   stock = get_object_or_404(Stock, pk=pk)
   if request.method == "POST":
       form = StockForm(request.POST, instance=stock)
       if form.is_valid():
           stock = form.save()
           # stock.customer = stock.id
           stock.updated_date = timezone.now()
           stock.save()
           stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/stock_list.html', {'stocks': stocks})
   else:
       # print("else")
       form = StockForm(instance=stock)
   return render(request, 'portfolio/stock_edit.html', {'form': form})

@login_required
def stock_delete(request, pk):
   stock = get_object_or_404(Stock, pk=pk)
   stock.delete()
   stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/stock_list.html', {'stocks': stocks})

@login_required
def investment_list(request):
    investments = Investment.objects.filter(recent_date__lte=timezone.now())
    return render(request, 'portfolio/investment_list.html', {'investments': investments})

@login_required
def investment_list(request):
   investments = Investment.objects.filter(acquired_date__lte=timezone.now())
   return render(request, 'portfolio/investment_list.html', {'investments': investments})


@login_required
def investment_new(request):
   if request.method == "POST":
       form = InvestmentForm(request.POST)
       if form.is_valid():
           investment = form.save(commit=False)
           investment.created_date = timezone.now()
           investment.save()
           investments = Investment.objects.filter(acquired_date__lte=timezone.now())
           return render(request, 'portfolio/investment_list.html',
                         {'investments': investments})
   else:
       form = InvestmentForm()
       # print("Else")
   return render(request, 'portfolio/investment_new.html', {'form': form})


@login_required
def investment_edit(request, pk):
   investment = get_object_or_404(Investment, pk=pk)
   if request.method == "POST":
       form = InvestmentForm(request.POST, instance=investment)
       if form.is_valid():
           investment = form.save()
           # investment.customer = investment.id
           investment.updated_date = timezone.now()
           investment.save()
           investments = Investment.objects.filter(acquired_date__lte=timezone.now())
           return render(request, 'portfolio/investment_list.html', {'investments': investments})
   else:
       # print("else")
       form = InvestmentForm(instance=investment)
   return render(request, 'portfolio/investment_edit.html', {'form': form})




@login_required
def investment_delete(request, pk):
   investment = get_object_or_404(Investment, pk=pk)
   investment.delete()
   investments = Investment.objects.filter(acquired_date__lte=timezone.now())
   return render(request, 'portfolio/investment_list.html', {'investments': investments})




@login_required
def portfolio(request,pk):
   customer = get_object_or_404(Customer, pk=pk)
   customers = Customer.objects.filter(created_date__lte=timezone.now())
   investments =Investment.objects.filter(customer=pk)
   stocks = Stock.objects.filter(customer=pk)
   mutuals = Mutual.objects.filter (customer=pk)
   sum_recent_value = Investment.objects.filter(customer=pk).aggregate(Sum('recent_value'))
   sum_acquired_value = Investment.objects.filter(customer=pk).aggregate(Sum('acquired_value'))
   #overall_investment_results = sum_recent_value-sum_acquired_value

   # Initialize the value of the stocks
   sum_current_stocks_value = 0
   sum_of_initial_stock_value = 0
   sum_current_mutual_value = 0
   sum_of_initial_mutual_value = 0

   # Loop through each stock and add the value to the total
   for stock in stocks:
        sum_current_stocks_value += stock.current_stock_value()
        sum_of_initial_stock_value += stock.initial_stock_value()

   for mutual in mutuals:
       sum_current_mutual_value += mutual.current_mutual_value ()
       sum_of_initial_mutual_value += mutual.initial_mutual_value ()

   return render(request, 'portfolio/portfolio.html', {'customers': customers,
                                                       'investments': investments,
                                                       'stocks': stocks,
                                                       'mutuals':mutuals,
                                                       'sum_acquired_value': sum_acquired_value,
                                                       'sum_recent_value': sum_recent_value,
                                                        'sum_current_stocks_value': sum_current_stocks_value,
                                                        'sum_of_initial_stock_value': sum_of_initial_stock_value,
                                                       'sum_current_mutual_value':sum_current_mutual_value,
                                                       'sum_of_initial_mutual_value':sum_of_initial_mutual_value,

                                                       })

   # Initialize the value of the stocks
   #total_initial_investments = 0
   #total_current_investments = 0

   # Loop through each investment and add the value to the total
   #for investment in investments:
   #     total_initial_investments += investment.acquired_value()
   #     total_current_investments += investment.recent_value()


   #return render(request, 'portfolio/portfolio.html', {'customers': customers,
   #                                                    'investments': investments,
   #                                                    'stocks': stocks,
   #                                                    'sum_acquired_value': sum_acquired_value,
   #                                                    'sum_recent_value': sum_recent_value,
   #                                                     'sum_current_stocks_value': sum_current_stocks_value,
   #                                                     'sum_of_initial_stock_value': sum_of_initial_stock_value,
   #                                                    'total_current_investments':total_current_investments,
   #                                                    'total_initial_investments':total_initial_investments
   #                                                    })






#class pdfDetail(PDFTemplateResponseMixin,DetailView):
#    template_name = 'pdf_detail.html'
#    context_object_name='investment'
#    model= Investment

def genrate_investment_pdf(request,pk):
    investments_pdf = Investment.objects.filter(investment=pk)
    context = { 'investments': investments_pdf }
    pdf = render_to_pdf('portfolio/pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['content-Disposition'] = 'filename = "investments_{}.pdf"'
        return pdf
    return HttpResponse("Not Found")

@login_required
def investments_download(request):
    investments = Investment.objects.filter()
    data = 'customer, category, description, acquired_value, acquired_date, recent_value,recent_date\n'
    for investment in investments:
        data += '%s,%s,%s,%s\n' % (investments.customer, investments.category, investments.description,
                                   investments.acquired_value, investments.recent_value, investments.recent_date)

    response = HttpResponse(data)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="investments.csv"'

    return response

@login_required
def mutual_list(request):
   mutuals = Mutual.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/mutual_list.html', {'mutuals': mutuals})


@login_required
def mutual_new(request):
   if request.method == "POST":
       form = MutualForm(request.POST)
       if form.is_valid():
           mutual = form.save(commit=False)
           mutual.created_date = timezone.now()
           mutual.save()
           mutuals = Mutual.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/mutual_list.html',
                         {'mutuals': mutuals})
   else:
       form = MutualForm()
       # print("Else")
   return render(request, 'portfolio/mutual_new.html', {'form': form})



@login_required
def mutual_edit(request, pk):
    mutual = get_object_or_404(Mutual, pk=pk)
    if request.method == "POST":
        form = MutualForm(request.POST, instance=mutual)
        if form.is_valid():
            mutual = form.save()
            # mutual.customer = mutual.id
            mutual.updated_date = timezone.now()
            mutual.save()
            mutuals = Mutual.objects.filter(purchase_date__lte=timezone.now())
            return render(request, 'portfolio/mutual_list.html', {'mutuals': mutuals})
    else:
       # print("else")
       form = MutualForm(instance=mutual)
       return render(request, 'portfolio/mutual_edit.html', {'form': form})

@login_required
def mutual_delete(request, pk):
    mutual = get_object_or_404(Mutual, pk=pk)
    mutual.delete()
    mutuals = Mutual.objects.filter(purchase_date__lte=timezone.now())
    return render(request, 'portfolio/mutual_list.html', {'mutuals': mutuals})
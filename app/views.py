from django.shortcuts import render , get_object_or_404
from .models import Product , Costumer , Payment 
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# def myview(request):
    
#     return HttpResponse(
#         request.GET.get('q', 'Please enter q')
#     )

# def myview(request):
#     if request.method == 'POST':
#         if 'pk' in request.POST:
#             Product.objects.get(pk=request.POST.get('pk')).delete()
#         else:
#             Product.objects.create(
#                 name=request.POST.get('name'),
#                 price=request.POST.get('price')
#             )
    
#     return render(request, 'myhtml.html', {
#         'time': '18:00',
#         'products': Product.objects.all()

#     })

class MyView(TemplateView):
    template_name = 'product.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] =  Product.objects.all()
        return context


    def post(self, request):
        if 'pk' in request.POST:
            Product.objects.get(pk=request.POST.get('pk')).delete()
        else:
            Product.objects.create(
                name=request.POST.get('Pname'),
                price=request.POST.get('price'),
                brand=request.POST.get('brand'),
                PR_id=request.POST.get('PR_id'),

            )
        return self.get(request)

class MyView4(TemplateView):
    template_name = 'cart.html'
    
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] =  Product.objects.all()
        context['Product'] = Product.Total
        context['Costumers'] = Costumer.objects.all()
        return context


    def post(self, request):
        if 'pk' in request.POST:
            amn = Product.objects.get(pk=request.POST.get('pk')) 
            amn.PR_number = amn.PR_number + 1
            amn.save()
            Product.Total = Product.Total + amn.price

        if 'pj' in request.POST:
            
           anm = Product.objects.get(pk=request.POST.get('pj')) 
           if anm.PR_number > 0 :
                anm.PR_number = anm.PR_number - 1
                anm.save()
                Product.Total = Product.Total - anm.price
        
        if 'addd' in request.POST:
            
            Payment.objects.create(
                buyer=request.POST.get('buyer'),
                amount=Product.Total,
                PA_type="cash",
                
             )
            Product.Total = 0
            Product.objects.update(PR_number=0)


        if 'clear' in request.POST:
        
            Product.Total = 0
            
            Product.objects.update(PR_number=0)
                

           

        
        return self.get(request)

class Costumerr(TemplateView):
    template_name = 'Costumers.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['costumers'] =  Costumer.objects.all()
        return context


    def post(self, request):
        if 'plk' in request.POST:
            Costumer.objects.get(pk=request.POST.get('plk')).delete()

        
        else:
            Costumer.objects.create(
                Cname=request.POST.get('Cname'),
                email=request.POST.get('email'),
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                
            )
        return self.get(request)

class Paymentt(TemplateView):
    template_name = 'Payment.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['payments'] =  Payment.objects.all()
        return context


    def post(self, request):
        if 'pkk' in request.POST:
            Payment.objects.get(pk=request.POST.get('pkk')).delete()
        else:
            Payment.objects.create(
                buyer=request.POST.get('buyer'),
                amount=request.POST.get('amount'),
                PA_type=request.POST.get('PA_type'),
                
            )
        return self.get(request)

class MyView2(View):
    def get(self, request, code):
        return HttpResponse(str(request.user))

class Homee(TemplateView):
    template_name = 'home.html'

class SignUp(TemplateView):
    template_name = 'signupp.html'


    # def post(self, request):
    #     if 'pk' in request.POST:
    #         Product.objects.get(pk=request.POST.get('pk')).delete()
    #     else:
    #         User.objects.create(
    #             name=request.POST.get('name'),
    #             Email=request.POST.get('Email')
    #             psw=request.POST.get('psw')
    #             pswrepeat=request.POST.get('pswrepeat')
    #         )
    #     return self.get(request)

    
  

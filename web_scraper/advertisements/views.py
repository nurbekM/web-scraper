from django.shortcuts import render
from django.views import View
from advertisements.models import Phone
import os

class HomePage(View):

    def get(self, request):
        return render(request, 'advertisements/index.html')

    def post(self, request):
        phone_name = request.POST['phone_name'].split()

        if  len(phone_name) >= 2:
            phone_list = [Phone.objects.filter(shop_name=shop).filter(name__icontains=phone_name[0]).filter(
                name__icontains=phone_name[1]).order_by('price')[:1] for shop in ['Technodom', 'sulpak', 'kaspi', 'mechta', 'alser']]
        else:
            phone_list = [Phone.objects.filter(shop_name=shop).filter(name__icontains=phone_name[0]).order_by(
                'price')[:1] for shop in ['Technodom', 'sulpak', 'kaspi', 'mechta', 'alser']]

        print(phone_list)
        return render(request, 'advertisements/search_result.html', {'phone_list': phone_list})


class About(View):

    def get(self, request):
        return render(request, 'advertisements/about.html')

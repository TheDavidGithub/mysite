from django.template.context_processors import csrf
from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse
from models import Car
import copy
import os

def show_default(request,offset):
    page = int(offset)
    if page >= 0:
        return show(request,'city=/brand=/types=/time=/mileage=/price=/page='+offset)
    else:
        return show(request,'city=/brand=/types=/time=/mileage=/price=/page=1')

def show_max(request):
    return show(request,'city=/brand=/types=/time=/mileage=/price=/page=1')

def show(request,offset):
    search_list = offset.split('/')
    select = {}
    have_search = False
    for search in search_list:
        if search.split('=')[0] == 'page':
            page_num = int(search.split('=')[1])
        else:
            if search.split('=')[1]:
                have_search = True
            select[search.split('=')[0]] = [search.split('=')[1]]

    car_list = Car.objects.all()
    if select["city"][0]:
        car_list = car_list.filter(city=select["city"][0])
    if select["brand"][0]:
        car_list = car_list.filter(brand=select["brand"][0])
    if select["types"][0]:
        car_list = car_list.filter(types=select["types"][0])
    if select["time"][0]:
        car_list = car_list.filter(car_time=select["time"][0].replace('-','/'))
    if select["mileage"][0]:
        car_list = car_list.filter(mileage=select["mileage"][0])
    if select["price"][0]:
        car_list = car_list.filter(car_price=select["price"][0])

    city_list = car_list.values('city').distinct().order_by('city')
    citys = []
    for city in city_list:
        citys.append(city['city'])
    brand_list = car_list.values('brand').distinct().order_by('brand')
    brands = []
    for brand in brand_list:
        brands.append(brand['brand'])
    types_list = car_list.values('types').distinct().order_by('types')
    typess = []
    for types in types_list:
        typess.append(types['types'])
    car_time_list = car_list.values('car_time').distinct().order_by('car_time')
    car_times = []
    for car_time in car_time_list:
        car_times.append(car_time['car_time'].replace('/','-'))
    mileage_list = car_list.values('mileage').distinct().order_by('mileage')
    mileages = []
    for mileage in mileage_list:
        mileages.append(mileage['mileage'])
    car_price_list = car_list.values('car_price').distinct().order_by('car_price')
    car_prices = []
    for car_price in car_price_list:
        car_prices.append(car_price['car_price'])

    select["city"].append(u'\u57ce\u5e02')
    select["brand"].append(u'\u54c1\u724c')
    select["types"].append(u'\u8f66\u578b')
    select["time"].append(u'\u4e0a\u724c\u65f6\u95f4')
    select["mileage"].append(u'\u884c\u9a76\u91cc\u7a0b')
    select["price"].append(u'\u4ef7\u683c')
    select["city"].append(citys)
    select["brand"].append(brands)
    select["types"].append(typess)
    select["time"].append(car_times)
    select["mileage"].append(mileages)
    select["price"].append(car_prices)

    sorted_select = []
    sorted_select.append(["city",select["city"]])
    sorted_select.append(["brand",select["brand"]])
    sorted_select.append(["types",select["types"]])
    sorted_select.append(["time",select["time"]])
    sorted_select.append(["mileage",select["mileage"]])
    sorted_select.append(["price",select["price"]])

    if len(car_list) > 0 and len(car_list) % 20 == 0:
        total_page = len(car_list)/20
    else:
        total_page = len(car_list)/20+1
    if page_num < 3:
        page_list = [1,2,3,4,5]
    else:
        if page_num > total_page - 2:
            if total_page > 4:
                page_list = [total_page-4,total_page-3,total_page-2,total_page-1,total_page]
            else:
                page_list = [1,2,3,4,5]
        else:
            page_list = [page_num-2,page_num-1,page_num,page_num+1,page_num+2]

    if page_num == 0:
        car_list = []
    else:
        car_list = car_list[(page_num-1)*20:page_num*20]
    i = 0
    car_1 = []
    format_car_list = []
    for car in car_list:
        if i == 4:
            format_car_list.append(car_1)
            car_1 = []
            i = 0
        car_1.append(car)
        i = i + 1
    format_car_list.append(car_1)
    fp = open(os.path.join(os.path.dirname(__file__), 'list.html').replace('\\','/'))
    page = fp.read()
    fp.close()

    t = Template(page)
    c = Context(
        {
            'select': select,
            'sorted_select': sorted_select,
            'have_search': have_search,
            'car_list': format_car_list,
            'page_num': page_num,
            'total_page': total_page,
            'last_page': page_num - 1,
            'next_page': page_num + 1,
            'page_list': page_list
        }
    )
    c.update(csrf(request))
    return HttpResponse(t.render(c))
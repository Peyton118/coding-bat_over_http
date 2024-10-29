from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.

def Hey_You(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse('Hey, ' + name + '!')

def Age_In(request, end: int, birthyear: int):
    return HttpResponse(end - birthyear)

def Order_In(request, burgers, fries, drinks):
    # Burgers are $4.50. Fries are $1.5. Drinks are $1.
    burger_price = 4.50 * burgers
    fries_price = 1.50 * fries
    drinks_price = 1.00 * drinks

    total = burger_price + fries_price + drinks_price

    return HttpResponse(f'{total:.2f}')
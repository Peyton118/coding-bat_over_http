from django.contrib import admin
from django.urls import path
from app.views import Hey_You, Age_In, Order_In

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hey/<name>", Hey_You),
    path("age-in/<int:end>/<int:birthyear>", Age_In),
    path("order-total/<int:burgers>/<int:fries>/<int:drinks>", Order_In)
]

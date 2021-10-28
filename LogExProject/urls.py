
from django.contrib import admin
from django.urls import path, include

from LogExAPP.views import home, get_started, learn, instant_buy, dashboard, individual, business, base
from accounts.views import login
# from accounts.views import login, logout, register, dashbaord


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('getstarted/', get_started, name='getstarted'),
    path('login/', login, name='login'),
    path('learn/', learn, name='learn'),
    path('instantbuy/', instant_buy, name='instantbuy'),
    path('dashboard/', dashboard, name='dashboard'),
    path('individual/', individual, name='individual'),
    path('business/', business, name='business'), 
    path('accounts/', include('accounts.url')),
    path('base/', base, name='base'),
]
 
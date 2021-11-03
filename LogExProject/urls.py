
from django.contrib import admin
from django.urls import path, include

from LogExAPP.views import index, learn, instant_buy, dashboard, individual, business, welcome
from accounts.views import login, register
# from accounts.views import login, logout, register, dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('getstarted/', get_started, name='getstarted'),

    # path('login/', login, name='login'),
    # path('register/', register, name='register'), 

    path('learn/', learn, name='learn'),
    path('instantbuy/', instant_buy, name='instantbuy'),
    path('dashboard/', dashboard, name='dashboard'),
    path('individual/', individual, name='individual'),
    path('business/', business, name='business'), 
    path('welcome/', welcome, name='welcome'),
    path('accounts/', include('accounts.urls'))
    # path('base/', base, name='base'),
]
 
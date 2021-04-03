"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from holy.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HOME ,name='home'),
    path('add_cart/', Add_cart ,name='add_cart'),
    path('cart/', Show_cart ,name='cart'),
    path('pluscart/', plus_cart ),
    path('minuscart/', minus_cart ),
    path('removecart/', remove_cart ),
    path('orderd/', Orderd,name='orderd'),
    path('about/', ABT ,name='abt'),
    path('login/', LOGIN ,name='log'),
    path('shop1/<int:c_id>/', SHOP1 ,name='shop11'),
    path('shop/', SHOP ,name='shp'),
    path('check/',CHECK,name='chk'),
    path('confirm/',confirmation,name='cnfrm'),
    path('contact/',CONTACT,name='cont'),
    path('element/',ELEMENT,name='elmnt'),
    path('<int:pr_id>/',PRODET,name = 'pd'),
    path('sign/',SINGUP,name='sign'),
    path('Logout/',LOGOUT,name='Logout'),
    path('myorder/',My_order,name='myorder')
    # path('search/',search,name='search'),
    

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
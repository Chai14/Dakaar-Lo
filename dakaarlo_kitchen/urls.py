from django.contrib import admin
from django.urls import path
from dakaarlo_kitchen import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('menu/', views.menu, name="menu"),
    path('chinese/', views.chinese, name="chinese"),
    path('italian/', views.italian, name="italian"),
    path('street/', views.indianstreet, name="street"),
    path('north/', views.northindian, name="north"),
    path('south/', views.southindian, name="south"),
    path('gujraj/', views.gujraj, name="gujraj"),
    path('custom/', views.custom, name="custom"),
    path('signup/', views.signup, name="signup"),
    path('custom2/', views.custom, name="custom"),
    path('about/', views.about, name="about"),
    path('cuscare/', views.customercare, name="customercare"),
    path('cart/', views.cart, name="cart"),
    path('member/', views.memberships, name="memberships"),
    path('offer/', views.offers, name="offers"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
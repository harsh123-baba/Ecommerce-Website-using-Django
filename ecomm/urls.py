
from django.contrib import admin
from django.urls import path, include
from shop import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', 'shop')),
    path('about/', include('shop.urls' , 'shop')),
    # path('accounts/', include('accounts.urls',namespace='accounts')), 
    # path('login/' ,include('accounts.urls', namespace='accounts')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('shop.urls' , 'shop')),
    path('prodview/', include('shop.urls', 'shop')),
    path('update_item/', include('shop.urls', 'shop')),
    path('cart/', include('shop.urls', 'shop')),
    path('checkout/', include('shop.urls', 'shop')),    
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)



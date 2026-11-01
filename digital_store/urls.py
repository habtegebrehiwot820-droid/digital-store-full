from django.contrib import admin
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_store, name='home'),
    path('buy/<int:product_id>/', views.initialize_payment, name='buy_product'),
    path('download/<int:product_id>/', views.download_product_file, name='download_product'), # The secure delivery link
]

# This allows Django to locate your uploaded files while you are coding locally
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

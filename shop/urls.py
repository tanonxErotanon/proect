from django.contrib import admin
from django.urls import path
from catalog.views import product_list, product_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", product_list, name="product_list"),  
    path("product/<int:product_id>/", product_detail, name="product_detail"),  
]


# добавление путей медиа файлов 
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
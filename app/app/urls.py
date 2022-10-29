from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from webapp.views import IndexView, ProductView, ProductCreate, ProductDelete, ProductUpdate, ReviewCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/product/<int:pk>', ProductView.as_view(), name='product_view'),
    path('products/create', ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('review/create/', ReviewCreate.as_view(), name='review_create'),

    path("accounts/", include('accounts.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

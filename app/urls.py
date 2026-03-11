from django.urls import path
from app import views

urlpatterns = [
    #    path('admin/', admin.site.urls),
    #path('hello', views.hello),
    path('product', views.product_count),
    path('product/nouveau', views.show_form),
    path('product/enregister', views.create_product),
    path('product/<pk>', views.product_detail)

]

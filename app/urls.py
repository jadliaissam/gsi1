from django.urls import path

from app import views

urlpatterns = [
    #    path('admin/', admin.site.urls),
    # path('hello', views.hello),
    path('form', views.show_contact_form),
    path('form2', views.handle_contact_form2),
    path('process_form', views.handle_contact_form),
    path('messages', views.list_messages),
    path('product', views.product_count),
    path('product/nouveau', views.show_form),
    path('product/enregister', views.create_product),
    path('product/<pk>', views.product_detail)

]

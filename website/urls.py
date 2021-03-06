from django.conf.urls import url

from django.urls import path

from . import views

from .views import product_details,product_delete_confirm, product_delete

from django.contrib.auth.decorators import login_required




app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'), 
    url(r'^process$', views.process_product, name='process'),
    url(r'^overview$',views.overview, name='overview'),
    url(r'^billing$', views.billing_status, name='billing_status'),
    url(r'^design$', views.design_status, name='design_status'),
    url(r'^cnc$', views.cnc_status, name='cnc_status'),
    url(r'^grinding$', views.grinding_status, name='grinding_status'),
    url(r'^painting$', views.painting_status, name='painting_status'),
    url(r'^packaging$', views.packaging_status, name='packaging_status'),
    url(r'^shipping$', views.shipping_status, name='shipping_status'),
    url(r'^test$', views.test, name='test'),
    path('details/<int:id>/<int:status_id>/', views.product_details, name='product_details'),
    path('send_to_design/<int:product_id>/', views.send_to_design, name='send_to_design'),
    path("product/search", views.product_search, name="product_search"),
    path("warning/<int:id>/<int:status_id>/", views.product_delete_confirm, name="product_delete_confirm"),
    path("delete/<int:product_id>/<int:status_id>/", views.product_delete, name="product_delete")
    ]
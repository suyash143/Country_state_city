from django.conf.urls import url
from django.urls import path
from app import views

urlpatterns = [
    path('country/',views.country_view,name='country_view'),

    path('country/<int:id>/state/',views.state_view,name='state_view'),
    path('country/<int:id>/state/<int:state_id>/',views.state_detail,name='state_detail'),
    path('state/<int:id>/city/',views.city_view,name='city_view'),
    path('state/<int:id>/city/<int:city_id>/',views.city_detail,name='city_detail')
]
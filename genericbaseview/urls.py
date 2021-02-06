from django.urls import path
from genericbaseview.views import *

urlpatterns = [
    path('save/', AddEmployee.as_view(),name='add'),
    path('<pk>/edit/', UpdateEmployee.as_view(),name='update'),
    path('<pk>/delete/', DeleteEmployee.as_view(),name='delete'),
    path('list/', FetchAllEmployee.as_view(),name='list'),
]

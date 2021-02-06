from django.urls import path
from classbaseview.views import *

urlpatterns = [
    path('save/', CrudEmployeeOps.as_view(),name="add"),
    path('<pk>/edit/', CrudEmployeeOps.as_view(),name='edit'),
    path('<pk>/delete/', CrudEmployeeOps.as_view(),name='delete'),
    path('list/', CrudEmployeeOps.as_view(),name='list'),
]
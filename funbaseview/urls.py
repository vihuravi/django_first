from django.urls import path
from funbaseview.views import *

urlpatterns = [
    path('emp/', welcome_page_emp),
    path('emp/save/', add_update_employee),
    path('emp/edit/<int:eid>', edit_employee),
    path('emp/delete/<int:eid>', delete_employee),
    path('adr/save/', add_update_address),
    path('adr/edit/<int:aid>', edit_address),
    path('adr/delete/<int:aid>', delete_address)
]
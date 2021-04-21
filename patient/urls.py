from django.urls import path
from .views import patient_create_view, patient_list_view,patient_detail_view,patient_delete_view,delete_suc

app_name="patient"
urlpatterns=[
    path('create/',patient_create_view),
    path('list/',patient_list_view),
    path('',patient_list_view),
    path('<int:id>/',patient_detail_view, name="patient-detail"),
    path('<int:id>/delete/',patient_delete_view),
]
from django.urls import path
from .views import delete_data, showdata, update_data
urlpatterns = [
    path('', showdata, name='show_data'),
    path('delete/<int:id>/',delete_data, name='delete_data'),
    path('<int:id>/', update_data, name='update_data')
]
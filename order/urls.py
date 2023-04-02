from django.urls import path

from .views import IndexView, CreateItemView, EditItemView

app_name = 'laundry'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create-item/', CreateItemView.as_view(), name='create_item'),
    path('edit-item/<int:pk>/', EditItemView.as_view(), name='edit_item'),
]
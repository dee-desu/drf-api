
from django.urls import path
from .views import DeeListView, DeeDetailView
urlpatterns = [
    path('', DeeListView.as_view(), name='dee_list'),
    path('<int:pk>', DeeDetailView.as_view(),name='dee_detail' )
    
]
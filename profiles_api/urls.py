from django.urls import path
from . import views
urlpatterns = [
    path('profiles_api_view/<int:pk>/',views.ProfilesApiView.as_view())
]

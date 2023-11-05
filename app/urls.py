from django.urls import path
from . import views


urlpatterns = [
	path("", views.list_blog, name="list_blog"),
	path("<int:pk>", views.detail_blog, name="detail_blog")
]

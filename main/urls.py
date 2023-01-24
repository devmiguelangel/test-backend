from django import urls
from django.urls import include, path

from main import views


urlpatterns = [
    path("categories/", views.CategoryAPIView.as_view()),
    path("products/", views.ProductAPIView.as_view()),
    path("products/<int:pk>/", views.ProductDetailAPIView.as_view()),
]

"""
urlpatterns = [
    path("products/", include("domains.rest.suppliers.v100.urls")),
]
"""

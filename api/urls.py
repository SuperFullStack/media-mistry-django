from django.urls import path
from .views import ProductTypesView, CountryView, QuantityView

urlpatterns = [
    path('product-types/', ProductTypesView.as_view()),
    path('country/', CountryView.as_view()),
    path('quantity/', QuantityView.as_view()),
]
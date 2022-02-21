from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Country, ProductType, Quantity, Product, Review
from .serializers import ProductTypeSerializer, CountrySerializer, QuantitySerializer


class ProductTypesView(APIView):
    def get(self, request, format=None):
        product_types = ProductType.objects.all()
        serializer = ProductTypeSerializer(product_types, many=True)
        return Response(serializer.data)

class CountryView(APIView):
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

class QuantityView(APIView):
    def get(self, request, format=None):
        quantities = Quantity.objects.all()
        serializer = QuantitySerializer(quantities, many=True)
        return Response(serializer.data)

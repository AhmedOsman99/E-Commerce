from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
from .signals import set_products_limit
from helper.crud import getAll, getById, addInstance, editInstance, deleteInstance
# Create your views here.


@api_view(['get'])
def list_products(request):
    data, http_status = getAll(Product, ProductSerializer)
    return Response(data=data, status=http_status)


@api_view(['get'])
def get_product(request, id):
    data, http_status = getById(id, Product, ProductSerializer)
    return Response(data=data, status=http_status)


@api_view(['post'])
def add_product(request):
    try:
        if set_products_limit(None, Category_id=request.data.get('Category')):
            data = {
                'Error': "Not Accepted, you can't add more than 5 products at category"}
            http_status = status.HTTP_400_BAD_REQUEST
        else:
            data, http_status = addInstance(
                request, Product, ProductSerializer)
    except Exception as e:
        data = {"Error": f"An error occurred => {e}"}
        http_status = status.HTTP_400_BAD_REQUEST

    return Response(data=data, status=http_status)


@api_view(['PUT'])
def edit_product(request, id):
    try:
        if set_products_limit(None, Category_id=request.data.get('Category')):
            data = {
                'Error': "Not Accepted, you can't add more than 5 products at category"}
            http_status = status.HTTP_400_BAD_REQUEST
        else:
            data, http_status = editInstance(
                request, id, Product, ProductSerializer)
    except Exception as e:
        data = {"Error": f"An error occurred => {e}"}
        http_status = status.HTTP_400_BAD_REQUEST

    return Response(data=data, status=http_status)


@api_view(['delete'])
def delete_product(request, id):
    data, http_status = deleteInstance(
        request, id, Product)
    return Response(data=data, status=http_status)


@api_view(['get'])
def list_categories(request):
    data, http_status = getAll(Category, CategorySerializer)
    return Response(data=data, status=http_status)


@api_view(['get'])
def get_category(request, id):
    data, http_status = getById(id, Category, CategorySerializer)
    return Response(data=data, status=http_status)


@api_view(['post'])
def add_category(request):
    data, http_status = addInstance(
        request, Category, CategorySerializer)
    return Response(data=data, status=http_status)    


@api_view(['PUT'])
def edit_category(request, id):
    data, http_status = editInstance(
        request, id, Category, CategorySerializer)
    return Response(data=data, status=http_status)


@api_view(['delete'])
def delete_category(request, id):
    data, http_status = deleteInstance(
        request, id, Category)
    return Response(data=data, status=http_status)

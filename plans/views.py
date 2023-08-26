from rest_framework.response import Response
from rest_framework import status
from .models import Plan, CustomPlan
from .serializers import PlanSerializer, CustomPlanSerializer
from rest_framework.decorators import api_view
from helper.crud import getAll, getById, addInstance, editInstance, deleteInstance
# Create your views here.

@api_view(['get'])
def list_plans(request):
    data, http_status = getAll(Plan, PlanSerializer)
    return Response(data=data, status=http_status)


@api_view(['get'])
def get_plan(request, id):
    data, http_status = getById(id, Plan, PlanSerializer)
    return Response(data=data, status=http_status)


@api_view(['post'])
def add_plan(request):
    data, http_status = addInstance(
        request, Plan, PlanSerializer)
    return Response(data=data, status=http_status) 


@api_view(['put'])
def edit_plan(request, id):
    data, http_status = editInstance(
        request, id, Plan, PlanSerializer)
    return Response(data=data, status=http_status)


@api_view(['delete'])
def delete_plan(request, id):
    data, http_status = deleteInstance(
        request, id, Plan)
    return Response(data=data, status=http_status)


@api_view(['get'])
def get_custom_plan(request):
    try:
        no_of_products = request.GET.get('products')
        storage = request.GET.get('storage')
        no_of_products = int(no_of_products)
        storage = int(storage)
        data = {"no_of_products":no_of_products, "storage": storage}
        model_serializer = CustomPlanSerializer(data=data, context={'request':request})
        if model_serializer.is_valid():
            price = model_serializer.calculate_price(no_of_products, storage)
            price = round(price, 2)
            data = {"price": price}
            http_status = status.HTTP_202_ACCEPTED
        else:
            data = model_serializer.errors
            http_status = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        data = {"Error": f"An error occurred => {e}"}
        http_status = status.HTTP_400_BAD_REQUEST
    return Response(data=data, status=http_status)


@api_view(['post'])
def add_custom_plan(request):
    data, http_status = addInstance(
        request, CustomPlan, CustomPlanSerializer)
    return Response(data=data, status=http_status)


@api_view(['put'])
def edit_custom_plan(request, id):
    data, http_status = editInstance(
        request, id, CustomPlan, CustomPlanSerializer)
    return Response(data=data, status=http_status)


@api_view(['delete'])
def delete_custom_plan(request, id):
    data, http_status = deleteInstance(
        request, id, CustomPlan)
    return Response(data=data, status=http_status)


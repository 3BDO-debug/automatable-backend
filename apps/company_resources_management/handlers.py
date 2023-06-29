from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Expenses, IncomeSource, Income
from .serializers import ProductSerializer, ExpensesSerializer, IncomeSourceSerializer, IncomeSerializer

# Products API
@api_view(['GET', 'POST', 'DELETE'])
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        products = Product.objects.all()
        products.delete()
        return Response({'message': 'All products deleted'}, status=204)

# Expenses API
@api_view(['GET', 'POST', 'DELETE'])
def expenses(request):
    if request.method == 'GET':
        expenses = Expenses.objects.all()
        serializer = ExpensesSerializer(expenses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ExpensesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        expenses = Expenses.objects.all()
        expenses.delete()
        return Response({'message': 'All expenses deleted'}, status=204)

# Income Sources API
@api_view(['GET', 'POST', 'DELETE'])
def income_sources(request):
    if request.method == 'GET':
        income_sources = IncomeSource.objects.all()
        serializer = IncomeSourceSerializer(income_sources, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IncomeSourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        income_sources = IncomeSource.objects.all()
        income_sources.delete()
        return Response({'message': 'All income sources deleted'}, status=204)

# Income API
@api_view(['GET', 'POST', 'DELETE'])
def income(request):
    if request.method == 'GET':
        income = Income.objects.all()
        serializer = IncomeSerializer(income, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        income = Income.objects.all()
        income.delete()
        return Response({'message': 'All income deleted'}, status=204)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models,serializers


class ExpensesHandler(APIView):
    def get(self, request):
        expenses = models.Expense.objects.all().order_by("-date_issued")
        expenses_serializer = serializers.ExpenseSerializer(expenses, many=True)

        return Response(status=status.HTTP_200_OK, data=expenses_serializer.data)

    def post(self, request):

        created_by = request.user
        price = float(request.data.get("amountDue"))
        paid_to = request.data.get("paidTo")
        invoice_description = request.data.get("invoiceDescription")


        models.Expense.objects.create(
            created_by=created_by,
            price=price,
            invoice_description=invoice_description,
            paid_to=paid_to
        ).save()

        return Response(status=status.HTTP_201_CREATED)
    

class IncomeSourcesHandler(APIView):
    def get(self, request):
        income_sources = models.IncomeSource.objects.all().order_by("-created_at")
        income_sources_serializer = serializers.IncomeSourceSerializer(income_sources, many=True)

        return Response(status=status.HTTP_200_OK, data=income_sources_serializer.data)


    def post(self, request):
        name = request.data.get("name")
        description = request.data.get("description")

        models.IncomeSource.objects.create(
            name=name,
            description=description
        ).save()


        return Response(status=status.HTTP_201_CREATED)


class EarningsHandler(APIView):
    def get(self, request):
        earnings = models.Earning.objects.all().order_by("-date_recieved")
        earnings_serializer = serializers.EarningSerializer(earnings, many=True)

        return Response(status=status.HTTP_200_OK, data=earnings_serializer.data)

    def post(self, request):
        
        created_by = request.user
        price = float(request.data.get("price"))
        income_source = models.IncomeSource.objects.get(id=int(request.data.get("incomeSource")["id"]))

        models.Earning.objects.create(
            created_by =created_by,
            price=price,
            income_source=income_source
        ).save()

        return Response(status=status.HTTP_200_OK)
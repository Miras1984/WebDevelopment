from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class show_companiesAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    permission_classes = (IsAuthenticated,)


class show_companyAPIView(APIView):
    def get_company(self, pk):
        try:
            company = Company.objects.get(id=pk)
            return company
        except Company.DoesNotExist as ex:
            return Response({'message': str(ex)}, status=400)

    def get(self, request, pk=None):
        company = self.get_company(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk=None):
        company = self.get_company(pk)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        company = self.get_company(pk)
        company.delete()
        return Response({'message': 'deleted'}, status=204)


class show_vacanciesAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class show_vacancyAPIView(APIView):
    def get_vacancy(self, pk):
        try:
            vacancy = Vacancy.objects.get(id=pk)
            return vacancy
        except Vacancy.DoesNotExist as ex:
            return Response({'message': str(ex)}, status=400)

    def get(self, request, pk=None):
        vacancy = self.get_vacancy(pk)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, pk=None):
        vacancy = self.get_vacancy(pk)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        vacancy = self.get_vacancy(pk)
        vacancy.delete()
        return Response({'message': 'deleted'}, status=204)


class show_vacancies_by_companyAPIView(APIView):
    def get(self, request, pk=None):
        try:
            vacancies = Vacancy.objects.filter(company_id=pk)
            serializer = VacancySerializer(vacancies, many=True)
        except Company.DoesNotExist as ex:
            return Response({'message': str(ex)}, status=400)

        return Response(serializer.data)

class top_tenAPIView(APIView):
    def get(self, request):
        try:
            vacancies = Vacancy.objects.all().order_by('-salary')
            serializer = VacancySerializer(vacancies, many=True)
        except Vacancy.DoesNotExist as e:
            return Response({'message': str(e)}, status=400)

        return Response(serializer.data)

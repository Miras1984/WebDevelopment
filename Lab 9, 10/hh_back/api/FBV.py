from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import Company, Vacancy

from api.serializers import CompanySerializer, VacancySerializer
# Create your views here.


@api_view(['GET', 'POST'])
def show_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def show_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as ex:
        return Response({'message': str(ex)}, status=400)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        company.delete()
        return Response({'message': 'deleted'}, status=204)


@api_view(['GET', 'POST'])
def show_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def show_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as ex:
        return Response({'message': str(ex)}, status=400)

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CompanySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({'message': 'deleted'}, status=204)


@api_view(['GET'])
def show_vacancies_by_company(request, company_id):
    try:
        vacancies = Vacancy.objects.filter(company_id=company_id)
        serializer = VacancySerializer(vacancies, many=True)
    except Company.DoesNotExist as ex:
        return Response({'message': str(ex)}, status=400)

    return Response(serializer.data)


@api_view(['GET'])
def top_ten(request):
    try:
        vacancies = Vacancy.objects.all().order_by('-salary')
        serializer = VacancySerializer(vacancies, many=True)
    except Vacancy.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    return Response(serializer.data)

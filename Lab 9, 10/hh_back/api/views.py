from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy
import json

from api.serializers import CompanySerializer, VacancySerializer
# Create your views here.


@csrf_exempt
def show_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)


@csrf_exempt
def show_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as ex:
        return JsonResponse({'message': str(ex)}, status=400)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


@csrf_exempt
def show_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)


@csrf_exempt
def show_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as ex:
        return JsonResponse({'message': str(ex)}, status=400)

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer(instance=vacancy, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


def show_vacancies_by_company(request, company_id):
    try:
        vacancies = Vacancy.objects.filter(company_id=company_id)
        serializer = VacancySerializer(vacancies)
    except Company.DoesNotExist as ex:
        return JsonResponse({'message': str(ex)}, status=400)

    return JsonResponse(serializer.data, safe=False)


def top_ten(request):
    try:
        vacancies = Vacancy.objects.all().order_by('-salary')
        serializer = VacancySerializer(vacancies, many=True)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(serializer.data, safe=False)

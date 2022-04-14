from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy
import json
# Create your views here.


@csrf_exempt
def show_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.create(name=data['name'],
                                             description=data['description'],
                                             city=data['city'],
                                             address=data['address'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(company.to_json())


@csrf_exempt
def show_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as ex:
        return JsonResponse({'message': str(ex)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data['name']
        company.city = data['city']
        company.address = data['address']
        company.description = data['description']
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


@csrf_exempt
def show_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            vacancy = Vacancy.objects.create(name=data['name'],
                                             description=data['description'],
                                             salary=data['salary'],
                                             company=data['company'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(vacancy.to_json())


@csrf_exempt
def show_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as ex:
        return JsonResponse({'message': str(ex)}, status=400)

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())

    if request.method == 'PUT':
        data = json.loads(request.body)
        vacancy.name = data['name']
        vacancy.salary = data['salary']
        vacancy.description = data['description']
        vacancy.company = data['company']
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


def show_vacancies_by_company(request, company_id):
    try:
        vacancies = Vacancy.objects.filter(company_id=company_id)
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    except Company.DoesNotExist as ex:
        return JsonResponse({'message': str(ex)}, status=400)

    return JsonResponse(vacancies_json, safe=False)


def top_ten(request):
    try:
        vacancies = Vacancy.objects.all().order_by('-salary')
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(vacancies_json, safe=False)

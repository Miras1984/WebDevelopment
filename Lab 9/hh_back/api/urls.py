from django.urls import path
from api.views import show_company, show_vacancy, show_companies, show_vacancies, show_vacancies_by_company, top_ten

urlpatterns = [
    path('companies/', show_companies),
    path('companies/<int:company_id>/', show_company),
    path('companies/<int:company_id>/vacancies', show_vacancies_by_company),
    path('vacancies/', show_vacancies),
    path('vacancies/<int:vacancy_id>/', show_vacancy),
    path('vacancies/top_ten', top_ten)
]

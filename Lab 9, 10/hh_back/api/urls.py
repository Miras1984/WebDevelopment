from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

#from api.views import show_company, show_vacancy, show_vacancies, show_vacancies_by_company, top_ten, show_companies
#from api.FBV import show_company, show_vacancy, show_vacancies, show_vacancies_by_company, top_ten, show_companies
from api.CBV import show_companyAPIView, show_companiesAPIView, show_vacancyAPIView, show_vacancies_by_companyAPIView, show_vacanciesAPIView, top_tenAPIView

#urlpatterns = [
#    path('companies/', show_companies),
#    path('companies/<int:company_id>/', show_company),
#    path('companies/<int:company_id>/vacancies', show_vacancies_by_company),
#    path('vacancies/', show_vacancies),
#    path('vacancies/<int:vacancy_id>/', show_vacancy),
#    path('vacancies/top_ten', top_ten)
#]

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('companies/', show_companiesAPIView.as_view()),
    path('companies/<int:pk>/', show_companyAPIView.as_view()),
    path('companies/<int:pk>/vacancies', show_vacancies_by_companyAPIView.as_view()),
    path('vacancies/', show_vacanciesAPIView.as_view()),
    path('vacancies/<int:pk>/', show_vacancyAPIView.as_view()),
    path('vacancies/top_ten', top_tenAPIView.as_view())
]

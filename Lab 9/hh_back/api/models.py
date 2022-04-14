from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='A good company')
    city = models.CharField(max_length=100, default='Almaty')
    address = models.TextField(default='')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    salary = models.FloatField(default=1000)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, default=1)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def to_json(self):
        return{
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }


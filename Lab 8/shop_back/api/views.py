from django.shortcuts import render
from django.http.response import JsonResponse

from api.models import Product, Category
# Create your views here.


def show_products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def show_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as ex:
        return JsonResponse({'message': str(ex)}, status=400)

    return JsonResponse(product.to_json())


def show_categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def show_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Product.DoesNotExist as ex:
        return JsonResponse({'message': str(ex)}, status=400)

    return JsonResponse(category.to_json())


def show_products_category(request, category_id):
    try:
        products = Product.objects.filter(categoryId=category_id)
        products_json = [product.to_json() for product in products]
    except Category.DoesNotExist as ex:
        return JsonResponse({'message': str(ex)}, status=400)

    return JsonResponse(products_json, safe=False)



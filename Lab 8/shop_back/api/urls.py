from django.urls import path
from api.views import show_products, show_product, show_categories, show_category, show_products_category

urlpatterns = [
    path('products/', show_products),
    path('products/<int:product_id>/', show_product),
    path('categories/', show_categories),
    path('categories/<int:category_id>/', show_category),
    path('categories/<int:category_id>/products', show_products_category)
]
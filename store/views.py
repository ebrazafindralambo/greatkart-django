from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category

def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        print(type(categories))
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    contexte = {"products": products,
                "product_count":product_count,
                "category_slug":category_slug,
                }
    return render(request, "store/store.html", contexte)

def product_detail(request, category_slug=None, product_slug=None):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product':single_product,
    }
    return render(request, "store/product_detail.html", context)

    p
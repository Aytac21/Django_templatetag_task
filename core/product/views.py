from django.shortcuts import render
from django.db.models import F, FloatField
from django.db.models.functions import Coalesce
from .models import Product

def list_view(request):
    products = Product.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        total_price=F("price") - F("discount")
    )
    context = {
        "products": products
    }
    return render(request, "list.html", context)


def list_2_view(request):
    products = Product.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        total_price=F("price") - F("discount")
    )
    context = {
        "products": products
    }
    return render(request, "list_2.html", context)

from django.db.models import Avg, Max, F, FloatField, Sum

#for average price
Book.objects.all().aggregate(Avg('price'))

#for maximum price
Book.objects.all().aggregate(Max('price'))

#cost per page
Book.objects.all().aggregate(
   price_per_page = Sum(F('price')/F('pages'), output_field=FloatField())
)
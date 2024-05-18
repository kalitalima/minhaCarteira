from django.contrib import admin
from .models import Categoria, Despesa, FormaPagamento
# Register your models here.
admin.site.register(Categoria)
admin.site.register(FormaPagamento)
admin.site.register(Despesa)

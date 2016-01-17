from django.contrib import admin
from models import Standard,Dataset, FragmentationSpectrum, Adduct, Xic
# Register your models here.
admin.site.register(Standard)
admin.site.register(Adduct)
admin.site.register(Dataset)
admin.site.register(FragmentationSpectrum)
admin.site.register(Xic)
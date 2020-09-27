from django.contrib import admin
from sample_app.models.memo import Memo

# Register your models here.
@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    pass
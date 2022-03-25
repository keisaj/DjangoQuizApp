from django.contrib import admin
from .models import Question, Category
# Register your models here.


@admin.register(Question)
class QuizAdmin(admin.ModelAdmin):

    list_display = ["question"]
    search_fields = ("question", "category")
    list_filter = ("category",)


admin.site.register(Category)

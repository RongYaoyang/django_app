from django.contrib import admin
from app01 import models

# Register your models here.
admin.site.register(models.Person)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.Student_Class)
admin.site.register(models.Type)
admin.site.register(models.Type_Text)
admin.site.register(models.Type_Choice)
admin.site.register(models.Type_Score)
admin.site.register(models.Questions)
admin.site.register(models.QuestionPapers)
admin.site.register(models.Answer)
# admin.site.register(models.Person)

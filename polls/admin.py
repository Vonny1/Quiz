from django.contrib import admin


from .models import Question, Listotvet,Listscore

admin.site.register(Question)
admin.site.register(Listotvet)
admin.site.register(Listscore)

# Register your models here.

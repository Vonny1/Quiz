from django.db import models
class Question(models.Model):
    question_text= models.CharField(max_length=200)
    question_answer=models.CharField(max_length=200)
    def __str__(self):
        return self.question_text
class Listotvet(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    otvet = models.CharField(max_length=200, default= "0")
    def __str__(self):
        return self.question.question_text +" =" +  self.otvet

class Listscore(models.Model):
    otvet = models.OneToOneField(Listotvet, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)


# Create your models here.

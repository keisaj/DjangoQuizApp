from django.db import models

# Create your models here.



class Question(models.Model):

    question = models.CharField(max_length=200, null=True, blank=False)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    option1 = models.CharField(max_length=200, null=True, blank=True)
    option2 = models.CharField(max_length=200, null=True, blank=True)
    option3 = models.CharField(max_length=200, null=True, blank=True)
    option4 = models.CharField(max_length=200, null=True, blank=True)
    correct_answer = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return str(self.question)

class Category(models.Model):

    name = models.CharField(max_length=20, blank=False, default='', null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)
from django.db import models

# Create your models here.
class Fashion(models.Model):
    fash_question = models.CharField(max_length=200) #fash_question, pub_date are d field name etc.
    pub_date = models.DateTimeField('Publication Date')


class Style(models.Model):
    fashion = models.ForeignKey(Fashion, on_delete=models.CASCADE) #foriegnkey tells django dat each styles is related to a Fashion
    style_choice = models.CharField(max_length=200) #first field of d Style #each Choice style of d user is associated with a fashion_question
    style_pick = models.IntegerField(default=0) #second field of d style
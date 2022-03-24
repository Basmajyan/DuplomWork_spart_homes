from tabnanny import verbose
from django.db import models


class UserInfo(models.Model):
    user = models.CharField(verbose_name="Пользователь", max_length=80)
    
class Solution(models.Model):
    solution = models.CharField(verbose_name="Решение для УД", max_length=100)
    action = models.CharField(verbose_name="Действия", max_length=100)
    date = models.DateField(verbose_name="Дата", auto_now_add=True)
    
    def  __str__(self):
        return self.solution + ' ' + self.action
    
class ConnectedSolution(models.Model):
    author = models.CharField(verbose_name="ИД автора", max_length=100,blank=True)
    solutionID = models.CharField(verbose_name="ИД решение УД", max_length=100)
    status = models.CharField(max_length=60, verbose_name='Статус',choices=(('none','none'),('treatment','В обработке'),('connected','Подключено')), default='none',null=True) 
    date = models.DateField(verbose_name="Дата", auto_now_add=True)
        
    def  __str__(self):
        return self.solutionID + ' ' + self.author

class Action(models.Model):
    solution = models.CharField(verbose_name="ИД решении", max_length=100,blank=True)
    author = models.CharField(verbose_name="ИД автора", max_length=100,blank=True)
    date = models.DateTimeField(verbose_name='Дата и время', auto_now=True)
    
    def  __str__(self):
        return self.solution + ' ' + self.author
    
class Communal(models.Model):
    mounth = models.CharField(verbose_name="Месяц", max_length=25,blank=True)
    author = models.CharField(verbose_name="ИД автора", max_length=100,blank=True)
    date = models.DateTimeField(verbose_name='Дата и время', auto_now=True)
    
    def  __str__(self):
        return self.mounth + ' ' + self.author
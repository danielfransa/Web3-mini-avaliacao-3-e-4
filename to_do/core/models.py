from django.db import models

class Tarefa(models.Model):
    tarefa = models.CharField('Tarefa', max_length=100)
    inicio = models.DateField('Início')
    fim = models.DateField('Fim')
    status = models.CharField('Status',max_length=15)

def __str__(self):
    return self.tarefa

class Meta:
    verbose_name_plural = 'Feriados'
    verbose_name = 'Feriado'


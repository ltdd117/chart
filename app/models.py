from django.db import models
import string
import random

class ChartView(models.Model):
        start_at = models.FloatField(max_length=8,default='')
        end_at = models.FloatField(max_length=8,default='')
        poinLt_1 = models.FloatField(max_length=10)

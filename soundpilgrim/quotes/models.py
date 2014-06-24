from django.db import models

class Quote(models.Model):
    created_on = models.DateField('Date Created', null=False, editable=True)
    text = models.TextField(null=False)
    quoter = models.CharField(max_length=100, null=False)

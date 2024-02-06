from django.db import models

# Create your models here.

class CodeExplainer(models.Model):
    _input = models.TextField()
    _output = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "t_code_explainer"
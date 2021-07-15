from django.db import models
from django.contrib.auth.models import User 

# ---------------------------------------------------------------- 
class Employee(models.Model): 

    employee_id = models.ForeignKey(User, related_name='EMP_USER', on_delete=models.CASCADE) # foreign key refrecing to user. 
    employee_level = models.IntegerField(null=False) # employee level for dataAcess. 


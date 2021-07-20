from django.db import models
from django.contrib.auth.models import User 

class Mould(models.Model): 

    mould_id = models.IntegerField(primary_key=True)
    mould_name = models.CharField(max_length=200)
    cavity_number = models.IntegerField()
    registered_date = models.DateTimeField(auto_now_add=True)
    registered_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    threshold_value = models.IntegerField()
    present_count = models.IntegerField()

 
    def __str__(self): 
        return self.mould_name
    


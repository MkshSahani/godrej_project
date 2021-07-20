from django.db import models
from django.contrib.auth.models import User 

# -------------------------------------------------------------------------------
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

    def alert(self): 
        return self.threshold_value - self.present_count <= 500  


# -------------------------------------------------------------------------------- 

class MouldStatus(models.Model): 

    mould_id = models.ForeignKey(Mould, related_name='mould_status', on_delete=models.PROTECT, primary_key=True)
    status_update = models.DateTimeField(auto_now_add=True, primary_key=True)
    count_increment = models.IntegerField() # daily increment. 

    def __str__(self): 
        return str(self.mould_id) 






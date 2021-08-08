from django.db import models


# ------------------------------------- 
class PPMData(models.Model): 

    new_code =  models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=200)
    ppm_data_added = models.DateField(auto_now_add=True)
    total_number_of_lot = models.IntegerField()
    total_number_of_lot_rejected = models.IntegerField()


    def ppm(self): 
        
        number_of_lot_accepted = self.total_number_of_lot - self.total_number_of_lot_rejected
        return number_of_lot_accepted / (10 ** 6)
    
    
    def __str__(self): 
        return self.new_code + self.vendor_name


# ---------------------------------------- 

class DamageType(models.Model): 

    mould_name = models.CharField(max_length=200)
    mould_severity_level = models.IntegerField()

    def __str__(self):
        return self.mould_name + "_" + str(self.mould_severity_level) 
    
    
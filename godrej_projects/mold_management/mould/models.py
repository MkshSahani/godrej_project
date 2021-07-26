from django.db import models
from django.contrib.auth.models import User 

# -------------------------------------------------------------------------------
class Mould(models.Model): 

    mould_id = models.IntegerField(primary_key=True)
    mould_name = models.CharField(max_length=200)
    cavity_number = models.IntegerField()
    registered_date = models.DateTimeField(auto_now_add=True)
    registered_by = models.ForeignKey(User, on_delete=models.PROTECT) 

    general_maintaince_cleaning_threshold_value = models.IntegerField() 
    preventive_maintaince_clearning_thresold_value = models.IntegerField()
    tool_life = models.IntegerField()


    present_count = models.IntegerField()
    # * tool live over shots. 


 
    def __str__(self): 
        return str(self.mould_id)

    def general_alert(self):  # alert general cleaning. 
        mould_status_data = MouldStatus.objects.filter(mould_id = self.mould_id)
        count = 0 
        for mould in mould_status_data: 
            count = count + mould.count_increment 
        return self.general_maintaince_cleaning_threshold_value -count <= 500

    def preventive_maintance_alert(self): # preventive maintance alert function. 
        mould_status_data = MouldStatus.objects.filter(mould_id = self.mould_id)
        count = 0 
        for mould in mould_status_data: 
            count = count + mould.count_increment 
        return self.preventive_maintaince_clearning_thresold_value - count <= 500 
    
    def tool_life_over_alert(self): # tool live over alert. 
        mould_status_data = MouldStatus.objects.filter(mould_id = self.mould_id)
        count = 0 
        for mould in mould_status_data: 
            count = count + mould.count_increment 
        
        return self.tool_life - count <= 500 
    
    



# TODO : -------------------------------------------------------------------------------- 

class MouldStatus(models.Model): 

    mould_id = models.ForeignKey(Mould, related_name='mould_status', on_delete=models.CASCADE)
    status_update = models.DateTimeField(auto_now_add=True)
    count_increment = models.IntegerField() # daily increment. 

    def __str__(self): 
        return str(self.mould_id)
    
    # excel file updated . 
    # * no movind mould -> no entry for more than 2 years. 
    


# -----------------------------------------------------------------------------------
class MouldComment(models.Model): 

    mould_id = models.ForeignKey(Mould, related_name='mould_chat', on_delete=models.CASCADE)
    # -> 
    comment_text = models.TextField()
    commented_by = models.ForeignKey(User,related_name='chat_user', on_delete=models.CASCADE)
    commented_date_time = models.DateTimeField(auto_now_add=True)




# TODO : --------------------------------------------------------------- 

class MouldData(models.Model): 

    mould_id = models.ForeignKey(Mould, related_name='mould_data', on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    department_name = models.CharField(max_length=100) 
    product_line = models.CharField(max_length=100)  



# TODO : ---------------------------------------------------------------- 
class ProductLine(models.Model): 

    product_line_number = models.IntegerField() # numbef of product line. 
    product_line_name = models.CharField(max_length=100)


# ------------------------------------------------------------------ 
class Department(models.Model): 

    department_name = models.CharField(max_length=20) # name of department. 
    department_id = models.CharField(max_length=20) # id of department. 

# ------------------------------------------------------------------- 


from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Student(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'Student'
        
        
class todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=False)
    todo_name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.todo_name
    
    class Meta:
        db_table = 'todo_list'
        
    


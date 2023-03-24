from django.db import models

# Create your models here.
class department(models.Model):
    department_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, null=False)

    
    
    def __str__(self):
        return f"{self.department_id},{self.name}"
class Member(models.Model):
    # department_id=models.ForeignKey(department,default=None,null = False,on_delete=models.CASCADE)
    member_id=models.AutoField(primary_key=True)
    User=models.CharField(max_length=50, null=False)
    Bookname = models.CharField(max_length=100, null=False)
    
    
    def __str__(self):
        return f"{self.member_id},{self.User},{self.User},{self.Bookname}"#{self.department_id},
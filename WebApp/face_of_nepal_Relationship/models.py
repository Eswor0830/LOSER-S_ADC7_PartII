from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class FreeLancer(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    Mobile_No=models.IntegerField()
    Location=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Name,self.Email,self.Mobile_No,self.Location}"



class Payment(models.Model):
    
    Cash=models.IntegerField()  
    Cheque=models.CharField(max_length=30)

    # def __str__(self):
    #     return "{self.Cash,self.Cheque}"

class Tourist(models.Model):
    
    Guide=models.ManyToManyField(FreeLancer,blank=True,related_name="guide")
    Tourist_Name=models.CharField(max_length=20)
    Tourist_Email=models.EmailField(max_length=30)
    Tourist_Mobile_No=models.IntegerField()
    Tourist_address=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.Package_cost,self.Guide,self.Tourist_Name,self.Tourist_Email,self.Tourist_Mobile_No,self.Tourist_address}"


class Business(models.Model):
    company_name=models.CharField(max_length=20)
    company_location=models.CharField(max_length=20)
    package_name=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.company_name,self.company_location,self.package_name}"

class Administrator(models.Model):
    admin=models.ForeignKey(FreeLancer,on_delete=models.CASCADE,related_name='admin' )
    Guide=models.OneToOneField(FreeLancer,  on_delete = models.CASCADE, primary_key = False,related_name='admin_guide')
    Username=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Username,self.admin,self.Guide}" 

































































































































































































































































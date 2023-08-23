from django.db import models

# Create your models here.

class Cars(models.Model):
    img = models.ImageField(upload_to='home/files/covers')
    img1 = models.ImageField(upload_to='home/files/covers' , blank=True)
    img2= models.ImageField(upload_to='home/files/covers' , blank=True)
    img3 = models.ImageField(upload_to='home/files/covers' , blank=True)
    img4 = models.ImageField(upload_to='home/files/covers' , blank=True)
    img5 = models.ImageField(upload_to='home/files/covers' , blank=True)
    img6 = models.ImageField(upload_to='home/files/covers' , blank=True)
    cars_name = models.CharField(max_length=64)
    kms = models.IntegerField(blank = True)
    color = models.TextField(blank=True)
    maintance = models.TextField(blank=True)
    parag = models.TextField(blank=True)


    def __str__(self) :
        return f'{self.cars_name} color : {self.color}'
    


class about(models.Model) :
    header = models.CharField(max_length=64)    
    parag1 = models.TextField(blank = True)    
    parag2 = models.TextField(blank = True)    


    def __str__(self) -> str:
        return f"matn about {self.header}"    
    
class Contact(models.Model) :
    name =models.CharField(max_length=64)  
    name_owner =models.CharField(max_length=64)  
    parag1 =models.TextField(blank = True) 
    parag2 =models.TextField(blank = True)    
    number1 =models.TextField(blank = True)    
    number2 =models.TextField(blank = True)    


    def __str__(self) :
        return f"{self.name} , {self.name_owner} "
   

class Home(models.Model) :
    imgone = models.ImageField(blank=True , upload_to='home/files/covers')
    nameone = models.CharField(max_length=64)
    paragone =models.TextField(blank = True)   
    imgtwo = models.ImageField(blank=True , upload_to='home/files/covers')
    nametwo = models.CharField(max_length=64)
    paragtwo =models.TextField(blank = True)   
    imgthree = models.ImageField(blank=True , upload_to='home/files/covers')
    namethree = models.CharField(max_length=64)
    paragthree =models.TextField(blank = True) 
    paragerafe_asli = models.TextField(blank=True)  
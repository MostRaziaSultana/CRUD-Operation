from django.db import models

# Create your models here.

class Profile(models.Model):
    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    RELIGION=(
        ('Islam','Islam'),
        ('Hindu','Hindu'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,null=True,blank=True)
    image = models. ImageField(upload_to='prof_pic/', default= 'def.png', null=True, blank=True)
    address = models. TextField(max_length=50, null= True)
    number = models.IntegerField()
    age = models.FloatField()
    gender = models.CharField(max_length=8, choices=GENDER,default=None)
    religion = models.CharField(max_length=10, choices=RELIGION, default=None)
    division= models.CharField(max_length=5, null=True)
    color = models.CharField(max_length=10,null=True)

    def __str__(self):
     return str(self.name)

class Custom_User(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='Profile')

    def __str__(self):
        return str(self.profile.name)





models.OneToOneField
models.ForeignKey
models.ManyToManyField















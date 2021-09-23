from django.db import models

# Create your models here.
class EditEdu(models.Model):
    UniName= models.CharField(max_length=50)
    Degree=models.CharField(max_length=50)
    Majors= models.CharField(max_length=20)
    def __str__(self):
        return self.UniName
class EditExp(models.Model):
    Company= models.CharField(max_length=20)
    Designation= models.CharField(max_length=20)
    Description= models.CharField(max_length=200)
    months= models.CharField(max_length=20)
    def __str__(self):
        return self.Company
class EditProj(models.Model):
    Title= models.CharField(max_length=50)
    Desc= models.CharField(max_length=200)
    Year= models.CharField(max_length=20)
    def __str__(self):
        return self.Title
class EditLin(models.Model):
    SiteNam= models.CharField(max_length=30)
    Urlo= models.CharField(max_length=100)
    def __str__(self):
        return self.SiteNam
class EditSkill(models.Model):
    Skill= models.CharField(max_length=20)
    Per= models.CharField(max_length=5)
    def __str__(self):
        return self.Skill
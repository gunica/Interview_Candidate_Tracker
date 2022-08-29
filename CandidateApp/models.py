from django.db import models

# Create your models here.

class CandidateDetails(models.Model):
    CandidateId = models.AutoField(primary_key=True, default=0)
    Name = models.CharField(max_length=500)

class ContactDetails(models.Model):
    candidatedetails = models.ForeignKey(CandidateDetails, default=0, on_delete=models.CASCADE, related_name='details')
    CandidateId = models.IntegerField()
    PhoneNumber = models.CharField(max_length=10)
    Email = models.EmailField(max_length=40)
    Address = models.CharField(max_length=500)
    Location = models.CharField(max_length=20)

class TechSkills(models.Model):
   candidatedetails = models.ForeignKey(CandidateDetails, on_delete=models.CASCADE, related_name='skills')
   CandidateId = models.IntegerField()
   Skills = models.CharField(max_length=50)


# class CandidateDetails(models.Model): 
#     CandidateId = models.IntegerField()
#     Name = models.CharField(max_length=3, null=True) 
#     def __str__(self): 
#         return self.CandidateId

# class ContactDetails(models.Model): 
#     candidatedetails = models.ForeignKey(CandidateDetails, on_delete=models.CASCADE, null=True)
#     CandidateId = models.IntegerField()
#     PhoneNumber = models.CharField(max_length=10)
#     Email = models.EmailField(max_length=40)
#     Address = models.CharField(max_length=500)
#     Location = models.CharField(max_length=20)
#     def __str__(self): 
#         return self.state_name

# class TechSkills(models.Model): 
#     city_name = models.CharField(max_length=200, null=True) 
#     countrystate = models.ForeignKey(countrystate, on_delete=models.CASCADE, null=True) 
#     def __str__(self): 
#         return self.city_name
from pyexpat import model
from rest_framework import serializers
from CandidateApp.models import CandidateDetails, ContactDetails, TechSkills
#from CandidateApp.models import CandidateDetails, TechSkills

class CandidateDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CandidateDetails
        fields=('CandidateId','Name')

class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactDetails
        fields=('CandidateId','PhoneNumber','Email','Address','Location')

class TechSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TechSkills
        fields=('CandidateId','Skill')
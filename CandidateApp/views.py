from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CandidateApp.models import CandidateDetails,ContactDetails,TechSkills
#from CandidateApp.models import CandidateDetails,TechSkills
from CandidateApp.serializers import CandidateDetailsSerializer,ContactDetailsSerializer,TechSkillsSerializer

# Create your views here.

@csrf_exempt
def listApi(request,id=0):
    if request.method=='GET':
        #candidates = CandidateDetails.objects.filter(ContactDetails__TechSkills)
        #candidates=CandidateDetails.objects.raw('select * from candidateapp_candidatedetails INNER JOIN candidateapp_contactdetails on candidateapp_candidatedetails.CandidateId=candidateapp_contactdetails.CandidateId_id ')
        #candidates = CandidateDetails.objects.select_related('details','skills')#.filter(details__Location__icontains='Hyderabad',skills__Skills_icontains='Python')
        candidates = CandidateDetails.objects.all()
        candidates_serializer=CandidateDetailsSerializer(candidates,many=True)
        return JsonResponse(candidates_serializer.data,safe=False)

# @csrf_exempt
# def listApi(request):
#     candidates = TechSkills.objects.all()
#     candidates_serializer=CandidateDetailsSerializer(candidates,many=True)
#     return JsonResponse(candidates_serializer.data,safe=False)

@csrf_exempt
def add_candidateApi(request,id=0):
    if request.method=='POST':
        candidate_data=JSONParser().parse(request)
        candidatedetails_serializer=CandidateDetailsSerializer(data=candidate_data)
        if candidatedetails_serializer.is_valid():
            candidatedetails_serializer.save()
            return JsonResponse("Candidate Added Succesfully!", safe=False)
        return JsonResponse("Failed to Add",safe=False)
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader,RequestContext
from django.views.decorators.csrf import csrf_exempt
from .models import PatientData
import json,datetime
from django.conf import settings
from django.core.files.images import ImageFile
# Create your views here.
def index(request):
    template = loader.get_template('patient/index.html')
    return render(request,'patient/index.html')

def result(request):
    patientName = request.POST['patient_name']
    patientCode = request.POST['patient_code']
    patientAge = request.POST['patient_age']
    physicianName = request.POST['physician_name']
    diagnosticsValue = request.POST['diagnostics']
    patientImage= request.FILES['patient_image']

    if(patientName and patientCode and patientAge and physicianName and diagnosticsValue and patientImage):
        q=PatientData(patient_name=patientName,patient_code=patientCode,patient_age=patientAge,physician_name=physicianName,diagnostics=diagnosticsValue)
        q.patient_picture=patientImage
        q.save()
        #destination = open('/uploads/'+ patientImage)
        #destination.close()
        return render_to_response("patient/result.html")
    else:
        return render_to_response('patient/index.html')

@csrf_exempt
def mobileApp(request):
    input = request.body.decode("UTF-8")
    data = json.loads(input)
    errorResult = {'error':'error'}
    if(data['patient_name'] and data ['patient_code']):
        if(PatientData.objects.filter(patient_name = data['patient_name']).filter(patient_code=data['patient_code'])):
            q= PatientData.objects.get(patient_name= data['patient_name'])
            #image =encode_image(Image.open(q.patient_picture))
            #image = encode_image(q.patient_picture)

            image =  "http://192.168.43.156:8000"+ q.patient_picture.url

            result ={
                'patient_name':q.patient_name,
                'patient_age':q.patient_age,
                'physician_name':q.physician_name,
                'diagnostics':q.diagnostics,
                'patient_image': image
                     }
            return HttpResponse(json.dumps(result))
        else:
            return HttpResponse(json.dumps(errorResult))
    else:
        return HttpResponse(json.dumps(errorResult))


def encode_image(obj):
    """
    Extended encoder function that helps to serialize dates and images
    """

    if isinstance(obj, ImageFile):
        try:
            return obj.path
        except ValueError as e:
            return ''

    raise TypeError(repr(obj) + " is not JSON serializable")
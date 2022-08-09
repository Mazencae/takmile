from django.shortcuts import render,redirect,reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ScientificSerializer,ChoiceScientificSerializer,LiterarySerializer,ChoiceLiterarySerializer
# Create your views here.
from api.models import Scientific,ChoiceScientific,Literary,ChoiceLiterary


@api_view(['GET'])
def getroot(request):
    root=[
        {
            'endpoint':'details/<str:number>/<str:gender>',
            'method':'GET',
            'body':'{"id": ,"name": ,"father_name": ,"mather_name": ,"Arabic": ,"Maths": ,"English": ,"French": ,"biology": ,"Physics": ,"chemistry": ,"nationalism": ,"Islamic": ,"number": }',
            'description':'تفاصيل الطالب'
        },
        {
            'endpoint':'det/<str:gender>',
            'method':'GET',
            'body':'[{"id": ,"title":["","",""],"number": },[{"id": ,"title":["","",""],"number": }',
            'description':'جميع طلبات الطلاب التي قدمت'
        },
        {
            'endpoint':'det/<str:gender>/create',
            'method':'POST',
            'body':'{"title": ["","",""],"number": }',
            'description':'التقديم على المواد'
        },
        {
            'endpoint':'update/<str:number>/<str:gender>',
            'method':'PUT',
            'body':'{"title": ["","",""],"number": }',
            'description':'التعديل ع الطلب المقدم'
        },
        {
            'endpoint':'delete/<str:number>/<str:gender>',
            'method':'DELETE',
            'body':'',
            'description':'حذف الطلب المقدم'
        },
        {
            'endpoint':'details/<str:gender>',
            'method':'GET',
            'body':'[{"id": ,"name": ,"father_name": ,"mather_name": ,"Arabic": ,"Maths": ,"English": ,"French": ,"biology": ,"Physics": ,"chemistry": ,"nationalism": ,"Islamic": ,"number": },{...}]',
            'description':'علامات ومعلومات كل الطلاب '
        },
        {
            'علمي':'Scientific',
            'ادبي':'Literary'

        }

    ]
    return Response(root)

@api_view(['GET'])
def getData(request,gender):
    if gender =='Scientific':
        details=Scientific.objects.all()
        serializer=ScientificSerializer(details,many=True)
        return Response(serializer.data)    
    elif gender =='Literary':
        details=Literary.objects.all()
        serializer=LiterarySerializer(details,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getDataSegnal(request,number,gender):
    if gender =='Scientific':
        details=Scientific.objects.get(number=number)
        serializer=ScientificSerializer(details,many=False)
        return Response(serializer.data) 
    elif gender =='Literary':   
        details=Literary.objects.get(number=number)
        serializer=LiterarySerializer(details,many=False)
        return Response(serializer.data) 

@api_view(['GET'])
def getChois(request,gender):
    if gender =='Scientific':
        det=ChoiceScientific.objects.all()
        serializer_context = {
                'request': request,
            }
        serializer=ChoiceScientificSerializer(det,context=serializer_context,many=True)
        return Response(serializer.data) 
    elif gender =='Literary': 
        det=ChoiceLiterary.objects.all()
        serializer_context = {
                'request': request,
            }
        serializer=ChoiceLiterarySerializer(det,context=serializer_context,many=True)
        return Response(serializer.data)


@api_view(['POST'])
def createChois(request,gender):
    if gender =='Scientific':
        GS='Scientific'
        data=request.data
        print(request.data)
        chick_unique=ChoiceScientific.objects.values_list('number',flat=True)
        if len(data.get('title'))<=3 and data['number'] not in chick_unique:
            
            det=ChoiceScientific.objects.create(
                title=data['title'],
                number=data['number']
            )
            serializer_context = {
                    'request': request,
                }
            serializer=ChoiceScientificSerializer(det,context=serializer_context,many=False)
            print(serializer.data)
            return Response(serializer.data)   
        else :
            print(GS)
            #return redirect(createChois(request,gender=GS))
            return redirect(reverse("output_page",kwargs={'gender':'Scientific'}))

    elif gender =='Literary': 
        GL='Literary'
        data=request.data
        print(request.data)
        chick_unique=ChoiceLiterary.objects.values_list('number',flat=True)
        if len(data.get('title'))<=3 and data['number'] not in chick_unique:
            
            det=ChoiceLiterary.objects.create(
                title=data['title'],
                number=data['number']
            )
            serializer_context = {
                    'request': request,
                }
            serializer=ChoiceLiterarySerializer(det,context=serializer_context,many=False)
            print(serializer.data)
            return Response(serializer.data)   
        else :
            print(GL)
            return redirect(reverse("output_page",kwargs={'gender':'Literary'}))

@api_view(['PUT'])
def UpdateChois(request,number,gender):
    if gender =='Scientific':
        data=request.data
        print(data)
        details=ChoiceScientific.objects.values_list('id',flat=True).filter(number=number)
        dat=ChoiceScientific.objects.get(id=details[0])
        #dat=ChoiceScientific.objects.get(id=data['id'])
        print(data)
        serializer_context = {
                    'request': request,
                }
        #serializer=ChoiceScientificSerializer(dat,data=request.data,context=serializer_context)
        serializer=ChoiceScientificSerializer(dat,data=request.data,context=serializer_context)
        if serializer.is_valid():
            serializer.save()
        else:    
            serializer.errors 
        return Response(serializer.data)

    elif gender =='Literary':
        data=request.data
        print(data)
        details=ChoiceLiterary.objects.values_list('id',flat=True).filter(number=number)
        dat=ChoiceLiterary.objects.get(id=details[0])
        #dat=ChoiceScientific.objects.get(id=data['id'])
        print(data)
        serializer_context = {
                    'request': request,
                }
        #serializer=ChoiceScientificSerializer(dat,data=request.data,context=serializer_context)
        serializer=ChoiceLiterarySerializer(dat,data=request.data,context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:    
            print(serializer.errors)
            return redirect(reverse("update_page",kwargs={'number':number,'gender':'Literary'}))
        

@api_view(['DELETE'])
def deleteChois(request,number,gender):
    if gender =='Scientific':
        details=ChoiceScientific.objects.values_list('id',flat=True).filter(number=number)
        dat=ChoiceScientific.objects.get(id=details[0])
        dat.delete()
        return Response('choice was deleted!')
from rest_framework import serializers,fields
from api.models import Scientific,Scientific_CHOICES,ChoiceScientific,Literary,Literary_CHOICES,ChoiceLiterary

class ScientificSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientific
        fields = '__all__'



# class ChoiceSubSerializer(serializers.HyperlinkedModelSerializer):
#     # ...
#     my_field = fields.MultipleChoiceField(choices=Sub_CHOICES)
#     class Meta:
#         model = ChoiceSub
#         fields =('title','my_field')
##############################################################? *
class CustomMultipleChoiceField(fields.MultipleChoiceField):
    def to_representation(self, value):
        return list(super().to_representation(value))
class ChoiceScientificSerializer(serializers.ModelSerializer):          
    class Meta:
        model = ChoiceScientific
        fields =('id','title','number')
     ############################################################## ? this and help from * solve the proplem of serializer how [\'name\'] 
    title= CustomMultipleChoiceField(choices=Scientific_CHOICES)    

class LiterarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Literary
        fields = '__all__'

class CustomMultipleChoiceField(fields.MultipleChoiceField):
    def to_representation(self, value):
        return list(super().to_representation(value))
class ChoiceLiterarySerializer(serializers.ModelSerializer):          
    class Meta:
        model = ChoiceLiterary
        fields =('id','title','number')
    title= CustomMultipleChoiceField(choices=Literary_CHOICES)    



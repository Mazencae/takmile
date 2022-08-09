from django.db import models

from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here
class Scientific(models.Model):
    name=models.CharField(max_length=200,verbose_name="الاسم ")
    father_name=models.CharField(max_length=200,verbose_name="اسم الاب ")
    mather_name=models.CharField(max_length=200,verbose_name="اسم الام ")
    Arabic= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(400)],verbose_name="اللغة العربية ")
    Maths=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(600)],verbose_name="الرياضيات ")
    English= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)],verbose_name="اللغة الانكليزية ")
    French= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)],verbose_name="اللغة الفرنسية ")
    biology= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)],verbose_name="علم احياء ")
    Physics= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(400)],verbose_name="الفيزياء ")
    chemistry= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)],verbose_name="الكيمياء ")
    nationalism= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)],verbose_name="التربية القومية ")
    Islamic= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)],verbose_name="التربية الاسلامية ")
    number=models.IntegerField(validators=[MinValueValidator(0)],verbose_name="رقم الطالب ",unique=True)
    def __str__(self):
        full_name=self.name +" "+ self.father_name +" "+ self.mather_name
        return full_name

Scientific_CHOICES=(
        ("اللغة العربية","اللغة العربية"),
        ("الرياضيات","الرياضيات"),
        ("اللغة الانكليزية","اللغة الانكليزية"),
        ("اللغة الفرنسية","اللغة الفرنسية"),
        ("علم الاحياء","علم الاحياء"),
        ("الفيزياء","الفيزياء"),
        ("الكيمياء","الكيمياء"),
        ("التربية القومية","التربية القومية"),
        ("التربية الاسلامية","التربية الاسلامية")
        )
class ChoiceScientific(models.Model):
    title=MultiSelectField(choices=Scientific_CHOICES,max_choices=3,verbose_name="قائمة المواد ")    
    number=models.IntegerField(validators=[MinValueValidator(0)],verbose_name="رقم الطالب ",unique=True)


class Literary(models.Model):
    name=models.CharField(max_length=200,verbose_name="الاسم ")
    father_name=models.CharField(max_length=200,verbose_name="اسم الاب ")
    mather_name=models.CharField(max_length=200,verbose_name="اسم الام ")
    Arabic= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(600)],verbose_name="اللغة العربية ")
    philosophy=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(400)],verbose_name="فلسفة ")
    English= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(400)],verbose_name="اللغة الانكليزية ")
    French= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(400)],verbose_name="اللغة الفرنسية ")
    history= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)],verbose_name="التاريخ ")
    Geography= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)],verbose_name="الجغرافيا ")
    nationalism= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)],verbose_name="التربية القومية ")
    Islamic= models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)],verbose_name="التربية الاسلامية ")
    number=models.IntegerField(validators=[MinValueValidator(0)],verbose_name="رقم الطالب ",unique=True)
    def __str__(self):
        full_name=self.name +" "+ self.father_name +" "+ self.mather_name
        return full_name


Literary_CHOICES=(
        ("اللغة العربية","اللغة العربية"),
        ("فلسفة","فلسفة"),
        ("اللغة الانكليزية","اللغة الانكليزية"),
        ("اللغة الفرنسية","اللغة الفرنسية"),
        ("التاريخ","التاريخ"),
        ("الجغرافيا","الجغرافيا"),
        ("التربية القومية","التربية القومية"),
        ("التربية الاسلامية","التربية الاسلامية")
        )
class ChoiceLiterary(models.Model):
    title=MultiSelectField(choices=Literary_CHOICES,max_choices=3,verbose_name="قائمة المواد ")    
    number=models.IntegerField(validators=[MinValueValidator(0)],verbose_name="رقم الطالب ",unique=True)
    
from django.db import models
jensiat_choice=(("male","مرد"),("female","زن"))
nationality_choice=(("iranian","ایرانی"),("other","غیر ایرانی"))
illness_choice=(("blood pressure","فشار خون"),("diabet","دیابت"))
class mdl_language(models.Model):
    name_lan=models.CharField(verbose_name="نام زبان",max_length=20)
    class Meta:
        verbose_name=u"زبان ها"
        defــstrــ(self):
            return self.name_lan;
class mdl_participant(models.Model):
    mobile=models.CharField(verbose_name="شماره همراه",max_length=20)
    date_enter=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ و ساعت ورود")
    date_exit=models.DateTimeField(verbose_name="تاریخ و ساعت خروج")
    birthday=models.DateField(verbose_name="تاریخ تولد")
    jensiat=models.CharField(max_length=20,verbose_name="جنسیت",choices=jensiat_choice)
    national_number=models.CharField(max_length=10,verbose_name="شماره پاسپورت")
    nationality=models.CharField(max_length=40,verbose_name="ملیت",choices=nationality_choice)
    desc_illness=models.TextField(verbose_name="توضیحات بیماری",max_length=2000)
    illness=models.CharField(verbose_name="بیماری",max_length=40,choices=illness_choice)
    language=models.ManyToManyField(mdl_language,verbose_name="زبان ها")
    num_traveller=models.IntegerField(verbose_name="تعداد همراهان",default=0)
    parent=models.ForeignKey("self",verbose_name="سرپرست",null=True,blank=True,on_delete=models.DO_NOTHING)


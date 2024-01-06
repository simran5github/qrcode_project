from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

import qrcode



# Create your models here.
class Review(models.Model):
    reviewer_name=models.CharField(max_length=50)
    reviewer_mobile=models.IntegerField()
    reviewer_email=models.EmailField(max_length=254)
    reviewer_profile=models.CharField(max_length=100)
    reviewer_message=models.CharField(max_length=500)
    reviewer_review=models.CharField(max_length=500)
    reviewer_country=models.CharField(max_length=50)
    def __str__(self):
        return self.reviewer_email 
    



# Create your models here.

class qr_model(models.Model):
    name = models.CharField(max_length = 200)
    code = models.ImageField(blank=True)


    def save(self,*args,**kwargs):
        qr_image = qrcode.make(self.name)
        qr_offset = Image.new('RGB',(400,400), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream,'PNG')
        self.code.save(files_name, File(stream),save=False)
        qr_offset.close()
        super().save(*args,*kwargs)


# class qr_user_history(models.Model):
#     history_qr=models.ForeignKey(User, on_delete=models.CASCADE)
#     qname = models.CharField(max_length = 200)
#     qcode = models.ImageField(blank=True)


#     def save(self,*args,**kwargs):
#         qr_image = qrcode.make(self.name)
#         qr_offset = Image.new('RGB',(400,400), 'white')
#         qr_offset.paste(qr_image)
#         files_name = f'{self.id}qr.png'
#         stream = BytesIO()
#         qr_offset.save(stream,'PNG')
#         self.code.save(files_name, File(stream),save=False)
#         qr_offset.close()
#         super().save(*args,*kwargs)


class qr_model_auth(models.Model):
    name = models.CharField(max_length = 200)
    code = models.ImageField(upload_to='qrcodes',blank=True) 
    user = models.ForeignKey(User, related_name='ok' ,on_delete=models.CASCADE)
    dob=models.DateTimeField(auto_now=False, auto_now_add=True,blank=True)

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.name)
        qr_offset = Image.new('RGB',(400,400), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.code.save(files_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args,*kwargs)

    
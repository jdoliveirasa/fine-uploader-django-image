from django.db import models
from django.core.files import File
from urllib import request
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage

def content_file_name(instance, filename):
    '''
    upload_dir = os.path.join('uploads',instance.albumname)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)
    '''
    return 'meu_novo_nome'

class Post(models.Model):
	conteudo = models.CharField(max_length=255, null=True)

class Item(models.Model):
	image_csrfmiddlewaretoken = models.CharField(max_length=255, null=True)
	image_uuid = models.CharField(max_length=255, null=True)
	'''
	image_file = models.ImageField(upload_to='media/' + settings.TEMP_FINE_UPLOADER)
	'''
	image_file = models.ImageField(
		upload_to=lambda instance, filename: settings.TEMP_FINE_UPLOADER + '{0}/{1}'.format(instance.image_uuid, filename))
	image_url = models.URLField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post', null=True)
	'''	
    	storage=FileSystemStorage(
    	location=settings.IMAGE_FILES_PATH,
    	base_url=os.path.join(settings.MEDIA_URL, settings.TEMP_FINE_UPLOADER)
    ))
    '''


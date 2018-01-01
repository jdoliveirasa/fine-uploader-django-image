from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Item, Post
from .forms import UploadFileForm
import shutil  	
from django.conf import settings 
import os
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, Template
from django.template.response import TemplateResponse


# Create your views here.
def home(request):
	#return HttpResponse('Hello World')
	#return render(request, 'home.html', {'usuario': 'Fulano de Tal'})
	return render(request, 'home.html')

def contact(request):
	return render(request, 'contact.html')	

def fileupload(request):
	return render(request, 'fileupload.html')	

def fineupload(request):
	return render(request, 'fineupload.html')	

def post(request):
	i = Item.objects.filter(image_csrfmiddlewaretoken=request.POST['csrfmiddlewaretoken'])
	if i is not None:
		post = Post(conteudo=request.POST['conteudo'])
		post.save()
		i.update(post=post)
	else:
		post = Post(conteudo=request.POST['conteudo'])
		post.save()

	#import pdb
	#pdb.set_trace()

	return TemplateResponse(request, 'post.html', {'post': post, 'itens': i})

def uploads(request):
	if request.method == 'POST':
		#import pdb
		#pdb.set_trace()
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			i = Item(image_csrfmiddlewaretoken=request.POST['csrfmiddlewaretoken'],
				image_uuid=request.POST['qquuid'], 
				image_url=request.POST['qqfilename'], 
				image_file=request.FILES['qqfile'])
			i.save()
			data = {"success":True}
			return JsonResponse(data)				

@csrf_exempt
def uploadsdelete(request, uuid):
	if request.method == 'DELETE':
		i = Item.objects.filter(image_uuid=uuid).first()		
		if i is not None:
			path = 'media/' + settings.TEMP_FINE_UPLOADER + i.image_uuid
			if os.path.exists(path):
				shutil.rmtree(path)
			i.delete()
			#import pdb
			#pdb.set_trace()
	return JsonResponse({})
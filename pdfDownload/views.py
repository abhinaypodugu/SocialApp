from re import template
from .models import textBox, Image
from django.views.generic import TemplateView
import os
from django.http import HttpResponse
from django.shortcuts import redirect, render
import mimetypes
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import textForms, ImageForm
from django.views.decorators.http import require_POST
# Create your views here.


@login_required
def download_file(request):
    # fill these variables with real values
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Get_Started_With_Smallpdf.pdf'
    fl_path = os.getcwd() + '\\social\\static\\docs\\' + filename

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


class Index(TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        form = textForms()
        context['textList'] = textBox.objects.order_by('id')
        context['form'] = form
        imgForm = ImageForm()
        context['imgList'] = Image.objects.order_by('id')
        # print(context['imgList'][0].image)
        context['imgForm'] = imgForm
        return context

# @login_required
@require_POST
def addText(request):

    form = textForms(request.POST)
    
    if form.is_valid():
        new_text = textBox(text=request.POST['text'])
        new_text.save()

    return redirect('home')

# @login_required
def deleteText(request, text_id):

    text = textBox.objects.filter(id=text_id).delete()

    return redirect('home')

@require_POST
def addImg(request):

    imgForm = ImageForm(request.POST or None, request.FILES or None)
    print(request.POST, request.FILES)
    if imgForm.is_valid():
        newObj = Image(image=request.FILES['image'], imgText=request.POST['imgText'])
        newObj.save()

    return redirect('home')


def deleteImg(request, img_id):

    image = Image.objects.filter(id=img_id).delete()

    return redirect('home')

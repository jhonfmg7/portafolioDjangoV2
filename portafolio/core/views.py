from django.core.mail import EmailMessage
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import ContactForm

# Create your views here.

def index(request):
    images = Image.objects.all().order_by("?")
    instagram = Instagram.objects.all()
    tags = Tag.objects.all().order_by('-created')
    services = Service.objects.all()
    return render(request, 'core/index.html', {'images': images, 'tags': tags, 'services': services})

def about(request):
    abilities = Ability.objects.all()
    chooses = Choose.objects.all()
    video = Video.objects.first()
    team = Team.objects.all()
    instagram = Instagram.objects.all()
    video_2 = Video_2.objects.first()
    return render(request, 'core/about.html', {'abilities': abilities, 'video': video, 'chooses': chooses, 'team': team, 'video_2': video_2})

def projects(request):
    projects = Project.objects.all()
    if request.GET:
        if request.GET['select'] == 'date':
            projects = Project.objects.all().order_by('-date_end')
        if request.GET['select'] == 'relevance':
            projects = Project.objects.all().order_by('-relevance')
    return render(request, 'core/projects.html', {'projects': projects})

def career(request):
    careers = Career.objects.all()
    return render(request, 'core/career.html', {'careers': careers})

def contact(request):
    contact_form = ContactForm()
    contacts = Contact.objects.all()
    instagram = Instagram.objects.all()
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if name != '' and email != '' and message != '':
            try:
                email = EmailMessage('Mensaje de {}'.format(email), 'Mensaje: {}. \n Remitente: {}'.format(message, name) , to=['jfmarmolg@gmail.com', email])
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse('success')) 
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    return render(request, 'core/contact.html')

def success(request):
    return render(request, 'core/success.html')

def discovery(request):
    return render(request, 'core/discovery.html', {})
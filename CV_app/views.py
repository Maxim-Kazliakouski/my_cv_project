from django.shortcuts import render

# Create your views here.

def main_layout(request):
    return render (request, 'CV_app/main_layout.html')


def about_me(request):
    return render (request, 'CV_app/about_me.html')


def person_page(request):
    return render (request, 'CV_app/personal_info.html')

def work(request):
    return render (request, 'CV_app/work_expirience.html')

def edu(request):
    return render (request, 'CV_app/education.html')

def lang(request):
    return render (request, 'CV_app/languages.html')

def skills(request):
    return render (request, 'CV_app/skills.html')

def cert(request):
    return render (request, 'CV_app/certificates.html')

def hob(request):
    return render (request, 'CV_app/hobbies.html')

def per_inf_skype(request):
    return render (request, 'CV_app/personal_info_skype.html')    

def per_inf_phone(request):
    return render (request, 'CV_app/personal_info_phone.html')

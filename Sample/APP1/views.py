from django.shortcuts import render

# Create your views here.
def BlockToInline(request):
    return render(request, 'BlockToInline.html')
def CSSBoxModel(request):
    return render(request, 'CSSBoxModel.html')
def Forms(request):
    return render(request, 'Forms.html')
def RegistrationPage(request):
    return render(request, 'RegistrationPage.html')
def StudentForms(request):
    return render(request, 'StudentForms.html')
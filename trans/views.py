from django.shortcuts import render,HttpResponse
from translate import Translator



def home(request):
    if request.method=='POST':
        text=request.POST["translate"]
        lang=request.POST['language']
        translate=Translator(to_lang=lang)
        translation=translate.translate(text)
        return render(request,'text.html',{"trans":translation})
    return render(request,'index.html')
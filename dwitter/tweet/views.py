from django.shortcuts import render

# Create your views here.

def index(request):
    return render( request, "index.html")

# sirf index.html isliye likha h kyuki settings m TEMPLATES m DIRS m specify h ki 'templates' wale folder m hi dhunna h 
# however agr 'templates' folder ke andr bhi ek folder hota 'tweet' then it shudve been like:
# return render( request, "tweet/index.html")
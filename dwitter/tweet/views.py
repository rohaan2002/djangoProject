from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.

def index(request):
    return render( request, "index.html")

# sirf index.html isliye likha h kyuki settings m TEMPLATES m DIRS m specify h ki 'templates' wale folder m hi dhunna h 
# however agr 'templates' folder ke andr bhi ek folder hota 'tweet' then it shudve been like:
# return render( request, "tweet/index.html")


def tweet_list(request):
    tweets= Tweet.objects.all().order_by("-created_at")
    return render (request, "tweet_list.html", {"tweets": tweets})

@login_required #decorator predefined rhte, login_required lgane se ensure hota well, login required h before u access this view
def create_tweet(request):
    if (request.method =="POST"):
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet= form.save(commit=False)
            tweet.user = request.user #tweet ka ek attribute "user" bnadere h jo request.user (authenticated user) ko hold krega
            tweet.save()
            return redirect("tweet_list") # note that in POST case the data is coming from the empty form i.e, GET req se empty form show hua (niche handle kia h) after that usee bhrke POST req generate hua.
        # ab ye post req ek TweetForm ka instance bna leta h with filled data, or usko Database m save krdeta h (acc to form fields - thats what saving the form means here)
        # then redirect("tweet_list") happens and so in POST case the "form " is not returned or any html file donot render that filled form
    else:
        form = TweetForm()  #empty form for get request
    return render(request, "tweet_form.html", {"form": form})
    
@login_required      
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk= tweet_id, user= request.user)
    if (request.method=="POST"):
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if(form.is_valid()):
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")

    else:
        form = TweetForm(instance= tweet)
    return render( request, "tweet_form.html", {"form": form})

@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if(request.method=="POST"):
        tweet.delete()
        return redirect("tweet_list")
    else:
        return render(request, "confirm_tweet_delete.html", {'tweet': tweet})


# note that 'request' is an instance of HttpRequest in django, it has many attributes including "user", which is the current authenticated user,
# if no user is authenticated then it reverts to an instance of anonymousUser


# form.cleaned_data returns a dictionary of validated form input fields and their values, where string primary keys are returned as objects.

# form.data returns a dictionary of un-validated form input fields and their values in string format (i.e. not objects).

# ALWAYS USE form.clean_data when u want to extract data easily using '.get' then field name or simply ['fieldname]

def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if(form.is_valid):
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request,user)
            return redirect("tweet_list")
    else:
        form = UserRegistrationForm()
        return render(request, "registration/register.html", {'form': form})
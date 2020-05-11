from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print("TEST", args, kwargs)
    print("TEST2", request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me",
        "my_number": 123,
        "my_list": [123, 4242, 12313, "ABC"]
    }
    return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

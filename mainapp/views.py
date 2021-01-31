from django.shortcuts import render


def main(request):
    return render(request, "mainapp/index.html")


def blog(request):
    return render(request, "mainapp/blog.html")


def text(request):
    return render(request, "mainapp/text.html")

def text2(request):
    return render(request, "mainapp/text-2.html")
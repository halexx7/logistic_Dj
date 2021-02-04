import datetime
from django.shortcuts import render
import json


def load_data(dir):
    ''' Загружаем данные из файла JSON'''
    with open( dir, 'r', encoding='utf-8') as result:
        data = json.load(result)
    return data


def main(request):
    title = "home"

    services = load_data('mainapp/data/services.json')
    news = load_data('mainapp/data/news.json')

    reviews = [
        {"name": 'MIchel Fox', "company": "FOX Hub CEO", "photo": "https://placehold.it/100", "alt": "Photo client", "content_1": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Numquam veritatis ab consectetur aliquam corporis sequi dolore maxime eaque magnam! Laborum eligendi necessitatibus porro officia, dicta deserunt commodi! Vel, nisi, aspernatur!",  "content_2": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Numquam veritatis ab consectetur aliquam corporis sequi dolore maxime eaque magnam! Laborum eligendi necessitatibus porro officia, dicta deserunt commodi! Vel, nisi, aspernatur!"},
        {"name": 'John Smith', "company": "GIT Hub", "photo": "https://placehold.it/100", "alt": "Photo client", "content_1": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Numquam veritatis ab consectetur aliquam corporis sequi dolore maxime eaque magnam! Laborum eligendi necessitatibus porro officia, dicta deserunt commodi! Vel, nisi, aspernatur!",  "content_2": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Numquam veritatis ab consectetur aliquam corporis sequi dolore maxime eaque magnam! Laborum eligendi necessitatibus porro officia, dicta deserunt commodi! Vel, nisi, aspernatur!"},
    ]
    benefits_list = [
        {"name": "Safety", "desc": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod"},
        {"name": "High quality drivers", "desc": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod"},
        {"name": "Guarantee &amp; Support 24/7", "desc": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod"},
        {"name": "Personal manager", "desc": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod"},
    ]
    team = [
        {"name": "John Smith", "profession": "Logistic manager - 8 years experience", "photo": "/static/img/team/team1.jpg", "alt": "John Smith", "email": "john@centerlogistic.com", "phone": "+987412512543"},
        {"name": "Daniel Kore", "profession": "Software engineer", "photo": "/static/img/team/team2.jpg", "alt": "Daniel Kore", "email": "daniel@centerlogistic.com", "phone": "+987423252253"},
        {"name": "Anna Filler", "profession": "Marketing specialist - 10 years experience", "photo": "static/img/team/team3.jpg", "alt": "Anna Filler", "email": "anna@centerlogistic.com", "phone": "+98735353456"},
    ]
    content = {
        "title": title, 
        "services": services, 
        "reviews": reviews,
        "benefits_list": benefits_list,
        "team": team,
        "news": news,
        }
    return render(request, "mainapp/index.html", content)


def blog(request):
    title = "blog"

    news = load_data('mainapp/data/news.json')

    content = {
        "title": title, 
        "news": news,
        }
    return render(request, "mainapp/blog.html", content)


def text(request):
    title = "Privacy Policy"
    content = {"title": title}
    return render(request, "mainapp/text.html", content)


def text2(request):
    title = "Terms & Conditions"
    content = {"title": title}
    return render(request, "mainapp/text-2.html", content)


def services(request):
    title = "Terms & Conditions"
    links_menu = [
        {"href": "services", "name": "Ground"},
        {"href": "services_railway", "name": "Railway"},
        {"href": "services_water", "name": "Water"},
        {"href": "services_air", "name": "Air"}
    ]
    services = [
        {
            "name": "Gazel NEXT",
            "lifting": "5 tons",
            "services_img": "/static/img/services/gazel.jpg",
            "services_alt": "Gazel",
            "desc": "The reliability of the vehicle has been tested and confirmed by bench, forced and long-term road tests using special methods",
        },
        {
            "name": "Volvo FE350",
            "lifting": "10 tons",
            "services_img": "/static/img/services/volvo_5.jpg",
            "services_alt": "Volvo - 5tonn",
            "desc": "The new generation of Volvo FL distribution trucks for intercity and short regional transport road tests using special methods",
        },
        {
            "name": "Volvo FH550",
            "lifting": "40 tons",
            "services_img": "/static/img/services/volvo_10.jpg",
            "desc": "New generation features offered in the FH versions and the flagship FH16: a completely new, more spacious and comfortable",
        },
    ]

    content = {
        "title": title,
        "links_menu": links_menu, 
        "services": services,
        }
    return render(request, "mainapp/services.html", content)


def contact(request):
    title = "contacts"
    visit_date = datetime.datetime.now()
    contacts = load_data('mainapp/data/contact.json')
    content = {
        "title": title,
        "visit_date": visit_date,
        "contacts": contacts,
        }
    return render(request, "mainapp/contact.html", content)

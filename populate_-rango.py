#/usr/bin/python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
        'tango_with_django.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
            {"title": "Office Python Tutorial",
                "url": "http://docs.python.org/2/tutorial/", "views":1200},
            {"title": "How to think like a Computer Scientist",
                "url": "http://www.greenteapress.com/thinkpython/", "views":3456},
            {"title": "Learn Python in 10 Minutes",
                "url":"http://www.korokithakis.net/tutorials/python/", "views":4534} ]

    django_pages = [
            {"title": "Official Django Tutorial",
                "url":"http://docs.djangoproject.com/en/1.9/intro/tutorial01/", "views":4322},
            {"title":"Django Rocks",
                "url":"http://www.djangorocks.com/", "views":3254},
            {"title":"How to Tango with Django",
                "url":"http://www.tangowithdjango.com/", "views":65464} ]

    other_pages = [
            {"title":"Bottle",
                "url":"http://bottlepy.org/docs/dev/", "views":3432},
            {"title":"Flask",
                "url":"http://flask.pocoo.org", "views":3424} ]
    cats = {"Python": {"pages": python_pages, "views":0, "likes": 64},
            "Django": {"pages": django_pages, "views":0,  "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views":0, "likes": 32} }
    
    for page in python_pages:
        cats["Python"]["views"]+=page["views"]
    for page in django_pages:
        cats["Django"]["views"]+=page["views"]
    for page in other_pages:
        cats["Other Frameworks"]["views"]+=page["views"]


    for cat,cat_data in cats.items():
        c=add_cat(cat,cat_data["views"],cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c,p["title"],p["url"],p["views"])
           
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1} - {2}".format(str(c),str(p),p.views))

def add_page(cat,title,url,views=0):
    p=Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,views,likes):
    c=Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

if __name__ == "__main__":
    print("Starting Rango population script...")
    populate()


# django-vue-graphql-celery
This is a sample project demostrating the use of Django, Vuejs, Graphql, Celery, Redis to asychronously process huge job of loading file into the database.

Steps: 
1. Goto https://github.com/abhishekzgithub/django-vue-graphql-celery

2. Clone the repo: https://github.com/abhishekzgithub/django-vue-graphql-celery.git
3. cd productimporter
4. pip install pipenv && pipenv shell : this will install pipenv and create a virtual environment.
5. pipenv install : this will install all the dependency packages
6. python manage.py makemigrations && python manage.py migrate && python manage.py runserver
7. celery -A productimporter worker -l info -P eventlet
8. celery -A productimporter beat -l info
. open the localhost:8000 on your browser
. Look for the urls

. Sample graphql queries which may be used via http://127.0.0.1:8000/graphql/:
    for filtering->
    """
    query{
    products(find:"{'name':'Bryce Jones'}")
    {
        name
        sku
        description
    }
    }
    """
    for searching->
    """
    query{
        products(search:"Bry"){
            name
            sku
        }
        }
    """
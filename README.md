# DJango Front Controller TicketsApp

Archivo .env:

    # .env
    X_AUTH_FILE_SERVICE=dXNlci1zdGlja3lfc2VjcmV0XzEyMzQ1Njc
    URL_FILE_SERVICE=http://localhost:9292/
    BASE_URL=http://localhost:8000/
    STATIC_URL=http://localhost:8000/static/
    STATIC_ENV=development

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate

Variables de entorno:

    # .env
    # file service
    X_AUTH_FILE_SERVICE=dXNlci1zdGlja3lfc2VjcmV0XzEyMzQ1Njc
    URL_FILE_SERVICE=http://localhost:8090/
    # access service
    X_AUTH_ACCESS_SERVICE=dXNlci1zdGlja3lfc2VjcmV0XzEyMzQ1Njc
    URL_ACCESS_SERVICE=http://localhost:8080/
    # tickets service
    X_AUTH_ACCESS_SERVICE=dXNlci1zdGlja3lfc2VjcmV0XzEyMzQ1Njc
    URL_ACCESS_SERVICE=http://localhost:9292/
    # app constants
    BASE_URL=http://localhost:8000/
    STATIC_URL=http://localhost:8001/
    STATIC_ENV=development

Arrancar aplicación con servidor Werkzeug:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

Ejectuar servidor:

    $ python manage.py runserver
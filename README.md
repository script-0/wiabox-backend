# Wiabox-backend
A REST api written in Django for Wiabox Project

## Technologies used
* Python 3.7.5
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs

## Preview
I definitely proscratined on it

## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip3 install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/script-0/wiabox-backend.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd wiabox-backend
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip3 install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python3 manage.py makemigrations
            $ python3 manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python3 manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/
    ```

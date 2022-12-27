# ToDo_App [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
A Simple ToDo Web Application using Django Framework
--------------------------------------------------------
### Features
* This `todo app` is designed using function based views in `django`.
* User can perform basic operations like.
  * Create, Edit, Update, Delete Tasks.
  * Can mark and view tasks as Completed/Incomplete
* User Authentication
  * Multi-User login.
  * Register, Login, Logout.
  * Edit User profile.
  * Change Password.
----------------------------------------------------
### Steps to follow for first time use open terminal/command prompt and execute this below commands.

1. Create a virtual environment.
~~~
   py -m venv env
~~~
2. Activate virtual environment.
~~~
   .\env\Scripts\activate
~~~
3. Install all the dependencies
~~~
   pip install -r requirements.txt
~~~
4. This will convert model class into sql statements.
~~~
   python manage.py makemigrations
~~~
5.  To execute sql statements generated by make migrations. This will create the tables in the Database. 
~~~
   python manage.py migrate
~~~
6. Create an admin user for admin panel.
~~~
   python manage.py createsuperuser
~~~
--------------------------------------------------
Preview.

[ToDo_Web_App.webm](https://user-images.githubusercontent.com/64123078/209545137-2059e2bf-2be8-404d-8a6e-4fa3c3a916da.webm)



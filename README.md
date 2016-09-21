# ProfilePic
Django, AngularJS profile picture upload application with user authentication.

Technology used for this app development are Django, python, AngularJS, bootstrap, postgresql. 
This app is tested in windows environment.
To use this app, some of the following tools need to be installed on your machine

1. Install python 3.5. You can download it from here https://www.python.org/downloads/
2. Install Django 1.10. use the command "pip install django==1.10"
3. The database used for this applicaiton is Postgres 9.5. Download and install postgres.
4. After installing postgres, run this command in cmd "pip install psycopg2"
5. Unzip the downloaded zip file in your workspace. Rename the project root folder from "ProfilePic-master" to "ProfilePic". Recommended to put it in the "C:\Python35" folder.
6. Open PgAdmin III and login. Create a database "ProfilePicDB". You can use any other database name but, make sure to change it in the settings.py file.
7. Update the database username and password with you database credentials in settings.py file.
8. Once database is created and settings updated, run migrations. Go to your project directory in cmd "ProfilePic" i.e., (C:\Python35\ProfilePic).
9. Run the following two commands
  "python manage.py makemigrations ProfilePicApp" and
  "python manage.py migrate"
10. You should now see the tables created in you database.
11. Run the server with the command "python manage.py runserver"
12. Go to "http://127.0.0.1:8000" in your browser and you should be able to see the app running.

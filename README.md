# url_shortener
## 1. Install python, VS code editor
## Command for start the url shortener:
### 1. Create and activate the virtual enviornemnt ( Optional but reccomended) 
#### python -m venv your_env_name
#### your_env_name\Scripts\activate
### 2.Install the requirement.txt
#### pip install -r requirements.txt
### 3. Create Django project and app ( Already done, No need to do it explicitly )
#### django-admin startproject urlshortener
#### django-admin startapp shortener
### 4. Start the mongo server
### 5. Start the django project ( You must be in the url_shortener directory, in which manage.py file is located)
#### python manage.py runserver
### 5.1 Optional, You can view the api's end point using the postman.
### 6. Create a new window and Start the front end ( 8001 is the port number, you can choose something else also)
#### python -m http.server 8001 
#### The front end is available at https://localhost:8001/
## Advice: Open inspect element in chrome, to debug if any error came, instead of copying and paste Think Logical. 
# GOOD LUCK


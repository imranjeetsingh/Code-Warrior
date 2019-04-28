
# Code Warrior

An online judge that supports the following languages:  
- C
- C++
- Python 2
- Python 3


### Tools Used

- **Python** - Django
- **Javascript**
- **Bootstrap**


### Third Party Services Used

- **Amazon Web Services (AWS)**: Stores all static and media files.
- **Heroku**: Used to deploy the project in production environment.
- **sendgrid**: Used to send transactional emails like email-id verification.


## Instructions for setting up the project

1. Clone the repository  
`git clone https://github.com/morphosis-nitmz/Code-Warrior`

2. Rename the file **.env-sample** to **.env** and replace the value of `SECRET_KEY` with the secret key of your own project. To generate a new secret key
	- Go to terminal and create a new django project `django-admin startproject <proj-name>`.
	- Now get the value of `SECRET_KEY` in *settings.py* and use that as the secret key for the **Stock-Bridge project**.
	- Now delete that new django project.

3. **Sendgrid setup**:
	- Create an account on [sendgrid](https://sendgrid.com/).
	- Add your sendgrid username and password to `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` in **credentials.py** respectively.
	- Change the email and name in `DEFAULT_FROM_EMAIL` and `MANAGERS` in all *settings files* with your name and email.

4. **Amazon Web Services (AWS) setup**:  
	Create and setup the IAM User and bucket in AWS, then add all the required values to **credentials.py**

5. **Heroku setup**:  
	Follow this guide to setup Heroku in the project: [Heroku Setup](notes/heroku_setup.md).

6. Run the following commands  
`python manage.py makemigrations`  
`python manage.py migrate`  
`python manage.py collectstatic`

7. Now load the **questions**, **test cases** and **expected outputs** into the database  
`python manage.py loaddata questions/fixtures/questions.json`

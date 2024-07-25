# Agent Service

Web application for football agents to view various information about players on the market, and about transactions made by other clubs and agents

## Check it out!

[Agent Manager App](https://agent-service-jd32.onrender.com/)
<br>
(You would need to wait for ~1 minute for the server to wake up)

<i>If you don't want to register you can use the following credentials:</i>

* <i>Login: admin</i>
* <i>Password: admin2509</i>

## Installing locally / Getting started

Python3 must be already installed

```shell
git clone https://github.com/BohdanKuzik/agent-account.git
cd agent-account
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
```
Install dependencies
```shell
pip install -r requirements.txt
```
Setting Up Environment Variables
This project requires certain environment variables to be set. A .env.template file has been provided to help you get started.
Steps:
1) Copy the .env.template file to .env:
```shell
cp .env.template .env
```
2) Open the .env file and fill in the required values:
```shell
set DJANGO_SECRET_KEY=your_secret_key_here
set DJANGO_DEBUG=False
set DATABASE_URL=postgresql://agentdb_owner:w5gOuPfUj1Ex@ep-nameless-limit-a29axxol.eu-central-1.aws.neon.tech/agentdb?sslmode=require
```
Replace your_secret_key_here with a secure, randomly generated secret key. You can generate one using the following command in a Python shell:
```shell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```


Migrate the database, generate initial data and run server
```shell
python manage.py migrate
python manage.py generator_data
python manage.py runserver
```

After running that code you'll be able to browse the website locally on your computer.

### Features

* Authentication functionality for Agent/User
* Managing transfers and players from the presented interface
* Creating, deleting and editing different data
* Searching players in app
* Admin panel for advanced DB management

## Demo
![Website Interface](demo.png)
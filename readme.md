# Zen Discipline Platform

## Local Development Setup

### Requirements
- Python 3.6+ (Tested with Python 3.9.1)
- mysqlclient

#### Verify python version
```shell
python --version
# `python` may point to a 2.x version of python.  If that's the case, try:
python3 --version
```

### Basics
```shell
git clone git@github.com:tylerseymour/zendiscipline.git 
cd zendiscipline
python -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Create and set up database
Create database in MySQL and populate the DB_HOST, DB_USERNAME, etc values in the `.env` file.

### Generate a secret key
```shell
cd scripts
python generate_secret_key.py
```
Copy the value that is output to your `.env` file, as the SECRET_KEY setting.  It should look like:
`SECRET_KEY="qs%1-)8m+tl39xtt@wl3$xy3v&!y1nw6q%e7kx-%7$$!m*%b-#"`

### Run Migrations
```shell
python manage.py migrate
```

### Running the Server

Execute the following and visit http://127.0.0.1:8000

```shell
# From the root of the project directory
source venv/bin/activate
python manage.py runserver
```

### Updating requirements

If you update requirements for the project via `pip install`, please run the following to update the requirements file.

```shell
pip freeze > requiremnts.txt
```

# Front End
```shell
cd zendiscipline
npm install
npm run dev
```




### Source Materials for setting up this project

- https://github.com/alonronin/react-tailwind-webpack5-boilerplate

#### Front end
- Create React App
- Then https://tailwindcss.com/docs/guides/create-react-app
- This requires use of CRACO https://github.com/gsoft-inc/craco

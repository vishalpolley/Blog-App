# Blog App

This is a blog application build on Django Framework.

## Set Up

* It is recommended to use a virtual environment for running the project (e.g. virtualenv), execute following commands on terminal
```
pip install virtualenv
virtualenv -p python3 env
```

* Now navigate inside the `env` folder
```
cd env/
```

* Now start the virtual environment by executing following commands in terminal
```
source bin/activate
```

* Now clone/download the repo inside the `env` folder [Click](https://github.com/vishalpolley/Blog-App/archive/master.zip)
```
git clone https://github.com/vishalpolley/Blog-App.git
```

* Navigate inside the repository folder
```
cd Blog-App/
```

* Now install the required python packages by using the following commands in terminal
```
sudo pip install -r requirements.txt
```

* Navigate inside the src folder.
```
cd src/
```

* Create a superuser by using following command
```
python manage.py createsuperuser
```

* Now run the Django server by using
```
python manage.py runserver
```

* Navigate to page and enter the URL
```
http://localhost:8000/
```

![screenshot from 2019-01-10 22-26-51](https://user-images.githubusercontent.com/20622980/50986241-50367000-152c-11e9-875d-481f1d20fbbc.png)

## Application Structure

The blog application contains two major application components -

* **Account Application** - (contains user login, register, logout functions)
* **Posts Application** - (contains post create, list, detail, update, delete functions)

## Account Application

The account application uses the Default Django User model.

The functionality of various components of account application are explained as follows -

### User Register View

The user registration view/form contains following three parameters -

* `username` - required field, unique
* `email` - required field
* `password` - required field

![screenshot from 2019-01-10 22-27-55](https://user-images.githubusercontent.com/20622980/50987271-2df22180-152f-11e9-86da-22145d06f0be.png)

* The Register form checks for any validation errors and on success redirects to the post main page
```
http://localhost:8000/posts/
```

### User Login View

The user login view contains following two parameters -

* `username` - required field, unique
* `password` - required field

![screenshot from 2019-01-10 22-27-52](https://user-images.githubusercontent.com/20622980/50987020-66453000-152e-11e9-9ba3-4c00f4f387ff.png)

* The Login form checks for any validations errors and on successful login, the page redirects to the main page.
```
http://localhost:8000/posts/
```

### User Logout View

The current login user can logout from the application by clicking on `logout` option on the navigation bar of the blog application.

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

* `username` - char field, required field, unique
* `email` - email field, required field
* `password` - password field, required field

```
http://localhost:8000/register/
```

![screenshot from 2019-01-10 22-27-55](https://user-images.githubusercontent.com/20622980/50987271-2df22180-152f-11e9-86da-22145d06f0be.png)

* The Register form checks for any validation errors and on success redirects to the post main page
```
http://localhost:8000/posts/
```

### User Login View

The user login view contains following two parameters -

* `username` - char field, required field, unique
* `password` - password field, required field

```
http://localhost:8000/login/
```

![screenshot from 2019-01-10 22-27-52](https://user-images.githubusercontent.com/20622980/50987020-66453000-152e-11e9-9ba3-4c00f4f387ff.png)

* The Login form checks for any validations errors and on successful login, the page redirects to the main page.
```
http://localhost:8000/posts/
```

### User Logout View

The current login user can logout from the application by clicking on `logout` option on the navigation bar of the blog application.
```
http://localhost:8000/logout/
```

## Post Application

The post application provides various functionality of post creation, updation, deletion which are explained as below -

### Post Creation View

The post creation view/form contains following parameters as -

* `title` - char field, required field
* `content` - text field, required field
* `image` - image field, non required field

```
http://localhost:8000/posts/create/
```

![screenshot from 2019-01-10 22-27-25](https://user-images.githubusercontent.com/20622980/50988019-482cff00-1531-11e9-9c8e-0822e0923ea1.png)

* A logged in user can only create a new post. If the user is not logged in, he/she can only view the post contents.

* The post create form also checks for validation errors on various fields.

* On successful creation of the post the page redirects to the main post lists page
```
http://localhost:8000/posts/
```

### Post Update View

The post update view/form contains following parameters as -

* `title` - char field, required field
* `content` - text field, required field
* `image` - image field, non required field

```
http://localhost:8000/posts/id/edit/
```
where `id` is the id of the post.

![screenshot from 2019-01-10 22-27-37](https://user-images.githubusercontent.com/20622980/50988455-adcdbb00-1532-11e9-9a57-fccb2429d677.png)

* Only the creator of the post is able to update his/her post.

* On successful updation of the post the page redirects to the particular post.

### Post List View

The post list view shows various posts by different users in the form of a scrollable list.
```
http://localhost:8000/posts/
```

![screenshot from 2019-01-10 22-27-00](https://user-images.githubusercontent.com/20622980/50989391-3e0cff80-1535-11e9-833e-7cce81de0879.png)

![screenshot from 2019-01-10 22-27-05](https://user-images.githubusercontent.com/20622980/50989403-48c79480-1535-11e9-931c-d229849080dd.png)

* The Post List view contains a `search` field which narrows the search results of the posts for the values of title, content, and username.

* The Post List view contains `pagination` feature which paginates the pages if post contents exceeds **10**.

### Post Delete View

The post delete view provides post deletion feature for the post app.
```
http://localhost:8000/posts/id/delete/
```
where `id` is the id of the post.

* Only the creator of the post is able to delete his/her post.

* On successful deletion of the post, the page redirects to the main page containing all posts.

### Post Detail View

The post detail view shows the contents of the particular post.
```
http://localhost:8000/posts/id/
```
where `id` is the id of the post.

![screenshot from 2019-01-10 22-27-17](https://user-images.githubusercontent.com/20622980/50990077-1f0f6d00-1537-11e9-93ed-20df89c77dbc.png)

* The Post detail view shows option for post `update` and post `delete` for the creator of the post. And for other users the options are disable over that post.

![screenshot from 2019-01-11 00-25-59](https://user-images.githubusercontent.com/20622980/50990252-8f1df300-1537-11e9-80d9-f04e8f1c9ef2.png)

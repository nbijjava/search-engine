To run, first install [Flask](https://flask.palletsprojects.com/en/1.1.x/):

```
pip install flask
```

Next, set the following environment variable:

```
export FLASK_ENV=development
```

Finally, run flask:

```
flask run
```

Visit the URL that is printed in the output to test your app.

To deploy your app, you might consider using [Heroku](https://bia-660-search-demo.herokuapp.com). Once you've created an account, download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). Log in using `heroku login`.

Next, create a new app on Heroku:

```
heroku create
```

Finally, deploy your app:

```
git push heroku master
``` 

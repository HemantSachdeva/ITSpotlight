<div align="center" style="text-align:center">

<img src="./static/assets/favicon.ico" width=200px />

[![GitHub](https://img.shields.io/github/license/HemantSachdeva/ITSpotlight?style=plastic)](https://github.com/HemantSachdeva/ITSpotlight/blob/main/LICENSE.md)
![GitHub repo size](https://img.shields.io/github/repo-size/HemantSachdeva/ITSpotlight?style=plastic)
![Lines of code](https://img.shields.io/tokei/lines/GitHub/HemantSachdeva/ITSpotlight?style=plastic&label=lines%20of%20code)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/HemantSachdeva/ITSpotlight?style=plastic)

</div>

# What is IT Spotlight?

IT Spotlight is a social news website mainly focusing on computer science and for the people who enjoy tinkering with technology. It is based on [Hacker News API](https://hackernews.api-docs.io/).

It is developed using <a href="https://flask.palletsprojects.com/en/2.0.x/">Python-Flask</a> and deployed on <a href="https://heroku.com">Heroku</a>.

# Why IT Spotlight?

[Hacker News](https://news.ycombinator.com/) website is already well-known for tech news but it does not garner many visitors due to its terrible user interface. So I decided to create a better one.

# Dependencies

```
Flask==2.0.3
Flask-Cors==3.0.10
Flask-RESTful==0.3.9
gunicorn==20.1.0
requests==2.27.1
```

# Installation of dependencies

```
pip install -r requirements.txt
```

# Want to run on locally?

- After installing all the dependencies just run the following command in the root direcotry of this cloned repository globally or in a virtual environment:

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

# Want to contribute?

- You can either fork this repository or create a new one.

Do not forget to read the [Contributing Guide](./CONTRIBUTING.md) before you start.

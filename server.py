from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)


@app.route("/")
def home():
  random_number = random.randint(1, 10)
  current_year = date.today().year
  return render_template("index.html", num=random_number, YYYY=current_year)


# makes a request to the website and get its json data with a specific key
def get_data(url, key):
  response = requests.get(url=url)
  data = response.json()
  info = data[key]
  return info


@app.route("/guess/<user_name>")
def guess(user_name):
  username = user_name.title()
  gender_url = f"https://api.genderize.io?name={user_name}"
  gender = get_data(gender_url, "gender")

  age_url = f'https://api.agify.io?name={user_name}'
  age = get_data(age_url, "age")

  return render_template("guess.html", name=username, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
  print(num)
  blog_url = "https://api.npoint.io/4af156202f984d3464c3"
  response = requests.get(blog_url)
  all_post = response.json()
  return render_template("blog.html", posts=all_post)

if __name__ == "__main__":
  app.run(debug=True)




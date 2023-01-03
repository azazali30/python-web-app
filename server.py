from flask import Flask, render_template
from flask import request, redirect
import csv

app = Flask(__name__)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        database.write(f'\n{data["email"]},{data["subject"]},{data["message"]}')


def write_to_csv(data):
    with open('databse.csv', mode='a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data["email"], data["subject"], data["message"]])


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/user/<username>/<int:post_id>")
def hello_user(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


@app.route("/<string:html_page>")
def contact(html_page='index.html'):
    return render_template(html_page)


@app.route("/favicon.ico")
def ico():
    return "images/favicon.ico"


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:

            data = request.form.to_dict()
            email = data['email']
            write_to_csv(data)
            return render_template('/thankyou.html', email=email)
        except:
            return "did not save to database"
    else:
        print('Not a post method')
    return "form submitted"

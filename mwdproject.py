from flask import Flask, render_template, url_for, request
import csv
#render template to use own html, CCS and js
app = Flask(__name__)


#high level of abstraction: decorator- app goves extra roots: to create a function that returns hello world
#
# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)
#
# @app.route('/root')
# def blog():
#     return 'shmøøøøø'
#
# @app.route('/root/smuziz')
# def blog2():
#     return 'Lupi & azizi'

#with flask:uses ginger when using double brackets, tells html to read inside the double brackts as python
#gz is a compressed files

#--------------------------------------------------------------------------------------------------------
#analogue way :)

@app.route('/')
def my_web():
    return render_template('index.html')

@app.route('/templates/components.html')
def components():
    return render_template('components.html')
#----------------------------------------------------
#sending email via contact form

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        write_to_csv(name, email, message) #can also use write to file for txt format
        return 'We thank you for your praise, and will get back to you in case you sent a request'
    else:
        return 'something went wrong'

def write_to_file(name, email, message):
    with open('database.txt', mode ='a') as database:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        file = database.write(f'\n {name}, {email}, {message}')

def write_to_csv(name, email, message):
    with open('database.csv', newline='', mode ='a') as database2:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])

#-------------------Subscriber function------------------

# def news_letter_sub():
#     if request.method == "POST":
#         subscriber = request.form['subscriber']
#         write_to_csv(subscriber) #can also use write to file for txt format
#
#         return 'We thank you for subscribing! Muzi pics incoming :) '
#     else:
#         return 'something went wrong'
#-------------------Subscriber function------------------
# def write_to_csv(subscriber):
#     with open('subscribers.csv', mode ='a') as database3:
#         subscriber = request.form['subscriber']
#         csv_writer = csv.writer(database3, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([subscriber])
#POST vs GET: post ? format in the url, Post send data bakc in data form GEt gets information in url

#automatically accepts the root and renders

# @app.route('/')
# def my_web():
#     return render_template('index.html')
#
# @app.route('/<string:page_name>/<string:page_two>')
# def my_surf(page_two):
#     return render_template(page_two)



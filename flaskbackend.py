from flask import Flask, request, render_template

app = Flask(__name__, template_folder='/home/tara/program/htmlbackend/htmlFls/ceisite')
@app.route('/', methods = ['GET', 'POST'])
def form():
    if request.method == "GET":
        return render_template('meetup.html')
    if request.method == "POST":
        name = request.form.get('Name')
        age = request.form.get('Age')
        edu = request.form.get('Education')
        code = request.form.get('Programming Language')
        email = request.form.get('Email')
        sm = request.form.get('Social Media')
        with open("dbtest.csv", "a") as file:
            file.write(f'{name}, {age}, {edu}, {code}, {email}, {sm}')
        return "Successfully Submitted"
if __name__== '__main__':
    app.run(debug=True)

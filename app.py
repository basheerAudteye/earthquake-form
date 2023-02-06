from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form_data.db'
# db = SQLAlchemy(app)

# class FormData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     message = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f'<FormData {self.name}>'

# db.create_all()





@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    form_data = request.form
    return render_template("dashboard.html", form_data=form_data)


# @app.route("/submit", methods=["POST"])
# def submit():
#     form_data = FormData(
#         name=request.form['name'],
#         email=request.form['email'],
#         message=request.form['message']
#     )
#     db.session.add(form_data)
#     db.session.commit()
#     return render_template("dashboard.html", form_data=form_data)



if __name__ == "__main__":
    app.run()

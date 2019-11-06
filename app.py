#
# Inspired by:  https://pythonspot.com/flask-web-forms/
#


from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = "afafafafafafafafaf"


class ReusableForm(Form):
    name = TextField("Name:", validators=[validators.InputRequired()])
    email = TextField(
        "Email:", validators=[validators.Email(), validators.Length(min=6, max=35)]
    )
    password = TextField(
        "Password:",
        validators=[validators.InputRequired(), validators.Length(min=3, max=35)],
    )

    @app.route("/", methods=["GET", "POST"])
    def hello():
        form = ReusableForm(request.form)

        print(form.errors)
        if request.method == "POST":
            name = request.form.get("name")
            password = request.form.get("password")
            email = request.form.get("email")
            print(name, " ", email, " ", password)

            if form.validate():
                # Save the comment here.
                flash("Thanks for registration " + name)
            else:
                for error_field, error_reason in form.errors.items():
                    print(f"Error: {error_field} {error_reason}")
                    flash(f"Error: {error_field} {error_reason}")

        return render_template("app.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

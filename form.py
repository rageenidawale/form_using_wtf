from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField(label="Password",
                             validators=[DataRequired(), Length(min=8,
                                                                message="Field must be atleast 8 characters long")])
    submit = SubmitField(label="Log In")

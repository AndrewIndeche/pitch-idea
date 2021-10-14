from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

CATEGORY_CHOICES=[('Jokes','Jokes'),('Inspiration','Inspiration'),('Random','Random')]
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    pitch_comment = TextAreaField('Make a comment', validators=[Required()])
    submit = SubmitField('Comment')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Choose a category', choices=CATEGORY_CHOICES, validators=[Required()])
    post = TextAreaField('Your Idea here', validators=[Required()])
    submit = SubmitField('Pitch')

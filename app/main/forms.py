from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

CATEGORY_CHOICES=[('Breakfast','Breakfast'),('Lunch','Lunch'),('Dinner','Dinner')]
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    pitch_comment = TextAreaField('Make a comment', validators=[Required()])
    submit = SubmitField('Comment')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Choose a category', choices=CATEGORY_CHOICES, validators=[Required()])
    pitch_text = TextAreaField('Your ingredients here', validators=[Required()])
    pitch_text = TextAreaField('Your Recipe here', validators=[Required()])
    post = SubmitField('Post')

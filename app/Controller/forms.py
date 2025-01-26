from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import  DataRequired, Length
from wtforms.widgets import ListWidget, CheckboxInput

from app.Model.models import Post, Tag


def returnAllTags():
    return Tag.query.all()
    
def tagName(Tag):
    return Tag.name

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    happiness_level = SelectField('Happiness Level',choices = [(3, 'I can\'t stop smiling'), (2, 'Really happy'), (1,'Happy')])
    tag =  QuerySelectMultipleField('Tag', query_factory=returnAllTags, get_label=tagName, widget=ListWidget(prefix_label=False), 
      option_widget=CheckboxInput())
    submit = SubmitField('Post')
    body = TextAreaField("Post Message", validators=[DataRequired(), Length(min=1, max=1500)])


class SortForm(FlaskForm):
    sort = SelectField('Sort By', choices=[(4, 'Date'),(3, 'Title'),(2, '# of likes'),(1,'Happiness level')])
    my_posts = BooleanField('Display my posts only')
    submit = SubmitField('Refresh')

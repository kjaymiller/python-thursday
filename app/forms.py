from flask.ext.wtf import Form
from wtforms import TextAreaField, FileField
from wtforms import SubmitField

class TextInput(Form):
    description_input = TextAreaField('text_input')
    chat_input = TextAreaField('text_input')
    file_input = FileField('file_input')

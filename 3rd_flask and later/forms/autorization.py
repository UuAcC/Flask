from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    team_leader = IntegerField('Team Leader ID', validators=[DataRequired()])
    job = StringField('Job Title', validators=[DataRequired()])
    work_size = IntegerField('Work size in ours', validators=[DataRequired()])
    collaborations = StringField('Collaborations', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?')

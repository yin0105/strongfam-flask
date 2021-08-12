from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, RadioField, DateField, TextAreaField, \
    HiddenField, DateTimeField, DecimalField, validators
from wtforms_components import SelectField
from wtforms.validators import DataRequired, ValidationError, InputRequired, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired

class ShareMyIdeaForm(FlaskForm):
    class Meta:
        #set to 1 week
        csrf_time_limit = 604800
        
    projname = StringField('Project Name ', validators=[validators.DataRequired(), validators.Length(3, 35)], render_kw={"maxlength": "35"})
    reqamount = DecimalField('Requested Grant Amount ', [validators.DataRequired(), validators.NumberRange(min=0, max=55000)], places=2)
    

    orgname = StringField('Organization Name ', validators=[validators.DataRequired(), validators.Length(3, 40)], render_kw={"maxlength": "40"})
    orgwebaddr = StringField('Organization Web Address ', validators=[validators.DataRequired(), validators.Length(3, 700)], render_kw={"maxlength": "700"})

    schoolname = StringField('School Name ', validators=[validators.Length(0, 35)], render_kw={"maxlength": "35"})
    schoolwebaddr = StringField('School Web Address ', validators=[validators.Length(0, 700)], render_kw={"maxlength": "700"})

    titles = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Ms', 'Ms'),
        ('Dr', 'Dr'),
    ]

    pititle = StringField('Title ', validators=[validators.DataRequired(), validators.Length(1, 3)], render_kw={"maxlength": "3"})
    pifirstname = StringField('First Name ', validators=[validators.DataRequired(), validators.Length(3, 14)], render_kw={"maxlength": "14"})
    pimi = StringField('Middle Initial ', validators=[ validators.optional(), validators.Length(0, 1)], render_kw={"maxlength": "1"})
    pilastname = StringField('Last Name ', validators=[validators.DataRequired(), validators.Length(3, 14)], render_kw={"maxlength": "14"})
    pisuffix = StringField('Name Suffix ', validators=[validators.optional(), validators.Length(0, 3)], render_kw={"maxlength": "3"})    
    picv = StringField('Curriculum Vitae web address ', validators=[validators.optional(), validators.Length(0, 700)], render_kw={"maxlength": "700"})    
    piemail = StringField('Email ', validators=[validators.DataRequired(), validators.Email()], render_kw={"maxlength": "700"})
    pitele = StringField('Telephone ', validators=[validators.DataRequired(), validators.Length(10, 10)], render_kw={"minlength": "10","maxlength": "10"})
    piaddr1 = StringField('Address 1 ', validators=[validators.DataRequired(), validators.Length(3, 30)], render_kw={"maxlength": "30"})
    piaddr2 = StringField('Address 2 ', validators=[validators.optional(), validators.Length(0, 30)], render_kw={"maxlength": "30"})
    picity = StringField('City ', validators=[validators.DataRequired(), validators.Length(3, 20)], render_kw={"maxlength": "20"})    
    pizip = StringField('Zip ', validators=[validators.DataRequired(), validators.Length(5, 5)], render_kw={"maxlength": "5", "minlength": "5"})

    othertitle = StringField('Title ', validators=[validators.Length(0, 3)], render_kw={"maxlength": "3"})
    otherfirstname = StringField('First Name ', validators=[validators.Length(0, 14)], render_kw={"maxlength": "14"})
    othermi = StringField('Middle Initial ', validators=[validators.Length(0, 1)], render_kw={"maxlength": "1"})
    otherlastname = StringField('Last Name ', validators=[validators.Length(0, 14)], render_kw={"maxlength": "14"})
    othersuffix = StringField('Name Suffix ', validators=[validators.Length(0, 3)], render_kw={"maxlength": "3"})
    otheremail = StringField('Email ', validators=[validators.optional(),validators.Email()], render_kw={"maxlength": "700"})
    othertele = StringField('Telephone ', validators=[validators.optional(), validators.Length(10, 10)], render_kw={"minlength": "10","maxlength": "10"})
    otheraddr1 = StringField('Address 1 ', validators=[validators.Length(0, 30)], render_kw={"maxlength": "30"})
    otheraddr2 = StringField('Address 2 ', validators=[validators.Length(0, 30)], render_kw={"maxlength": "30"})
    othercity = StringField('City ', validators=[validators.Length(0, 20)], render_kw={"maxlength": "20"})
    #otherstate = SelectField('State', validators=[validators.optional()], validate_choice=False)
    otherzip = StringField('Zip ', validators=[validators.optional(),validators.Length(5, 5)], render_kw={"maxlength": "5", "minlength": "5"})

    goal = TextAreaField('Research Goal ', validators=[validators.DataRequired(), validators.Length(3, 360)], render_kw={"rows": 3,"maxlength": "360"})
    description = TextAreaField('Project Description ', validators=[validators.DataRequired(), validators.Length(3, 2400)], render_kw={"rows": 3,"maxlength": "2400"})
    aboutpeople = TextAreaField('About the PI and other team members ', validators=[validators.Length(0, 1500)], render_kw={"rows": 3,"maxlength": "1500"})
    relevance = TextAreaField('Relevance of the project ', validators=[validators.DataRequired(), validators.Length(3, 2400)], render_kw={"rows": 3,"maxlength": "2400"})
    dissemination = TextAreaField('Dissemination ', validators=[validators.DataRequired(), validators.Length(3, 900)], render_kw={"rows": 3,"maxlength": "900"})
    projother = TextAreaField('Other Information ', validators=[validators.Length(0, 900)], render_kw={"rows": 3,"maxlength": "900"})

    submit = SubmitField('Submit')

    def validate(self, extra_validators=None):
        if super().validate(extra_validators):

            # your logic here e.g.
            if not (self.picv.data or self.aboutpeople.data):
                self.picv.errors.append('Either the PI’s CV web address or the About the PI… field must have a value.')
                return False
            else:
                return True

        return False


class sendDocumentForm(FlaskForm):
    irsfield = FileField(validators=[FileRequired(),FileAllowed(['pdf','jpg', 'png'])])
    budfield = FileField(validators=[FileRequired(),FileAllowed(['xls','xlsx'])])


class MessageForm(FlaskForm):
    class Meta:
        csrf_time_limit = 604800 
    
    # subject = SelectField('Select a subject', validators=[validators.optional()], validate_choice=False)
    visname = StringField('Name ', validators=[validators.DataRequired(), validators.Length(3, 50)], render_kw={"maxlength": "50"})
    visemail = StringField('Email ', validators=[validators.DataRequired(), validators.Email()], render_kw={"maxlength": "700"})
    message = TextAreaField('Message ', validators=[validators.Length(1, 480)], render_kw={"rows": 3,"maxlength": "480"})    

    submit = SubmitField('Submit')

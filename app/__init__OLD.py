from flask import Flask, request, flash, jsonify, url_for, redirect, Markup
from flask import render_template
from datetime import datetime, date
import time
import re
#import mysql.connector
from flaskext.mysql import MySQL
from app.forms import ShareMyIdeaForm, sendDocumentForm
from werkzeug.utils import secure_filename
import secrets
import os

app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'john1'  
app.config['MYSQL_DATABASE_PASSWORD'] = '1ab45*xy'  
app.config['MYSQL_DATABASE_DB'] = 'pffp'  
app.config['MYSQL_DATABASE_HOST'] = 'mysql.fpproject.dreamhosters.com'  
mysql.init_app(app)

conn = mysql.connect()
crsr = conn.cursor()

query1 = 'select * from projectinfo;'

crsr.execute(query1)
for (
    projname1, projname2, projname3,
    projaddr1, projaddr2, telephonenr, emailaddr,
    leadpixinscr1, leadpixinscr2, leadpixinscr3,
    copyrightmsg1, copyrightmsg2
    ) in crsr:
    projname = projname1 + ' ' + projname2 + ' ' + projname3
    copyrightmsg = copyrightmsg1 + ' ' + projname + '.  ' + copyrightmsg2

query2 = """
    select pagename, paranr, paratypecode, paratext
    from pagetext
    order by pagename, paranr, paratypecode
    ;
    """
# Initialize these variable as 2 dimensional lists:
home_paratextbody = [[]]
home_paratexthead = [[]]
why_paratextbody = [[]]
why_paratexthead = [[]]
scienceconverging_paratextbody = [[]]
scienceconverging_paratexthead = [[]]
earlyyears_paratextbody = [[]]
earlyyears_paratexthead = [[]]
parenting_paratextbody = [[]]
parenting_paratexthead = [[]]
thechallenge_paratextbody = [[]]
thechallenge_paratexthead = [[]]
opportunity_paratextbody = [[]]
opportunity_paratexthead = [[]]
ourwork_paratextbody = [[]]
ourwork_paratexthead = [[]]
history_paratextbody = [[]]
history_paratexthead = [[]]
activities_paratextbody = [[]]
activities_paratexthead = [[]]
joinin_paratextbody = [[]]
joinin_paratexthead = [[]]
results_paratextbody = [[]]
results_paratexthead = [[]]
phase1_paratextbody = [[]]
phase1_paratexthead = [[]]
statestandards_paratextbody = [[]]
statestandards_paratexthead = [[]]
questionnaire_paratextbody = [[]]
questionnaire_paratexthead = [[]]
curriculum_paratextbody = [[]]
curriculum_paratexthead = [[]]
whatlearned_paratextbody = [[]]
whatlearned_paratexthead = [[]]
whyapply_paratextbody = [[]]
whyapply_paratexthead = [[]]
focus_paratextbody = [[]]
focus_paratexthead = [[]]
details_paratextbody = [[]]
details_paratexthead = [[]]
whatexpect_paratextbody = [[]]
whatexpect_paratexthead = [[]]
goal_paratextbody = [[]]
goal_paratexthead = [[]]
thankyou_paratextbody = [[]]
thankyou_paratexthead = [[]]
board_paratextbody = [[]]
board_paratexthead = [[]]
references_paratextbody = [[]]
references_paratexthead = [[]]
contactus_paratextbody = [[]]
contactus_paratexthead = [[]]
terms_paratextbody = [[]]
terms_paratexthead = [[]]
footer_paratextbody = [[]]
footer_paratexthead = [[]]

crsr.execute(query2)
for (pagename, paranr, paratypecode, paratext) in crsr:
    if pagename == 'home':  # Must do a separate section for EACH page.
        if paratypecode == 'head':
            home_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            home_paratextbody.append(paratext)
    elif pagename == 'why':  # Must do a separate section for EACH page.
        if paratypecode == 'head':
            why_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            why_paratextbody.append(paratext)
    elif pagename == 'scienceconverging':  # Must do a separate section for EACH page.
        if paratypecode == 'head':
            scienceconverging_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            scienceconverging_paratextbody.append(paratext)
    elif pagename == 'earlyyears':
        if paratypecode == 'head':
            earlyyears_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            earlyyears_paratextbody.append(paratext)
    elif pagename == 'parenting':
        if paratypecode == 'head':
            parenting_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            parenting_paratextbody.append(paratext)
    elif pagename == 'thechallenge':
        if paratypecode == 'head':
            thechallenge_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            thechallenge_paratextbody.append(paratext)
    elif pagename == 'opportunity':
        if paratypecode == 'head':
            opportunity_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            opportunity_paratextbody.append(paratext)
    elif pagename == 'ourwork':
        if paratypecode == 'head':
            ourwork_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            ourwork_paratextbody.append(paratext)
    elif pagename == 'history':
        if paratypecode == 'head':
            history_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            history_paratextbody.append(paratext)
    elif pagename == 'activities':
        if paratypecode == 'head':
            activities_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            activities_paratextbody.append(paratext)
    elif pagename == 'joinin':
        if paratypecode == 'head':
            joinin_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            joinin_paratextbody.append(paratext)
    elif pagename == 'results':
        if paratypecode == 'head':
            results_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            results_paratextbody.append(paratext)
    elif pagename == 'phase1':
        if paratypecode == 'head':
            phase1_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            phase1_paratextbody.append(paratext)
    elif pagename == 'statestandards':
        if paratypecode == 'head':
            statestandards_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            statestandards_paratextbody.append(paratext)
    elif pagename == 'questionnaire':
        if paratypecode == 'head':
            questionnaire_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            questionnaire_paratextbody.append(paratext)
    elif pagename == 'curriculum':
        if paratypecode == 'head':
            curriculum_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            curriculum_paratextbody.append(paratext)
    elif pagename == 'whatlearned':
        if paratypecode == 'head':
            whatlearned_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            whatlearned_paratextbody.append(paratext)
    elif pagename == 'whyapply':
        if paratypecode == 'head':
            whyapply_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            whyapply_paratextbody.append(paratext)
    elif pagename == 'focus':
        if paratypecode == 'head':
            focus_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            focus_paratextbody.append(paratext)
    elif pagename == 'details':
        if paratypecode == 'head':
            details_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            details_paratextbody.append(paratext)
    elif pagename == 'whatexpect':
        if paratypecode == 'head':
            whatexpect_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            whatexpect_paratextbody.append(paratext)
    elif pagename == 'goal':  # add the pagename & string to the head list.
        if paratypecode == 'head':
            goal_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            goal_paratextbody.append(paratext)
    elif pagename == 'thankyou':  # add the pagename & string to the head list.
        if paratypecode == 'head':
            thankyou_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            thankyou_paratextbody.append(paratext)
    elif pagename == 'board':  # add the pagename & string to the head list.
        if paratypecode == 'head':
            board_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            board_paratextbody.append(paratext)
    elif pagename == 'references':  # add the pagename & string to the head list.
        if paratypecode == 'head':
            references_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            references_paratextbody.append(paratext)
    elif pagename == 'contactus':  # add the pagename & string to the head list.
        if paratypecode == 'head':
            contactus_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            contactus_paratextbody.append(paratext)
    elif pagename == 'terms':  # add the pagename & string to the head list.
        if paratypecode == 'head':
            terms_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            terms_paratextbody.append(paratext)
    elif pagename == 'footer':  # add the pagename & string to the head list.
        if paratypecode == 'head':
            footer_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            footer_paratextbody.append(paratext)

# query3 = 'select pagename, title from webpage;'

# Lower priority - Query 3 will be completed later.
# crsr.execute(query3)
# for (
#    pagename, title
#    ) in crsr:
#    projname = projname1 + ' ' + projname2 + ' ' + projname3
#    copyrightmsg = copyrightmsg1 + ' ' + projname + '.  ' + copyrightmsg2

@app.route("/")
def home():
    return render_template("/home.html",\
    projname = projname,\
    projname1 = projname1,\
    projname2 = projname2,\
    projname3 = projname3,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    telephonenr = telephonenr,\
    emailaddr = emailaddr,\
    copyrightmsg = copyrightmsg,\
    leadpixinscr1 = leadpixinscr1,\
    leadpixinscr2 = leadpixinscr2,\
    leadpixinscr3 = leadpixinscr3,\
    home_paratexthead1 = home_paratexthead[1], home_paratextbody1 = home_paratextbody[1],\
    home_paratexthead2 = home_paratexthead[2], home_paratextbody2 = home_paratextbody[2],\
    home_paratexthead3 = home_paratexthead[3], home_paratextbody3 = home_paratextbody[3],\
    home_paratexthead4 = home_paratexthead[4], home_paratextbody4 = home_paratextbody[4],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/why/")
def why():
    return render_template("why.html",\
    projname = projname,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    why_paratexthead1 = why_paratexthead[1],\
    why_paratextbody1 = why_paratextbody[1],\
    why_paratexthead2 = why_paratexthead[2],\
    why_paratextbody2 = why_paratextbody[2],\
    why_paratexthead3 = why_paratexthead[3],\
    why_paratextbody3 = why_paratextbody[3],\
    why_paratexthead4 = why_paratexthead[4],\
    why_paratextbody4 = why_paratextbody[4],\
    why_paratextbody5 = why_paratextbody[5],\
    copyrightmsg = copyrightmsg,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/earlyyears/")
def earlyyears():
    return render_template("earlyyears.html",\
    projname = projname,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    earlyyears_paratexthead1 = earlyyears_paratexthead[1],\
    earlyyears_paratextbody1 = earlyyears_paratextbody[1],\
    earlyyears_paratexthead2 = earlyyears_paratexthead[2],\
    earlyyears_paratextbody2 = earlyyears_paratextbody[2],\
    earlyyears_paratexthead3 = earlyyears_paratexthead[3],\
    earlyyears_paratextbody3 = earlyyears_paratextbody[3],\
    copyrightmsg = copyrightmsg,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/parenting/")
def parenting():
    return render_template("parenting.html",\
    projname = projname,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    parenting_paratexthead1 = parenting_paratexthead[1],\
    parenting_paratextbody1 = parenting_paratextbody[1],\
    parenting_paratexthead2 = parenting_paratexthead[2],\
    parenting_paratextbody2 = parenting_paratextbody[2],\
    parenting_paratexthead3 = parenting_paratexthead[3],\
    parenting_paratextbody3 = parenting_paratextbody[3],\
    copyrightmsg = copyrightmsg,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/thechallenge/")
def thechallenge():
    return render_template("thechallenge.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    thechallenge_paratexthead1 = thechallenge_paratexthead[1],\
    thechallenge_paratextbody1 = thechallenge_paratextbody[1],\
    thechallenge_paratexthead2 = thechallenge_paratexthead[2],\
    thechallenge_paratextbody2 = thechallenge_paratextbody[2],\
    thechallenge_paratexthead3 = thechallenge_paratexthead[3],\
    thechallenge_paratextbody3 = thechallenge_paratextbody[3],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])


@app.route("/opportunity/")
def opportunity():
    return render_template("opportunity.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    opportunity_paratexthead1 = opportunity_paratexthead[1],\
    opportunity_paratextbody1 = opportunity_paratextbody[1],\
    opportunity_paratexthead2 = opportunity_paratexthead[2],\
    opportunity_paratextbody2 = opportunity_paratextbody[2],\
    opportunity_paratexthead3 = opportunity_paratexthead[3],\
    opportunity_paratextbody3 = opportunity_paratextbody[3],\
    opportunity_paratextbody4 = opportunity_paratextbody[4],\
    opportunity_paratextbody5 = opportunity_paratextbody[5],\
    opportunity_paratextbody6 = opportunity_paratextbody[6],\
    opportunity_paratextbody7 = opportunity_paratextbody[7],\
    opportunity_paratextbody8 = opportunity_paratextbody[8],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/ourwork/")
def ourwork():
    return render_template("ourwork.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    ourwork_paratexthead1 = ourwork_paratexthead[1],\
    ourwork_paratextbody1 = ourwork_paratextbody[1],\
    ourwork_paratexthead2 = ourwork_paratexthead[2],\
    ourwork_paratextbody2 = ourwork_paratextbody[2],\
    ourwork_paratexthead3 = ourwork_paratexthead[3],\
    ourwork_paratextbody3 = ourwork_paratextbody[3],\
    ourwork_paratexthead4 = ourwork_paratexthead[4],\
    ourwork_paratextbody4 = ourwork_paratextbody[4],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/history/")
def history():
    return render_template("history.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    history_paratexthead1 = history_paratexthead[1],\
    history_paratextbody1 = history_paratextbody[1],\
    history_paratextbody2 = history_paratextbody[2],\
    history_paratextbody3 = history_paratextbody[3],\
    history_paratextbody4 = history_paratextbody[4],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/activities/")
def activities():
    return render_template("activities.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    activities_paratexthead1 = activities_paratexthead[1],\
    activities_paratextbody1 = activities_paratextbody[1],\
    activities_paratexthead2 = activities_paratexthead[2],\
    activities_paratextbody2 = activities_paratextbody[2],\
    activities_paratexthead3 = activities_paratexthead[3],\
    activities_paratextbody3 = activities_paratextbody[3],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/joinin/")
def joinin():
    return render_template("joinin.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    joinin_paratexthead1 = joinin_paratexthead[1],\
    joinin_paratextbody1 = joinin_paratextbody[1],\
    joinin_paratexthead2 = joinin_paratexthead[2],\
    joinin_paratextbody2 = joinin_paratextbody[2],\
    joinin_paratexthead3 = joinin_paratexthead[3],\
    joinin_paratextbody3 = joinin_paratextbody[3],\
    joinin_paratexthead4 = joinin_paratexthead[4],\
    joinin_paratextbody4 = joinin_paratextbody[4],\
    joinin_paratexthead5 = joinin_paratexthead[5],\
    joinin_paratextbody5 = joinin_paratextbody[5],\
    joinin_paratexthead6 = joinin_paratexthead[6],\
    joinin_paratextbody6 = joinin_paratextbody[6],\
    joinin_paratexthead7 = joinin_paratexthead[7],\
    joinin_paratextbody7 = joinin_paratextbody[7],\
    joinin_paratextbody8 = joinin_paratextbody[8],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/results/")
def results():
    return render_template("results.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    results_paratexthead1 = results_paratexthead[1],\
    results_paratextbody1 = results_paratextbody[1],\
    results_paratexthead2 = results_paratexthead[2],\
    results_paratextbody2 = results_paratextbody[2],\
    results_paratexthead3 = results_paratexthead[3],\
    results_paratextbody3 = results_paratextbody[3],\
    results_paratexthead4 = results_paratexthead[4],\
    results_paratextbody4 = results_paratextbody[4],\
    results_paratexthead5 = results_paratexthead[5],\
    results_paratextbody5 = results_paratextbody[5],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/phase1/")
def phase1():
    return render_template("phase1.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    phase1_paratexthead1 = phase1_paratexthead[1],\
    phase1_paratextbody1 = phase1_paratextbody[1],\
    phase1_paratextbody2 = phase1_paratextbody[2],\
    phase1_paratextbody3 = phase1_paratextbody[3],\
    phase1_paratextbody4 = phase1_paratextbody[4],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/statestandards/")
def statestandards():
    return render_template("statestandards.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    statestandards_paratexthead1 = statestandards_paratexthead[1],\
    statestandards_paratextbody1 = statestandards_paratextbody[1],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/questionnaire/")
def questionnaire():
    return render_template("questionnaire.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    questionnaire_paratexthead1 = questionnaire_paratexthead[1],\
    questionnaire_paratextbody1 = questionnaire_paratextbody[1],\
    questionnaire_paratextbody2 = questionnaire_paratextbody[2],\
    questionnaire_paratextbody3 = questionnaire_paratextbody[3],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/curriculum/")
def curriculum():
    return render_template("curriculum.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    curriculum_paratexthead1 = curriculum_paratexthead[1],\
    curriculum_paratextbody1 = curriculum_paratextbody[1],\
    curriculum_paratextbody2 = curriculum_paratextbody[2],\
    curriculum_paratextbody3 = curriculum_paratextbody[3],\
    curriculum_paratextbody4 = curriculum_paratextbody[4],\
    curriculum_paratextbody5 = curriculum_paratextbody[5],\
    curriculum_paratextbody6 = curriculum_paratextbody[6],\
    curriculum_paratextbody7 = curriculum_paratextbody[7],\
    curriculum_paratextbody8 = curriculum_paratextbody[8],\
    curriculum_paratextbody9 = curriculum_paratextbody[9],\
    curriculum_paratextbody10 = curriculum_paratextbody[10],\
    curriculum_paratextbody11 = curriculum_paratextbody[11],\
    curriculum_paratextbody12 = curriculum_paratextbody[12],\
    curriculum_paratextbody13 = curriculum_paratextbody[13],\
    curriculum_paratextbody14 = curriculum_paratextbody[14],\
    curriculum_paratextbody15 = curriculum_paratextbody[15],\
    curriculum_paratextbody16 = curriculum_paratextbody[16],\
    curriculum_paratextbody17 = curriculum_paratextbody[17],\
    curriculum_paratextbody18 = curriculum_paratextbody[18],\
    curriculum_paratextbody19 = curriculum_paratextbody[19],\
    curriculum_paratextbody20 = curriculum_paratextbody[20],\
    curriculum_paratextbody21 = curriculum_paratextbody[21],\
    curriculum_paratextbody22 = curriculum_paratextbody[22],\
    curriculum_paratextbody23 = curriculum_paratextbody[23],\
    curriculum_paratextbody24 = curriculum_paratextbody[24],\
    curriculum_paratextbody25 = curriculum_paratextbody[25],\
    curriculum_paratextbody26 = curriculum_paratextbody[26],\
    curriculum_paratextbody27 = curriculum_paratextbody[27],\
    curriculum_paratextbody28 = curriculum_paratextbody[28],\
    curriculum_paratextbody29 = curriculum_paratextbody[29],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/whatlearned/")
def whatlearned():
    return render_template("whatlearned.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    whatlearned_paratexthead1 = whatlearned_paratexthead[1],\
    whatlearned_paratextbody1 = whatlearned_paratextbody[1],\
    whatlearned_paratextbody2 = whatlearned_paratextbody[2],\
    whatlearned_paratextbody3 = whatlearned_paratextbody[3],\
    whatlearned_paratextbody4 = whatlearned_paratextbody[4],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/grants/")
def grants():
    return render_template("grants.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/whyapply/")
def whyapply():
    return render_template("whyapply.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    whyapply_paratexthead1 = whyapply_paratexthead[1],\
    whyapply_paratextbody1 = whyapply_paratextbody[1],\
    whyapply_paratexthead2 = whyapply_paratexthead[2],\
    whyapply_paratextbody2 = whyapply_paratextbody[2],\
    whyapply_paratexthead3 = whyapply_paratexthead[3],\
    whyapply_paratextbody3 = whyapply_paratextbody[3],\
    whyapply_paratexthead4 = whyapply_paratexthead[4],\
    whyapply_paratextbody4 = whyapply_paratextbody[4],\
    whyapply_paratextbody5 = whyapply_paratextbody[5],\
    whyapply_paratextbody6 = whyapply_paratextbody[6],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/focus/")
def focus():
    return render_template("focus.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    focus_paratexthead1 = focus_paratexthead[1],\
    focus_paratextbody1 = focus_paratextbody[1],\
    focus_paratextbody2 = focus_paratextbody[2],\
    focus_paratextbody3 = focus_paratextbody[3],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/details/")
def details():
    return render_template("details.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    details_paratexthead1 = details_paratexthead[1],\
    details_paratextbody1 = details_paratextbody[1],\
    details_paratexthead2 = details_paratexthead[2],\
    details_paratextbody2 = details_paratextbody[2],\
    details_paratexthead3 = details_paratexthead[3],\
    details_paratextbody3 = details_paratextbody[3],\
    details_paratexthead4 = details_paratexthead[4],\
    details_paratextbody4 = details_paratextbody[4],\
    details_paratexthead5 = details_paratexthead[5],\
    details_paratextbody5 = details_paratextbody[5],\
    details_paratexthead6 = details_paratexthead[6],\
    details_paratextbody6 = details_paratextbody[6],\
    details_paratexthead7 = details_paratexthead[7],\
    details_paratextbody7 = details_paratextbody[7],\
    details_paratexthead8 = details_paratexthead[8],\
    details_paratextbody8 = details_paratextbody[8],\
    details_paratexthead9 = details_paratexthead[9],\
    details_paratextbody9 = details_paratextbody[9],\
    details_paratexthead10 = details_paratexthead[10],\
    details_paratextbody10 = details_paratextbody[10],\
    details_paratexthead11 = details_paratexthead[11],\
    details_paratextbody11 = details_paratextbody[11],\
    details_paratexthead12 = details_paratexthead[12],\
    details_paratextbody12 = details_paratextbody[12],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/shareidea/")
def shareidea():
    return render_template("shareidea.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/whatexpect/")
def whatexpect():
    return render_template("whatexpect.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    whatexpect_paratexthead1 = whatexpect_paratexthead[1],\
    whatexpect_paratextbody1 = whatexpect_paratextbody[1],\
    whatexpect_paratextbody2 = whatexpect_paratextbody[2],\
    whatexpect_paratextbody3 = whatexpect_paratextbody[3],\
    whatexpect_paratextbody4 = whatexpect_paratextbody[4],\
    whatexpect_paratextbody5 = whatexpect_paratextbody[5],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/forfuture/")
def forfuture():
    return render_template("forfuture.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/about/")
def about():
    return render_template("about.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/goal/")
def goal():
    return render_template("goal.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    goal_paratexthead1 = goal_paratexthead[1],\
    goal_paratextbody1 = goal_paratextbody[1],\
    goal_paratextbody2 = goal_paratextbody[2],\
    goal_paratextbody3 = goal_paratextbody[3],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/thankyou/")
def thankyou():
    return render_template("thankyou.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    thankyou_paratexthead1 = thankyou_paratexthead[1],\
    thankyou_paratextbody1 = thankyou_paratextbody[1],\
    thankyou_paratexthead2 = thankyou_paratexthead[2],\
    thankyou_paratextbody2 = thankyou_paratextbody[2],\
    thankyou_paratexthead3 = thankyou_paratexthead[3],\
    thankyou_paratextbody3 = thankyou_paratextbody[3],\
    thankyou_paratexthead4 = thankyou_paratexthead[4],\
    thankyou_paratextbody4 = thankyou_paratextbody[4],\
    thankyou_paratexthead5 = thankyou_paratexthead[5],\
    thankyou_paratextbody5 = thankyou_paratextbody[5],\
    thankyou_paratexthead6 = thankyou_paratexthead[6],\
    thankyou_paratextbody6 = thankyou_paratextbody[6],\
    thankyou_paratexthead7 = thankyou_paratexthead[7],\
    thankyou_paratextbody7 = thankyou_paratextbody[7],\
    thankyou_paratexthead8 = thankyou_paratexthead[8],\
    thankyou_paratextbody8 = thankyou_paratextbody[8],\
    thankyou_paratexthead9 = thankyou_paratexthead[9],\
    thankyou_paratextbody9 = thankyou_paratextbody[9],\
    thankyou_paratexthead10 = thankyou_paratexthead[10],\
    thankyou_paratextbody10 = thankyou_paratextbody[10],\
    thankyou_paratexthead11 = thankyou_paratexthead[11],\
    thankyou_paratextbody11 = thankyou_paratextbody[11],\
    thankyou_paratexthead12 = thankyou_paratexthead[12],\
    thankyou_paratextbody12 = thankyou_paratextbody[12],\
    thankyou_paratexthead13 = thankyou_paratexthead[13],\
    thankyou_paratextbody13 = thankyou_paratextbody[13],\
    thankyou_paratexthead14 = thankyou_paratexthead[14],\
    thankyou_paratextbody14 = thankyou_paratextbody[14],\
    thankyou_paratexthead15 = thankyou_paratexthead[15],\
    thankyou_paratextbody15 = thankyou_paratextbody[15],\
    thankyou_paratextbody16 = thankyou_paratextbody[16],\
    thankyou_paratextbody17 = thankyou_paratextbody[17],\
    thankyou_paratextbody18 = thankyou_paratextbody[18],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/board/")
def board():
    return render_template("board.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2],\
    board_paratexthead1 = board_paratexthead[1],\
    board_paratextbody1 = board_paratextbody[1],\
    board_paratextbody2 = board_paratextbody[2])
 
@app.route("/references/")
def references():
    return render_template("references.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    references_paratexthead1 = references_paratexthead[1],\
    references_paratextbody1 = references_paratextbody[1],\
    references_paratextbody2 = references_paratextbody[2],\
    references_paratextbody3 = references_paratextbody[3],\
    references_paratextbody4 = references_paratextbody[4],\
    references_paratextbody5 = references_paratextbody[5],\
    references_paratextbody6 = references_paratextbody[6],\
    references_paratextbody7 = references_paratextbody[7],\
    references_paratextbody8 = references_paratextbody[8],\
    references_paratextbody9 = references_paratextbody[9],\
    references_paratextbody10 = references_paratextbody[10],\
    references_paratextbody11 = references_paratextbody[11],\
    references_paratextbody12 = references_paratextbody[12],\
    references_paratextbody13 = references_paratextbody[13],\
    references_paratextbody14 = references_paratextbody[14],\
    references_paratextbody15 = references_paratextbody[15],\
    references_paratextbody16 = references_paratextbody[16],\
    references_paratextbody17 = references_paratextbody[17],\
    references_paratextbody18 = references_paratextbody[18],\
    references_paratextbody19 = references_paratextbody[19],\
    references_paratextbody20 = references_paratextbody[20],\
    references_paratextbody21 = references_paratextbody[21],\
    references_paratextbody22 = references_paratextbody[22],\
    references_paratextbody23 = references_paratextbody[23],\
    references_paratextbody24 = references_paratextbody[24],\
    references_paratextbody25 = references_paratextbody[25],\
    references_paratextbody26 = references_paratextbody[26],\
    references_paratextbody27 = references_paratextbody[27],\
    references_paratextbody28 = references_paratextbody[28],\
    references_paratextbody29 = references_paratextbody[29],\
    references_paratextbody30 = references_paratextbody[30],\
    references_paratextbody31 = references_paratextbody[31],\
    references_paratextbody32 = references_paratextbody[32],\
    references_paratextbody33 = references_paratextbody[33],\
    references_paratextbody34 = references_paratextbody[34],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/contactus/")
def contactus():
    return render_template("contactus.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    telephonenr = telephonenr,\
    contactus_paratexthead1 = contactus_paratexthead[1],\
    contactus_paratextbody1 = contactus_paratextbody[1],\
    contactus_paratexthead2 = contactus_paratexthead[2],\
    contactus_paratextbody2 = contactus_paratextbody[2],\
    contactus_paratextbody3 = contactus_paratextbody[3],\
    contactus_paratextbody4 = contactus_paratextbody[4],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/terms/")
def terms():
    return render_template("terms.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    terms_paratexthead1 = terms_paratexthead[1],\
    terms_paratextbody1 = terms_paratextbody[1],\
    terms_paratexthead2 = terms_paratexthead[2],\
    terms_paratextbody2 = terms_paratextbody[2],\
    terms_paratexthead3 = terms_paratexthead[3],\
    terms_paratextbody3 = terms_paratextbody[3],\
    terms_paratexthead4 = terms_paratexthead[4],\
    terms_paratextbody4 = terms_paratextbody[4],\
    terms_paratexthead5 = terms_paratexthead[5],\
    terms_paratextbody5 = terms_paratextbody[5],\
    terms_paratexthead6 = terms_paratexthead[6],\
    terms_paratextbody6 = terms_paratextbody[6],\
    terms_paratexthead7 = terms_paratexthead[7],\
    terms_paratextbody7 = terms_paratextbody[7],\
    terms_paratexthead8 = terms_paratexthead[8],\
    terms_paratextbody8 = terms_paratextbody[8],\
    terms_paratexthead9 = terms_paratexthead[9],\
    terms_paratextbody9 = terms_paratextbody[9],\
    terms_paratexthead10 = terms_paratexthead[10],\
    terms_paratextbody10 = terms_paratextbody[10],\
    terms_paratexthead11 = terms_paratexthead[11],\
    terms_paratextbody11 = terms_paratextbody[11],\
    terms_paratexthead12 = terms_paratexthead[12],\
    terms_paratextbody12 = terms_paratextbody[12],\
    terms_paratexthead13 = terms_paratexthead[13],\
    terms_paratextbody13 = terms_paratextbody[13],\
    terms_paratexthead14 = terms_paratexthead[14],\
    terms_paratextbody14 = terms_paratextbody[14],\
    terms_paratexthead15 = terms_paratexthead[15],\
    terms_paratextbody15 = terms_paratextbody[15],\
    terms_paratexthead16 = terms_paratexthead[16],\
    terms_paratextbody16 = terms_paratextbody[16],\
    terms_paratexthead17 = terms_paratexthead[17],\
    terms_paratextbody17 = terms_paratextbody[17],\
    terms_paratexthead18 = terms_paratexthead[18],\
    terms_paratextbody18 = terms_paratextbody[18],\
    terms_paratexthead19 = terms_paratexthead[19],\
    terms_paratextbody19 = terms_paratextbody[19],\
    terms_paratexthead20 = terms_paratexthead[20],\
    terms_paratextbody20 = terms_paratextbody[20],\
    terms_paratextbody21 = terms_paratextbody[21],\
    terms_paratextbody22 = terms_paratextbody[22],\
    terms_paratextbody23 = terms_paratextbody[23],\
    terms_paratextbody24 = terms_paratextbody[24],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/scienceconverging/")
def scienceconverging():
    return render_template("scienceconverging.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    scienceconverging_paratexthead1 = scienceconverging_paratexthead[1],\
    scienceconverging_paratextbody1 = scienceconverging_paratextbody[1],\
    scienceconverging_paratexthead2 = scienceconverging_paratexthead[2],\
    scienceconverging_paratextbody2 = scienceconverging_paratextbody[2],\
    scienceconverging_paratexthead3 = scienceconverging_paratexthead[3],\
    scienceconverging_paratextbody3 = scienceconverging_paratextbody[3],\
    scienceconverging_paratexthead4 = scienceconverging_paratexthead[4],\
    scienceconverging_paratextbody4 = scienceconverging_paratextbody[4],\
    scienceconverging_paratexthead5 = scienceconverging_paratexthead[5],\
    scienceconverging_paratextbody5 = scienceconverging_paratextbody[5],\
    scienceconverging_paratexthead6 = scienceconverging_paratexthead[6],\
    scienceconverging_paratextbody6 = scienceconverging_paratextbody[6],\
    scienceconverging_paratexthead7 = scienceconverging_paratexthead[7],\
    scienceconverging_paratextbody7 = scienceconverging_paratextbody[7],\
    scienceconverging_paratexthead8 = scienceconverging_paratexthead[8],\
    scienceconverging_paratextbody8 = scienceconverging_paratextbody[8],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/makingmusic_cont/")
def makingmusic_cont():
    return render_template("/content/makingmusic_cont.html",\
    projname1 = projname1,\
    projname2 = projname2,\
    projname3 = projname3)

@app.route("/whyintro_cont/")
def whyintro_cont():
    return render_template("/content/whyintro_cont.html",\
    paratexthead1 = paratexthead[0], paratextbody1 = paratextbody[0],\
    paratexthead2 = paratexthead[1], paratextbody2 = paratextbody[1],\
    paratexthead3 = paratexthead[2], paratextbody3 = paratextbody[2],\
    paratexthead4 = paratexthead[3], paratextbody4 = paratextbody[3])

@app.route("/foot/")
def foot():
    return render_template("/foot.html",\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    projname = projname,\
    copyrightmsg = copyrightmsg)

@app.route('/ajax/find-project', methods=['GET'])
def findproject():
    reqtype = request.args['reqtype']
    projectnumber = request.args['projectnumber']
    submissiondate = request.args['submissiondate']
    pilastname = request.args['pilastname']

    crsr.execute("SELECT count(*) FROM myidea WHERE projnum = %s and DATE_FORMAT(subdate,'%%Y-%%m-%%d') = %s and pilastname=%s",(projectnumber, submissiondate, pilastname)) 
    #fetch all rows and store as a set of tuples 
    (number_of_rows,) = crsr.fetchone()
    
    status = "error"
    msg = "No Project found. Please try with different details"
    url = ""
    code = secrets.token_urlsafe(16)
    
    if (number_of_rows > 0):
        status = "success"
        msg = "Project found!. Please wait, redirecting..."
        if reqtype == 'document':
            url = url_for('senddocument', secret=code, pnum=projectnumber, reqtype=reqtype)
        else:
            url = url_for('sharemyidea', secret=code, pnum=projectnumber, reqtype=reqtype)
    
    return jsonify(status = status, url=url, message=msg)

@app.route('/share-my-idea', methods=['GET'])
def sharemyidea():
    existingprojnum = ''
    if 'pnum' in request.args:
        existingprojnum = request.args['pnum']
    
    form = ShareMyIdeaForm(request.form)
    crsr.execute('SELECT code,name FROM states') 
    #fetch all rows and store as a set of tuples 
    statelist = crsr.fetchall()    
        
    return render_template('sharemyidea.html',\
    form=form, statelist=statelist, existingprojnum=existingprojnum,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route('/ajax/save-my-idea', methods=['POST'])
def savemyidea():
    form = ShareMyIdeaForm(request.form)
    status = 'error'
    if form.validate_on_submit():
       
        existingprojnum = request.form['existingprojnum'] if request.form['existingprojnum'] !='' else None
        projname = form.projname.data
        reqamount = float(form.reqamount.data)
        orgname = form.orgname.data
        orgwebaddr = form.orgwebaddr.data
        schoolname = form.schoolname.data
        schoolwebaddr = form.schoolwebaddr.data
        pititle = form.pititle.data.title()
        picv = form.picv.data
        pifirstname = form.pifirstname.data.title()
        pimi = form.pimi.data.title()
        pilastname = form.pilastname.data.title()
        pisuffix = form.pisuffix.data.title()
        piemail = form.piemail.data
        pitele = form.pitele.data
        piaddr1 = form.piaddr1.data
        piaddr2 = form.piaddr2.data
        picity = form.picity.data.title()
        pistate = request.form['pistate']
        pizip = form.pizip.data
        othertitle = form.othertitle.data.title() if form.othertitle.data !='' else None
        otherfirstname = form.otherfirstname.data.title() if form.otherfirstname.data !='' else None
        othermi = form.othermi.data.title() if form.othermi.data !='' else None
        otherlastname = form.otherlastname.data.title() if form.otherlastname.data !='' else None
        othersuffix = form.othersuffix.data.title() if form.othersuffix.data !='' else None
        otheremail = form.otheremail.data if form.otheremail.data !='' else None
        othertele = form.othertele.data if form.othertele.data !='' else None
        otheraddr1 = form.otheraddr1.data if form.otheraddr1.data !='' else None
        otheraddr2 = form.otheraddr2.data if form.otheraddr2.data !='' else None
        othercity = form.othercity.data.title() if form.othercity.data !='' else None
        otherstate = request.form['otherstate'] if request.form['otherstate'] !='' else None
        otherzip = form.otherzip.data if form.otherzip.data != '' else None
        irsletter_TF = 0
        budget_TF = 0
        confirmsent_TF = 0
        goal = form.goal.data
        description = form.description.data
        aboutpeople = form.aboutpeople.data if form.aboutpeople.data !='' else None
        relevance = form.relevance.data
        dissemination = form.dissemination.data
        projother = form.projother.data if form.projother.data !='' else None
        
        crsr.execute("""
            INSERT INTO myidea (projname,reqamount,newprojnum,orgname,orgwebaddr,schoolname,schoolwebaddr,pititle,picv,pifirstname,pimi,pilastname,pisuffix,piemail,pitele,piaddr1,piaddr2,picity,pistate,pizip,othertitle,otherfirstname,othermi,otherlastname,othersuffix,otheremail,othertele,otheraddr1,otheraddr2,othercity,otherstate,otherzip,irsletter_TF,budget_TF,confirmsent_TF,goal,description,aboutpeople,relevance,dissemination,projother) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            , (projname,reqamount,None,orgname,orgwebaddr,schoolname,schoolwebaddr,pititle,picv,pifirstname,pimi,pilastname,pisuffix,piemail,pitele,piaddr1,piaddr2,picity,pistate,pizip,othertitle,otherfirstname,othermi,otherlastname,othersuffix,otheremail,othertele,otheraddr1,otheraddr2,othercity,otherstate,otherzip,irsletter_TF,budget_TF,confirmsent_TF,goal,description,aboutpeople,relevance,dissemination,projother)
        )
        projnum = crsr.lastrowid;

        #update the existing project record with new project number
        crsr.execute("UPDATE myidea SET newprojnum=%s WHERE projnum=%s", (projnum,existingprojnum))
        conn.commit()
        
        status = 'success'
        today = date.today()        
        msg = "<b>Thank you</b> for sharing your Idea with us.<br><br> \
                We look forward to reading and learning about it.<br><br>\
                Your Project Number is: <b> " + str(projnum) + " </b> <br> <br> \
                Your Submission date is: <b> " + str(today.strftime("%m/%d/%Y")) + " </b> <br> <br> \
                Please save these as they may be required for communicating with us about the project. <br> <br> \
                Because we may use this and other information submitted with your Idea to verfiy persons connected with this project, \
                we suggest you maintain such information securely."
                
        url = url_for('whatexpect');
        flash(Markup(msg),'success')
        return jsonify(status = status, data=[], message=msg, url=url)

    return jsonify(status = status, data=form.errors, message='One or more items need revision.  Please modify.')

@app.route('/send-document', methods=['GET', 'POST'])
def senddocument():
    existingprojnum = ''
    
    if 'pnum' in request.args:
        existingprojnum = request.args['pnum']
    else:
        flash('Invalid Project','error')
        return redirect(url_for('shareidea'))

    today = date.today()    
    seconds = str(int(time.time()))    
    suffix = today.strftime("%Y-%m-%d") + '-' + seconds
    
    form = sendDocumentForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            irsfile = form.irsfield.data
            
            filename = secure_filename(str(existingprojnum) + '-irs-' + suffix + '.' + irsfile.filename.split('.')[1])
            irsfile.save(os.path.join(
                os.getcwd(),'public','static', 'received_files', filename
            ))
            crsr.execute("INSERT INTO myidea_docs (projnum,document) VALUES (%s, %s)", (existingprojnum,filename))

            budfile = form.budfield.data
            filename = secure_filename(str(existingprojnum) + '-bud-' + suffix + '.' + budfile.filename.split('.')[1])
            budfile.save(os.path.join(
                os.getcwd(),'public','static', 'received_files', filename
            ))

            crsr.execute("INSERT INTO myidea_docs (projnum,document) VALUES (%s, %s)", (existingprojnum,filename))
            
            #update the existing project record with file upload status
            crsr.execute("UPDATE myidea SET irsletter_TF=1, budget_TF=1 WHERE projnum=%s", (existingprojnum))
            conn.commit()


            flash('Document uploaded successfully.','success')
            return redirect(url_for('shareidea'))
        else:
            flash('One or more items is incorrect. Please try with valid files', 'error')
            
    return render_template('senddocument.html', form=form, existingprojnum=existingprojnum)

#from app import forms

if __name__=='__main__':
    main()
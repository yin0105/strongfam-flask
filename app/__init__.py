from flask import Flask, request, flash, jsonify, url_for, redirect, Markup
from flask import render_template
from datetime import datetime, date
import time
import re
# import mysql.connector
from flaskext.mysql import MySQL
from forms import ShareMyIdeaForm, sendDocumentForm
# from app.forms import ShareMyIdeaForm, sendDocumentForm 
from werkzeug.utils import secure_filename
import secrets
import os

app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'john1'  
app.config['MYSQL_DATABASE_PASSWORD'] = 'aB22yy98'  
app.config['MYSQL_DATABASE_DB'] = 'pffp'  
app.config['MYSQL_DATABASE_HOST'] = 'localhost'  
# app.config['MYSQL_DATABASE_HOST'] = 'mysql.fpproject.dreamhosters.com'  
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
    select pagename, paranr, paratext
    from pagetext
    order by pagename, paranr
    ;
    """

# Initialize these variables as simple one dimensional lists:
home_itemtxt = []
why_itemtxt = []
scienceaccumulating_itemtxt = []
earlyyears_itemtxt = []
parenting_itemtxt = []
thechallenge_itemtxt = []
opportunity_itemtxt = []
ourwork_itemtxt = []
history_itemtxt = []
activities_itemtxt = []
joinin_itemtxt = []
results_itemtxt = []
phase1_itemtxt = []
statestandards_itemtxt = []
questionnaire_itemtxt = []
curriculum_itemtxt = []
whatlearned_itemtxt = []
whyapply_itemtxt = []
focus_itemtxt = []
details_itemtxt = []
whatexpect_itemtxt = []
goal_itemtxt = []
thankyou_itemtxt = []
board_itemtxt = []
references_itemtxt = []
contactus_itemtxt = []
terms_itemtxt = []
footer_itemtxt = []

crsr.execute(query2)
for (pagename, paranr, paratext) in crsr:
    if pagename == 'home':  # Must do a separate section for EACH page BUT maybe not in future
        home_itemtxt.append(paratext) # add the pagename & string to the head list
    elif pagename == 'why':
        why_itemtxt.append(paratext)
    elif pagename == 'scienceaccumulating':
        scienceaccumulating_itemtxt.append(paratext)
    elif pagename == 'earlyyears':
        earlyyears_itemtxt.append(paratext)
    elif pagename == 'parenting':
        parenting_itemtxt.append(paratext)
    elif pagename == 'thechallenge':
        thechallenge_itemtxt.append(paratext)
    elif pagename == 'opportunity':
        opportunity_itemtxt.append(paratext)
    elif pagename == 'ourwork':
        ourwork_itemtxt.append(paratext)
    elif pagename == 'history':
        history_itemtxt.append(paratext)
    elif pagename == 'activities':
        activities_itemtxt.append(paratext)
    elif pagename == 'joinin':
        joinin_itemtxt.append(paratext)
    elif pagename == 'results':
        results_itemtxt.append(paratext)
    elif pagename == 'phase1':
        phase1_itemtxt.append(paratext)
    elif pagename == 'statestandards':
        statestandards_itemtxt.append(paratext)
    elif pagename == 'questionnaire':
        questionnaire_itemtxt.append(paratext)
    elif pagename == 'curriculum':
        curriculum_itemtxt.append(paratext)
    elif pagename == 'whatlearned':
        whatlearned_itemtxt.append(paratext)
    elif pagename == 'whyapply':
        whyapply_itemtxt.append(paratext)
    elif pagename == 'focus':
        focus_itemtxt.append(paratext)
    elif pagename == 'details':
        details_itemtxt.append(paratext)
    elif pagename == 'whatexpect':
        whatexpect_itemtxt.append(paratext)
    elif pagename == 'goal':
        goal_itemtxt.append(paratext)
    elif pagename == 'thankyou':
        thankyou_itemtxt.append(paratext)
    elif pagename == 'board':
        board_itemtxt.append(paratext)
    elif pagename == 'references':
        references_itemtxt.append(paratext)
    elif pagename == 'contactus':
        contactus_itemtxt.append(paratext)
    elif pagename == 'terms':
        terms_itemtxt.append(paratext)
    elif pagename == 'footer':
        footer_itemtxt.append(paratext)

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
    home_itemtxt1 = home_itemtxt[0], home_itemtxt2 = home_itemtxt[1],\
    home_itemtxt3 = home_itemtxt[2], home_itemtxt4 = home_itemtxt[3],\
    home_itemtxt5 = home_itemtxt[4], home_itemtxt6 = home_itemtxt[5],\
    home_itemtxt7 = home_itemtxt[6], home_itemtxt8 = home_itemtxt[7],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/why/")
def why():
    return render_template("why.html",\
    projname = projname,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    why_itemtxt1 = why_itemtxt[0],\
    why_itemtxt2 = why_itemtxt[1],\
    why_itemtxt3 = why_itemtxt[2],\
    why_itemtxt4 = why_itemtxt[3],\
    why_itemtxt5 = why_itemtxt[4],\
    why_itemtxt6 = why_itemtxt[5],\
    why_itemtxt7 = why_itemtxt[6],\
    why_itemtxt8 = why_itemtxt[7],\
    why_itemtxt9 = why_itemtxt[8],\
    copyrightmsg = copyrightmsg,\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/scienceaccumulating/")
def scienceaccumulating():
    return render_template("scienceaccumulating.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    scienceaccumulating_itemtxt1 = scienceaccumulating_itemtxt[0],\
    scienceaccumulating_itemtxt2 = scienceaccumulating_itemtxt[1],\
    scienceaccumulating_itemtxt3 = scienceaccumulating_itemtxt[2],\
    scienceaccumulating_itemtxt4 = scienceaccumulating_itemtxt[3],\
    scienceaccumulating_itemtxt5 = scienceaccumulating_itemtxt[4],\
    scienceaccumulating_itemtxt6 = scienceaccumulating_itemtxt[5],\
    scienceaccumulating_itemtxt7 = scienceaccumulating_itemtxt[6],\
    scienceaccumulating_itemtxt8 = scienceaccumulating_itemtxt[7],\
    scienceaccumulating_itemtxt9 = scienceaccumulating_itemtxt[8],\
    scienceaccumulating_itemtxt10 = scienceaccumulating_itemtxt[9],\
    scienceaccumulating_itemtxt11 = scienceaccumulating_itemtxt[10],\
    scienceaccumulating_itemtxt12 = scienceaccumulating_itemtxt[11],\
    scienceaccumulating_itemtxt13 = scienceaccumulating_itemtxt[12],\
    scienceaccumulating_itemtxt14 = scienceaccumulating_itemtxt[13],\
    scienceaccumulating_itemtxt15 = scienceaccumulating_itemtxt[14],\
    scienceaccumulating_itemtxt16 = scienceaccumulating_itemtxt[15],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/earlyyears/")
def earlyyears():
    return render_template("earlyyears.html",\
    projname = projname,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    earlyyears_itemtxt1 = earlyyears_itemtxt[0],\
    earlyyears_itemtxt2 = earlyyears_itemtxt[1],\
    earlyyears_itemtxt3 = earlyyears_itemtxt[2],\
    earlyyears_itemtxt4 = earlyyears_itemtxt[3],\
    earlyyears_itemtxt5 = earlyyears_itemtxt[4],\
    earlyyears_itemtxt6 = earlyyears_itemtxt[5],\
    copyrightmsg = copyrightmsg,\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/parenting/")
def parenting():
    return render_template("parenting.html",\
    projname = projname,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    parenting_itemtxt1 = parenting_itemtxt[0],\
    parenting_itemtxt2 = parenting_itemtxt[1],\
    parenting_itemtxt3 = parenting_itemtxt[2],\
    parenting_itemtxt4 = parenting_itemtxt[3],\
    parenting_itemtxt5 = parenting_itemtxt[4],\
    parenting_itemtxt6 = parenting_itemtxt[5],\
    copyrightmsg = copyrightmsg,\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/thechallenge/")
def thechallenge():
    return render_template("thechallenge.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    thechallenge_itemtxt1 = thechallenge_itemtxt[0],\
    thechallenge_itemtxt2 = thechallenge_itemtxt[1],\
    thechallenge_itemtxt3 = thechallenge_itemtxt[2],\
    thechallenge_itemtxt4 = thechallenge_itemtxt[3],\
    thechallenge_itemtxt5 = thechallenge_itemtxt[4],\
    thechallenge_itemtxt6 = thechallenge_itemtxt[5],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])


@app.route("/opportunity/")
def opportunity():
    return render_template("opportunity.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    opportunity_itemtxt1 = opportunity_itemtxt[0],\
    opportunity_itemtxt2 = opportunity_itemtxt[1],\
    opportunity_itemtxt3 = opportunity_itemtxt[2],\
    opportunity_itemtxt4 = opportunity_itemtxt[3],\
    opportunity_itemtxt5 = opportunity_itemtxt[4],\
    opportunity_itemtxt6 = opportunity_itemtxt[5],\
    opportunity_itemtxt7 = opportunity_itemtxt[6],\
    opportunity_itemtxt8 = opportunity_itemtxt[7],\
    opportunity_itemtxt9 = opportunity_itemtxt[8],\
    opportunity_itemtxt10 = opportunity_itemtxt[9],\
    opportunity_itemtxt11 = opportunity_itemtxt[10],\
    opportunity_itemtxt12 = opportunity_itemtxt[11],\
    opportunity_itemtxt13 = opportunity_itemtxt[12],\
    opportunity_itemtxt14 = opportunity_itemtxt[13],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/ourwork/")
def ourwork():
    return render_template("ourwork.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    ourwork_itemtxt1 = ourwork_itemtxt[0],\
    ourwork_itemtxt2 = ourwork_itemtxt[1],\
    ourwork_itemtxt3 = ourwork_itemtxt[2],\
    ourwork_itemtxt4 = ourwork_itemtxt[3],\
    ourwork_itemtxt5 = ourwork_itemtxt[4],\
    ourwork_itemtxt6 = ourwork_itemtxt[5],\
    ourwork_itemtxt7 = ourwork_itemtxt[6],\
    ourwork_itemtxt8 = ourwork_itemtxt[7],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/history/")
def history():
    return render_template("history.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    history_itemtxt1 = history_itemtxt[0],\
    history_itemtxt2 = history_itemtxt[1],\
    history_itemtxt3 = history_itemtxt[2],\
    history_itemtxt4 = history_itemtxt[3],\
    history_itemtxt5 = history_itemtxt[4],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/activities/")
def activities():
    return render_template("activities.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    activities_itemtxt1 = activities_itemtxt[0],\
    activities_itemtxt2 = activities_itemtxt[1],\
    activities_itemtxt3 = activities_itemtxt[2],\
    activities_itemtxt4 = activities_itemtxt[3],\
    activities_itemtxt5 = activities_itemtxt[4],\
    activities_itemtxt6 = activities_itemtxt[5],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/joinin/")
def joinin():
    return render_template("joinin.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    joinin_itemtxt1 = joinin_itemtxt[0],\
    joinin_itemtxt2 = joinin_itemtxt[1],\
    joinin_itemtxt3 = joinin_itemtxt[2],\
    joinin_itemtxt4 = joinin_itemtxt[3],\
    joinin_itemtxt5 = joinin_itemtxt[4],\
    joinin_itemtxt6 = joinin_itemtxt[5],\
    joinin_itemtxt7 = joinin_itemtxt[6],\
    joinin_itemtxt8 = joinin_itemtxt[7],\
    joinin_itemtxt9 = joinin_itemtxt[8],\
    joinin_itemtxt10 = joinin_itemtxt[9],\
    joinin_itemtxt11 = joinin_itemtxt[10],\
    joinin_itemtxt12 = joinin_itemtxt[11],\
    joinin_itemtxt13 = joinin_itemtxt[12],\
    joinin_itemtxt14 = joinin_itemtxt[13],\
    joinin_itemtxt15 = joinin_itemtxt[14],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/results/")
def results():
    return render_template("results.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    results_itemtxt1 = results_itemtxt[0],\
    results_itemtxt2 = results_itemtxt[1],\
    results_itemtxt3 = results_itemtxt[2],\
    results_itemtxt4 = results_itemtxt[3],\
    results_itemtxt5 = results_itemtxt[4],\
    results_itemtxt6 = results_itemtxt[5],\
    results_itemtxt7 = results_itemtxt[6],\
    results_itemtxt8 = results_itemtxt[7],\
    results_itemtxt9 = results_itemtxt[8],\
    results_itemtxt10 = results_itemtxt[9],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/phase1/")
def phase1():
    return render_template("phase1.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    phase1_itemtxt1 = phase1_itemtxt[0],\
    phase1_itemtxt2 = phase1_itemtxt[1],\
    phase1_itemtxt3 = phase1_itemtxt[2],\
    phase1_itemtxt4 = phase1_itemtxt[3],\
    phase1_itemtxt5 = phase1_itemtxt[4],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/statestandards/")
def statestandards():
    return render_template("statestandards.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    statestandards_itemtxt1 = statestandards_itemtxt[0],\
    statestandards_itemtxt2 = statestandards_itemtxt[1],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/questionnaire/")
def questionnaire():
    return render_template("questionnaire.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    questionnaire_itemtxt1 = questionnaire_itemtxt[0],\
    questionnaire_itemtxt2 = questionnaire_itemtxt[1],\
    questionnaire_itemtxt3 = questionnaire_itemtxt[2],\
#    questionnaire_itemtxt4 = questionnaire_itemtxt[3],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/curriculum/")
def curriculum():
    return render_template("curriculum.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    curriculum_itemtxt1 = curriculum_itemtxt[0],\
    curriculum_itemtxt2 = curriculum_itemtxt[1],\
    curriculum_itemtxt3 = curriculum_itemtxt[2],\
    curriculum_itemtxt4 = curriculum_itemtxt[3],\
    curriculum_itemtxt5 = curriculum_itemtxt[4],\
    curriculum_itemtxt6 = curriculum_itemtxt[5],\
    curriculum_itemtxt7 = curriculum_itemtxt[6],\
    curriculum_itemtxt8 = curriculum_itemtxt[7],\
    curriculum_itemtxt9 = curriculum_itemtxt[8],\
    curriculum_itemtxt10 = curriculum_itemtxt[9],\
    curriculum_itemtxt11 = curriculum_itemtxt[10],\
    curriculum_itemtxt12 = curriculum_itemtxt[11],\
    curriculum_itemtxt13 = curriculum_itemtxt[12],\
    curriculum_itemtxt14 = curriculum_itemtxt[13],\
    curriculum_itemtxt15 = curriculum_itemtxt[14],\
    curriculum_itemtxt16 = curriculum_itemtxt[15],\
    curriculum_itemtxt17 = curriculum_itemtxt[16],\
    curriculum_itemtxt18 = curriculum_itemtxt[17],\
    curriculum_itemtxt19 = curriculum_itemtxt[18],\
    curriculum_itemtxt20 = curriculum_itemtxt[19],\
    curriculum_itemtxt21 = curriculum_itemtxt[20],\
    curriculum_itemtxt22 = curriculum_itemtxt[21],\
    curriculum_itemtxt23 = curriculum_itemtxt[22],\
    curriculum_itemtxt24 = curriculum_itemtxt[23],\
    curriculum_itemtxt25 = curriculum_itemtxt[24],\
    curriculum_itemtxt26 = curriculum_itemtxt[25],\
    curriculum_itemtxt27 = curriculum_itemtxt[26],\
    curriculum_itemtxt28 = curriculum_itemtxt[27],\
    curriculum_itemtxt29 = curriculum_itemtxt[28],\
    curriculum_itemtxt30 = curriculum_itemtxt[29],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/whatlearned/")
def whatlearned():
    return render_template("whatlearned.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    whatlearned_itemtxt1 = whatlearned_itemtxt[0],\
    whatlearned_itemtxt2 = whatlearned_itemtxt[1],\
    whatlearned_itemtxt3 = whatlearned_itemtxt[2],\
    whatlearned_itemtxt4 = whatlearned_itemtxt[3],\
    whatlearned_itemtxt5 = whatlearned_itemtxt[4],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/grants/")
def grants():
    return render_template("grants.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/whyapply/")
def whyapply():
    return render_template("whyapply.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    whyapply_itemtxt1 = whyapply_itemtxt[0],\
    whyapply_itemtxt2 = whyapply_itemtxt[1],\
    whyapply_itemtxt3 = whyapply_itemtxt[2],\
    whyapply_itemtxt4 = whyapply_itemtxt[3],\
    whyapply_itemtxt5 = whyapply_itemtxt[4],\
    whyapply_itemtxt6 = whyapply_itemtxt[5],\
    whyapply_itemtxt7 = whyapply_itemtxt[6],\
    whyapply_itemtxt8 = whyapply_itemtxt[7],\
    whyapply_itemtxt9 = whyapply_itemtxt[8],\
    whyapply_itemtxt10 = whyapply_itemtxt[9],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])
 
@app.route("/focus/")
def focus():
    return render_template("focus.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    focus_itemtxt1 = focus_itemtxt[0],\
    focus_itemtxt2 = focus_itemtxt[1],\
    focus_itemtxt3 = focus_itemtxt[2],\
    focus_itemtxt4 = focus_itemtxt[3],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/details/")
def details():
    return render_template("details.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    details_itemtxt1 = details_itemtxt[0],\
    details_itemtxt2 = details_itemtxt[1],\
    details_itemtxt3 = details_itemtxt[2],\
    details_itemtxt4 = details_itemtxt[3],\
    details_itemtxt5 = details_itemtxt[4],\
    details_itemtxt6 = details_itemtxt[5],\
    details_itemtxt7 = details_itemtxt[6],\
    details_itemtxt8 = details_itemtxt[7],\
    details_itemtxt9 = details_itemtxt[8],\
    details_itemtxt10 = details_itemtxt[9],\
    details_itemtxt11 = details_itemtxt[10],\
    details_itemtxt12 = details_itemtxt[11],\
    details_itemtxt13 = details_itemtxt[12],\
    details_itemtxt14 = details_itemtxt[13],\
    details_itemtxt15 = details_itemtxt[14],\
    details_itemtxt16 = details_itemtxt[15],\
    details_itemtxt17 = details_itemtxt[16],\
    details_itemtxt18 = details_itemtxt[17],\
    details_itemtxt19 = details_itemtxt[18],\
    details_itemtxt20 = details_itemtxt[19],\
    details_itemtxt21 = details_itemtxt[20],\
    details_itemtxt22 = details_itemtxt[21],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])
 
@app.route("/shareidea/")
def shareidea():
    return render_template("shareidea.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])
 
@app.route("/whatexpect/")
def whatexpect():
    return render_template("whatexpect.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    whatexpect_itemtxt1 = whatexpect_itemtxt[0],\
    whatexpect_itemtxt2 = whatexpect_itemtxt[1],\
    whatexpect_itemtxt3 = whatexpect_itemtxt[2],\
    whatexpect_itemtxt4 = whatexpect_itemtxt[3],\
    whatexpect_itemtxt5 = whatexpect_itemtxt[4],\
    whatexpect_itemtxt6 = whatexpect_itemtxt[5],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])
 
@app.route("/forfuture/")
def forfuture():
    return render_template("forfuture.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])
 
@app.route("/about/")
def about():
    return render_template("about.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/goal/")
def goal():
    return render_template("goal.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    goal_itemtxt1 = goal_itemtxt[0],\
    goal_itemtxt2 = goal_itemtxt[1],\
    goal_itemtxt3 = goal_itemtxt[2],\
    goal_itemtxt4 = goal_itemtxt[3],\
    goal_itemtxt5 = goal_itemtxt[4],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])
 
@app.route("/thankyou/")
def thankyou():
    return render_template("thankyou.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    thankyou_itemtxt1 = thankyou_itemtxt[0],\
    thankyou_itemtxt2 = thankyou_itemtxt[1],\
    thankyou_itemtxt3 = thankyou_itemtxt[2],\
    thankyou_itemtxt4 = thankyou_itemtxt[3],\
    thankyou_itemtxt5 = thankyou_itemtxt[4],\
    thankyou_itemtxt6 = thankyou_itemtxt[5],\
    thankyou_itemtxt7 = thankyou_itemtxt[6],\
    thankyou_itemtxt8 = thankyou_itemtxt[7],\
    thankyou_itemtxt9 = thankyou_itemtxt[8],\
    thankyou_itemtxt10 = thankyou_itemtxt[9],\
    thankyou_itemtxt11 = thankyou_itemtxt[10],\
    thankyou_itemtxt12 = thankyou_itemtxt[11],\
    thankyou_itemtxt13 = thankyou_itemtxt[12],\
    thankyou_itemtxt14 = thankyou_itemtxt[13],\
    thankyou_itemtxt15 = thankyou_itemtxt[14],\
    thankyou_itemtxt16 = thankyou_itemtxt[15],\
    thankyou_itemtxt17 = thankyou_itemtxt[16],\
    thankyou_itemtxt18 = thankyou_itemtxt[17],\
    thankyou_itemtxt19 = thankyou_itemtxt[18],\
    thankyou_itemtxt20 = thankyou_itemtxt[19],\
    thankyou_itemtxt21 = thankyou_itemtxt[20],\
    thankyou_itemtxt22 = thankyou_itemtxt[21],\
    thankyou_itemtxt23 = thankyou_itemtxt[22],\
    thankyou_itemtxt24 = thankyou_itemtxt[23],\
    thankyou_itemtxt25 = thankyou_itemtxt[24],\
    thankyou_itemtxt26 = thankyou_itemtxt[25],\
    thankyou_itemtxt27 = thankyou_itemtxt[26],\
    thankyou_itemtxt28 = thankyou_itemtxt[27],\
    thankyou_itemtxt29 = thankyou_itemtxt[28],\
    thankyou_itemtxt30 = thankyou_itemtxt[29],\
    thankyou_itemtxt31 = thankyou_itemtxt[30],\
    thankyou_itemtxt32 = thankyou_itemtxt[31],\
    thankyou_itemtxt33 = thankyou_itemtxt[32],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])
 
@app.route("/board/")
def board():
    return render_template("board.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    board_itemtxt1 = board_itemtxt[0],\
    board_itemtxt2 = board_itemtxt[1],\
    board_itemtxt3 = board_itemtxt[2],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])
 
@app.route("/references/")
def references():
    return render_template("references.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    references_itemtxt1 = references_itemtxt[0],\
    references_itemtxt2 = references_itemtxt[1],\
    references_itemtxt3 = references_itemtxt[2],\
    references_itemtxt4 = references_itemtxt[3],\
    references_itemtxt5 = references_itemtxt[4],\
    references_itemtxt6 = references_itemtxt[5],\
    references_itemtxt7 = references_itemtxt[6],\
    references_itemtxt8 = references_itemtxt[7],\
    references_itemtxt9 = references_itemtxt[8],\
    references_itemtxt10 = references_itemtxt[9],\
    references_itemtxt11 = references_itemtxt[10],\
    references_itemtxt12 = references_itemtxt[11],\
    references_itemtxt13 = references_itemtxt[12],\
    references_itemtxt14 = references_itemtxt[13],\
    references_itemtxt15 = references_itemtxt[14],\
    references_itemtxt16 = references_itemtxt[15],\
    references_itemtxt17 = references_itemtxt[16],\
    references_itemtxt18 = references_itemtxt[17],\
    references_itemtxt19 = references_itemtxt[18],\
    references_itemtxt20 = references_itemtxt[19],\
    references_itemtxt21 = references_itemtxt[20],\
    references_itemtxt22 = references_itemtxt[21],\
    references_itemtxt23 = references_itemtxt[22],\
    references_itemtxt24 = references_itemtxt[23],\
    references_itemtxt25 = references_itemtxt[24],\
    references_itemtxt26 = references_itemtxt[25],\
    references_itemtxt27 = references_itemtxt[26],\
    references_itemtxt28 = references_itemtxt[27],\
    references_itemtxt29 = references_itemtxt[28],\
    references_itemtxt30 = references_itemtxt[29],\
    references_itemtxt31 = references_itemtxt[30],\
    references_itemtxt32 = references_itemtxt[31],\
    references_itemtxt33 = references_itemtxt[32],\
    references_itemtxt34 = references_itemtxt[33],\
    references_itemtxt35 = references_itemtxt[34],\
    references_itemtxt36 = references_itemtxt[35],\
    references_itemtxt37 = references_itemtxt[36],\
    references_itemtxt38 = references_itemtxt[37],\
    references_itemtxt39 = references_itemtxt[38],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])
 
@app.route("/contactus/")
def contactus():
    return render_template("contactus.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    telephonenr = telephonenr,\
    contactus_itemtxt1 = contactus_itemtxt[0],\
    contactus_itemtxt2 = contactus_itemtxt[1],\
    contactus_itemtxt3 = contactus_itemtxt[2],\
    contactus_itemtxt4 = contactus_itemtxt[3],\
    contactus_itemtxt5 = contactus_itemtxt[4],\
    contactus_itemtxt6 = contactus_itemtxt[5],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])
 
@app.route("/terms/")
def terms():
    return render_template("terms.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    terms_itemtxt1 = terms_itemtxt[0],\
    terms_itemtxt2 = terms_itemtxt[1],\
    terms_itemtxt3 = terms_itemtxt[2],\
    terms_itemtxt4 = terms_itemtxt[3],\
    terms_itemtxt5 = terms_itemtxt[4],\
    terms_itemtxt6 = terms_itemtxt[5],\
    terms_itemtxt7 = terms_itemtxt[6],\
    terms_itemtxt8 = terms_itemtxt[7],\
    terms_itemtxt9 = terms_itemtxt[8],\
    terms_itemtxt10 = terms_itemtxt[9],\
    terms_itemtxt11 = terms_itemtxt[10],\
    terms_itemtxt12 = terms_itemtxt[11],\
    terms_itemtxt13 = terms_itemtxt[12],\
    terms_itemtxt14 = terms_itemtxt[13],\
    terms_itemtxt15 = terms_itemtxt[14],\
    terms_itemtxt16 = terms_itemtxt[15],\
    terms_itemtxt17 = terms_itemtxt[16],\
    terms_itemtxt18 = terms_itemtxt[17],\
    terms_itemtxt19 = terms_itemtxt[18],\
    terms_itemtxt20 = terms_itemtxt[19],\
    terms_itemtxt21 = terms_itemtxt[20],\
    terms_itemtxt22 = terms_itemtxt[21],\
    terms_itemtxt23 = terms_itemtxt[22],\
    terms_itemtxt24 = terms_itemtxt[23],\
    terms_itemtxt25 = terms_itemtxt[24],\
    terms_itemtxt26 = terms_itemtxt[25],\
    terms_itemtxt27 = terms_itemtxt[26],\
    terms_itemtxt28 = terms_itemtxt[27],\
    terms_itemtxt29 = terms_itemtxt[28],\
    terms_itemtxt30 = terms_itemtxt[29],\
    terms_itemtxt31 = terms_itemtxt[30],\
    terms_itemtxt32 = terms_itemtxt[31],\
    terms_itemtxt33 = terms_itemtxt[32],\
    terms_itemtxt34 = terms_itemtxt[33],\
    terms_itemtxt35 = terms_itemtxt[34],\
    terms_itemtxt36 = terms_itemtxt[35],\
    terms_itemtxt37 = terms_itemtxt[36],\
    terms_itemtxt38 = terms_itemtxt[37],\
    terms_itemtxt39 = terms_itemtxt[38],\
    terms_itemtxt40 = terms_itemtxt[39],\
    terms_itemtxt41 = terms_itemtxt[40],\
    terms_itemtxt42 = terms_itemtxt[41],\
    terms_itemtxt43 = terms_itemtxt[42],\
    terms_itemtxt44 = terms_itemtxt[43],\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

@app.route("/login/")
def login():
    return render_template("/layouts/login.html",\
    projname1 = projname1,\
    projname2 = projname2,\
    projname3 = projname3)

#@app.route("/whyintro_cont/")
#def whyintro_cont():
#    return render_template("/content/whyintro_cont.html",\
#    itemtxt1 = itemtxt[0], itemtxt2 = itemtxt[1],\
#    itemtxt3 = itemtxt[2], itemtxt4 = itemtxt[3],\
#    itemtxt5 = itemtxt[4], itemtxt6 = itemtxt[5],\
#    itemtxt7 = itemtxt[6], itemtxt8 = itemtxt[7])

#@app.route("/foot/")
#def foot():
#    return render_template("/foot.html",\
#    projaddr1 = projaddr1,\
#    projaddr2 = projaddr2,\
#    projname = projname,\
#    copyrightmsg = copyrightmsg)

#  and newprojnum is null (in the cursor select below).
@app.route('/ajax/find-project', methods=['GET'])
def findproject():
    reqtype = request.args['reqtype']
    projectnumber = request.args['projectnumber']
    submissiondate = request.args['submissiondate']
    pilastname = request.args['pilastname']

    crsr.execute("SELECT count(*) FROM idea1 WHERE projnum = %s and DATE_FORMAT(subdate,'%%Y-%%m-%%d') = %s and pilastname=%s and newprojnum is null",(projectnumber, submissiondate, pilastname)) 
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
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    footer_itemtxt1 = footer_itemtxt[0],\
    footer_itemtxt2 = footer_itemtxt[1])

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
            INSERT INTO idea1 (projname,reqamount,newprojnum,orgname,orgwebaddr,schoolname,schoolwebaddr,pititle,picv,pifirstname,pimi,pilastname,pisuffix,piemail,pitele,piaddr1,piaddr2,picity,pistate,pizip,othertitle,otherfirstname,othermi,otherlastname,othersuffix,otheremail,othertele,otheraddr1,otheraddr2,othercity,otherstate,otherzip,irsletter_TF,budget_TF,confirmsent_TF,goal,description,aboutpeople,relevance,dissemination,projother) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            , (projname,reqamount,None,orgname,orgwebaddr,schoolname,schoolwebaddr,pititle,picv,pifirstname,pimi,pilastname,pisuffix,piemail,pitele,piaddr1,piaddr2,picity,pistate,pizip,othertitle,otherfirstname,othermi,otherlastname,othersuffix,otheremail,othertele,otheraddr1,otheraddr2,othercity,otherstate,otherzip,irsletter_TF,budget_TF,confirmsent_TF,goal,description,aboutpeople,relevance,dissemination,projother)
        )
        projnum = crsr.lastrowid;

        #update the existing project record with new project number
        crsr.execute("UPDATE idea1 SET newprojnum=%s WHERE projnum=%s", (projnum,existingprojnum))
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
            crsr.execute("UPDATE idea1 SET irsletter_TF=1, budget_TF=1 WHERE projnum=%s", (existingprojnum))
            conn.commit()


            flash('Document uploaded successfully.','success')
            return redirect(url_for('shareidea'))
        else:
            flash('One or more items is incorrect. Please try with valid files', 'error')
            
    return render_template('senddocument.html', form=form, existingprojnum=existingprojnum)

#from app import forms

if __name__=='__main__':
    # main()
    app.run(host='0.0.0.0', port=5000, debug=True)
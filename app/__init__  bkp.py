from flask import Flask
from flask import render_template
from datetime import datetime
import re
#import mysql.connector
from flaskext.mysql import MySQL
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'Bill'
app.config['MYSQL_DATABASE_PASSWORD'] = 'zz1357'
app.config['MYSQL_DATABASE_DB'] = 'ppp'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

conn = mysql.connect()
crsr = conn.cursor()

query1 = 'select * from projectinfo;'

crsr.execute(query1)
for (
    projname1, projname2, projname3,
    projaddr1, projaddr2,
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
plans_paratextbody = [[]]
plans_paratexthead = [[]]
possibilities_paratextbody = [[]]
possibilities_paratexthead = [[]]
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
scienceconverging_paratextbody = [[]]
scienceconverging_paratexthead = [[]]
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
    elif pagename == 'plans':
        if paratypecode == 'head':
            plans_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            plans_paratextbody.append(paratext)
    elif pagename == 'possibilities':
        if paratypecode == 'head':
            possibilities_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            possibilities_paratextbody.append(paratext)
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
    elif pagename == 'scienceconverging':  # Must do a separate section for EACH page.
        if paratypecode == 'head':
            scienceconverging_paratexthead.append(paratext) # add the pagename & string to the head list
        else:
            scienceconverging_paratextbody.append(paratext)
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

# home_paratextbody = []
# home_paratexthead = []

@app.route("/")
def home():
    return render_template("/home.html",\
    projname1 = projname1,\
    projname2 = projname2,\
    projname3 = projname3,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    leadpixinscr1 = leadpixinscr1,\
    leadpixinscr2 = leadpixinscr2,\
    leadpixinscr3 = leadpixinscr3,\
    projname = projname,\
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
    copyrightmsg = copyrightmsg,\
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
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/earlyyears/")
def earlyyears():
    return render_template("earlyyears.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    earlyyears_paratexthead1 = earlyyears_paratexthead[1],\
    earlyyears_paratextbody1 = earlyyears_paratextbody[1],\
    earlyyears_paratexthead2 = earlyyears_paratexthead[2],\
    earlyyears_paratextbody2 = earlyyears_paratextbody[2],\
    earlyyears_paratexthead3 = earlyyears_paratexthead[3],\
    earlyyears_paratextbody3 = earlyyears_paratextbody[3],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/parenting/")
def parenting():

    return render_template("parenting.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    parenting_paratexthead1 = parenting_paratexthead[1],\
    parenting_paratextbody1 = parenting_paratextbody[1],\
    parenting_paratexthead2 = parenting_paratexthead[2],\
    parenting_paratextbody2 = parenting_paratextbody[2],\
    parenting_paratexthead3 = parenting_paratexthead[3],\
    parenting_paratextbody3 = parenting_paratextbody[3],\
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
    ourwork_paratexthead5 = ourwork_paratexthead[5],\
    ourwork_paratextbody5 = ourwork_paratextbody[5],\
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

@app.route("/plans/")
def plans():
    return render_template("plans.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    plans_paratexthead1 = plans_paratexthead[1],\
    plans_paratextbody1 = plans_paratextbody[1],\
    plans_paratexthead2 = plans_paratexthead[2],\
    plans_paratextbody2 = plans_paratextbody[2],\
    plans_paratexthead3 = plans_paratexthead[3],\
    plans_paratextbody3 = plans_paratextbody[3],\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/possibilities/")
def possibilities():
    return render_template("possibilities.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    possibilities_paratexthead1 = possibilities_paratexthead[1],\
    possibilities_paratextbody1 = possibilities_paratextbody[1],\
    possibilities_paratextbody2 = possibilities_paratextbody[2],\
    possibilities_paratextbody3 = possibilities_paratextbody[3],\
    possibilities_paratextbody4 = possibilities_paratextbody[4],\
    possibilities_paratextbody5 = possibilities_paratextbody[5],\
    possibilities_paratextbody6 = possibilities_paratextbody[6],\
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
    joinin_paratextbody7 = joinin_paratextbody[7],\
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
    whyapply_paratextbody7 = whyapply_paratextbody[7],\
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
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/thankyou/")
def thankyou():
    return render_template("thankyou.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
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
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/references/")
def references():
    return render_template("references.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])

@app.route("/footnotes/")
def footnotes():
    return render_template("footnotes.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/contactus/")
def contactus():
    return render_template("contactus.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
    footer_paratextbody1 = footer_paratextbody[1],\
    footer_paratextbody2 = footer_paratextbody[2])
 
@app.route("/terms/")
def terms():
    return render_template("terms.html",\
    projname = projname,\
    copyrightmsg = copyrightmsg,\
    projaddr1 = projaddr1,\
    projaddr2 = projaddr2,\
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
if __name__=='__main__':
    main()
from SFF import app

#The following routes are in precisely the same sequence as the website menu. 

# Web page pieces for home page ------------------------------------

@app.route("/head/")
def head():
    return render_template("/head.html",\
    projname = projname)

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


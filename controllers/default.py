def index():
    return dict(message=T('Welcome to the Sahana Eden Deployment Tool'),right_sidebar_enabled=False)

def amazon():
    db.deployment.key.required = True
    form = SQLFORM(db.deployment)

    if form.process(session=None, formname=None).accepted:
        response.flash = "New Deployment Added"
        did = form.vars.id
        redirect(URL('deployment/%s' % did))
    elif form.errors:
        response.flash = "Form has errors"
    else:
        response.flash = "Please fill the form"
    return dict()

def linux():
    pass

def deployment():
    deployment = db.deployment(request.args(0)) or redirect(URL('error'))
    return dict(deployment=deployment)
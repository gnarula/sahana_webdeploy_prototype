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

def list_deployments():
    if len(request.args):
        page = int(request.args[0])
    else:
        page = 0
    items_per_page = 10
    limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    deployments = db().select(db.deployment.ALL, limitby=limitby)
    return dict(deployments=deployments, page=page, items_per_page=items_per_page)
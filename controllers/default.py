def index():
    response.logo=T('Sahana Web Deployment Tool')
    response.title=T('Sahana Web Deployment Tool')
    return dict(message=T('Welcome to the Sahana Eden Deployment Tool'),right_sidebar_enabled=False)

def amazon():
    response.title=T('Sahana Web Deployment Tool')
    response.logo=T('Sahana Web Deployment Tool')
    pass

def linux():
    pass
db = DAL('sqlite://storage.sqlite')

db.define_table(
    'deployment',
    Field('name', unique=True),
    Field('type'),
    Field('tier'),
    Field('key', 'upload', unique=True),
    Field('web_server'),
    Field('database'),
    format = '%(name)s'
    )

db.deployment.type.requires = IS_IN_SET(['amazon', 'generic'])
db.deployment.tier.requires = IS_IN_SET(['free', 'paid'])
db.deployment.web_server.requires = IS_IN_SET(['apache', 'cherokee'])
db.deployment.database.requires = IS_IN_SET(['mysql', 'postgresql'])

# TODO: Add Table for Configuration
from jsonstore.rest import JSONStore
# import sampleapp
from paste.deploy.config import ConfigMiddleware

def make_app(global_conf, **kw):
    conf = global_conf.copy()
    conf.update(kw)
    app = JSONStore(**conf)
    app = ConfigMiddleware(app, conf)
    return app


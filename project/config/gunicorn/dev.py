wsgi_app = "moe_count.wsgi:application"
loglevel = "debug"
workers = 2
bind = "0.0.0.0:8080"
reload = True
accesslog = errorlog = "/var/log/gunicorn/dev.log"
capture_output = True
pidfile = "/var/run/gunicorn/dev.pid"
daemon = False
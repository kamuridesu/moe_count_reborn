wsgi_app = "moe_count.wsgi:application"
loglevel = "warning"
workers = 2
bind = "0.0.0.0:8080"
reload = False
accesslog = errorlog = "/var/log/gunicorn/dev.log"
capture_output = True
pidfile = "/var/run/gunicorn/dev.pid"
daemon = False  # or else the container will exit
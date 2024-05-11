from flask_mail import Mail

MAIL = mail = Mail()

def register_extension(app):
    app.config["MAIL_SERVER"] = "smtppro.zoho.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_DEFAULT_SENDER"] = "rewards.r.us@dunderinitjob.me"
    app.config["MAIL_USERNAME"] = "rewards.r.us@dunderinitjob.me"
    app.config["MAIL_PASSWORD"] = "General_password123"

    MAIL.init_app(app)
    
    app.logger.info("Mail extension registered...")
    
    return app

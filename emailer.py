import webapp2
import json
import account
from google.appengine.api import mail

EMAIL_NAME = "NAME"
EMAIL_GRADE = "GRADE"
EMAIL_PEOPLE = "COMPANY_NAME"
EMAIL_COMPANY = "COMPANY"

DATA_COMPANY = "company_name"
DATA_PEOPLE = "company_people"
DATA_EMAIL_MAIN = "company_emails"
DATE_EMAIL_CC = "company_cc"

data = json.load(open("config/emails.json"))


def valid_emails(email_list):
    for email in email_list:
        if mail.is_email_valid(email):
            continue
        return False
    return True


def raw_email_parser(self):
    # replacer
    user = account.get_user(account.get_cookie(self))
    replace_info = {
        EMAIL_NAME: user.first_name + " " + user.last_name,
        EMAIL_GRADE: user.grade,
        EMAIL_PEOPLE: self.request.get(DATA_PEOPLE, default_value="ERR").strip(),
        EMAIL_COMPANY: self.request.get(DATA_COMPANY, default_value="ERR").strip()
    }

    status = "complete"
    for key, value in globals().items():
        if not "DATA_" in key or "_cc" in key:
            continue
        fail_value = "~*h8fnusd8*812*hjaisudnU*NU*7sdhfb*(*H"
        real_value = self.request.get(value, default_value=fail_value)
        if fail_value is not real_value and len(real_value) > 0:
            continue
        status = "incomplete"

    target = []
    cc_target = []
    if status is not "incomplete":
        target = [x.strip() for x in self.request.get(DATA_EMAIL_MAIN, default_value="").split(',')]
        cc_target = [x.strip() for x in self.request.get(DATE_EMAIL_CC, default_value="").split(',')]
        if not valid_emails(target):
            status = "invalid"

        if len(cc_target) > 0 and len(cc_target[0]) > 0:
            if not valid_emails(cc_target):
                status = "invalid"
        else:
            cc_target = None

    # replace
    email_info = data[self.request.get("email_type", "default").lower().strip()]
    email = email_info["data"]
    for key, value in replace_info.items():
        email = email.replace("${" + key + "}", value)

    return {"status": status, "email": email, "name": email_info["name"], "to": target, "cc": cc_target}


class EmailGenerator(webapp2.RequestHandler):
    def post(self):
        if account.unauthorized_request(self):
            return
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(raw_email_parser(self)))


class EmailSender(webapp2.RequestHandler):
    def post(self):
        if account.unauthorized_request(self):
            return
        email_content = raw_email_parser(self)
        if email_content["status"] is "complete":
            for email in email_content["to"]:
                message = mail.EmailMessage()
                message.sender = "STEMHacks <contact@stemhacks.com>"
                message.to = email
                print(email_content["cc"])
                if email_content["cc"] is not None:
                    message.cc = email_content["cc"]
                message.html = email_content["email"]
                message.subject = "%s at STEMHacks Hackathon!" % self.request.get(DATA_COMPANY,
                                                                                  default_value="ERR").strip()
                message.send()

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps({"result": email_content["status"]}))


class EmailTypes(webapp2.RequestHandler):
    def post(self):
        if account.unauthorized_request(self):
            return
        self.response.write(json.dumps(data.keys()))


app = webapp2.WSGIApplication([
    ('/email/send', EmailSender),
    ('/email/generate', EmailGenerator),
    ('/email/types', EmailTypes),
])

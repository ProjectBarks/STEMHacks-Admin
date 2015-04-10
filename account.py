import hashlib
import json
import uuid
import webapp2
from google.appengine.api import memcache

login_info = json.load(open("config/account.json"))


class User():
    def __init__(self, username, first_name, last_name, grade, cookie=""):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.cookie = cookie

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


def get_user(cookie):
    if not verify(cookie):
        return None

    usr = memcache.get(cookie)
    return User(usr, login_info[usr]["first"], login_info[usr]["last"], login_info[usr]["grade"], cookie)


def get_cookie(req):
    return req.request.cookies.get("account")


def unauthorized_request(req):
    if not verify(get_cookie(req)):
        req.error(401)
        return True
    return False


def verify(cookie):
    return memcache.get("ERR" if cookie is None else cookie) is not None


class Login(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username", default_value="ERR")
        if not username in login_info:
            self.error(401)
            return

        encrypt_pass = hashlib.sha512(self.request.get("password", default_value="ERR") + login_info[username]["salt"]).hexdigest()
        if encrypt_pass != login_info[username]["pass"]:
            self.error(401)
            return

        user_id = uuid.uuid1().hex
        memcache.set(user_id, username, 60 * 60 * 24)
        self.response.write(json.dumps({"cookie": user_id}))


class Logout(webapp2.RequestHandler):
    def post(self):
        cookie = get_cookie(self)
        if not verify(cookie):
            self.error(401)
            return
        memcache.delete(cookie)
        self.response.write(json.dumps({"result": "completed"}))


app = webapp2.WSGIApplication([
    ('/account/login', Login),
    ('/account/logout', Logout),
])
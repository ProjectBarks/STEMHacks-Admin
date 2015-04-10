import webapp2
import account


class Home(webapp2.RequestHandler):
    def get(self):
        valid = account.verify(account.get_cookie(self))
        self.response.write(open("site/" + ("admin" if valid else "login") + ".html").read())


app = webapp2.WSGIApplication([('/', Home)])
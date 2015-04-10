from google.appengine.api import channel
from google.appengine.api import memcache

import webapp2
import json
import account
import random
import string

commands = ["[connect]", "[disconnect]"]


def get_messages():
    msgs = memcache.get("msgs")
    if not msgs:
        msgs = []
    return msgs


def add_chatter(user_id, channel):
    chatters = get_accounts()
    chatters.append(user_id)
    memcache.set("connected_chatters", chatters, time=60 * 60 * 24)
    memcache.set("cha_" + user_id, channel, time=60 * 60 * 2)


def get_accounts():
    if memcache.get("connected_chatters"):
        updated_chatters = []
        for acc in memcache.get("connected_chatters"):
            if not memcache.get("cha_" + acc):
                continue
            updated_chatters.append(acc)
        memcache.set("connected_chatters", updated_chatters, 60 * 60 * 24)
        return updated_chatters
    else:
        return []


def get_channels():
    channels = []
    for acc in get_accounts():
        channels.append(memcache.get("cha_" + acc))
    return channels


def gen_id(N):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))


class Join(webapp2.RequestHandler):
    def post(self):
        if account.unauthorized_request(self):
            return
        chan = memcache.get("cha_" + account.get_cookie(self))
        if not chan:
            chan = channel.create_channel(gen_id(20))
            add_chatter(account.get_cookie(self), chan)
        self.response.write(json.dumps({"token": chan}))


class Broadcast(webapp2.RequestHandler):
    def post(self):
        if account.unauthorized_request(self):
            return
        msg = self.request.get("msg")
        if not msg:
            self.error(400)
            return
        if msg in commands:
            self.error(403)
            return
        user = account.get_user(account.get_cookie(self))
        serialized_msg = json.dumps({"name": user.full_name(), "msg": msg})
        for chan in get_channels():
            channel.send_message(chan, serialized_msg)
        messages = get_messages()[:100]
        messages.insert(0, serialized_msg)
        memcache.set("msgs", messages, 24 * 60 * 5)
        self.response.write(serialized_msg)


class History(webapp2.RequestHandler):
    def post(self):
        if account.unauthorized_request(self):
            return
        self.response.write(json.dumps(get_messages()))


class Disconnected(webapp2.RequestHandler):
    def post(self):
        if account.get_cookie(self):
            name = account.get_user(self)
            for chan in get_channels():
                channel.send_message(chan, json.dumps({"name": name, "msg": "[disconnect]"}))

app = webapp2.WSGIApplication([
    ('/chat/join', Join),
    ('/chat/send', Broadcast),
    ('/chat/history', History),
    ('/_ah/channel/disconnected/', Disconnected)
], debug=True)

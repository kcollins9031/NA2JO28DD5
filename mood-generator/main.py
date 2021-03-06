#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import datetime
import jinja2
import os
import random
import time
import webapp2
from google.appengine.ext import ndb

#setting up jinja
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class FeedbackComment(ndb.Model):
    name = ndb.StringProperty(required=False)
    comment = ndb.StringProperty(required=True)
    the_time = ndb.DateProperty(required=True)
    rating = ndb.IntegerProperty(required=True)

#homepage
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        html = template.render()
        self.response.write(html)
        # using letters to trigger the squares on our Trump pad?

class SadHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('sad.html')
        html = template.render({"mood": "Sad"})
        self.response.write(html)

class HappyHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('happy.html')
        html = template.render({"mood": "Happy"})
        self.response.write(html)

class LitHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('lit.html')
        html = template.render({"mood": "Lit"})
        self.response.write(html)

class TrumpHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('trump.html')
        html = template.render()
        self.response.write(html)

class FeedbackHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('feedback.html')
        html = template.render()
        self.response.write(html)

class PostFeedbackHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(get_feedback(self.request.get('name'), self.request.get('comment'), self.request.get('rating')))
    def post(self):
        self.response.write(get_feedback(self.request.get('name'), self.request.get('the_time'), self.request.get('rating')))

def get_feedback(name, comment, rating): # this isn't working yet
    the_time = datetime.datetime.fromtimestamp(time.time())
    # putting feedback into datastore
    if name == "":
        name = "Anonymous"

    feedback = FeedbackComment(name=name, comment=comment, the_time=the_time, rating=int(rating))
    feedback.put()

    template = jinja_environment.get_template('post_feedback.html')
    html = template.render()
    return html

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sad', SadHandler),
    ('/happy', HappyHandler),
    ('/lit', LitHandler),
    ('/trump', TrumpHandler),
    ('/feedback', FeedbackHandler),
    ('/thankyou', PostFeedbackHandler)
], debug=True)

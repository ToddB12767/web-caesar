#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
import webapp2
import caesar

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = "HELLOOOOO World?!"
        encrpyted_message = caesar.encrypt(message, 13)
        textarea = "<textarea>" + encrpyted_message + "</textarea>"
        submit = "<input type ='submit'/>"
        form = "<form>" + textarea + "<br>" + submit + "</form>"
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

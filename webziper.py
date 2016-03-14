'''
Created on Mar 13, 2016

@author: Gbenga
'''
import urllib2
import webapp2
import json


class MainPage(webapp2.RequestHandler):
    
    def get(self):
        self.response.out.write('<html><body><h1>Welcome to webzip</h1>')
        self.response.write('<h2>Please enter the zip code you will like to check</h2>')
        self.response.out.write('<form method="GET">')
        self.response.out.write('Zipcode:  <input name="Zipcode" type="text"><br>')
        self.response.out.write('<br>')
        self.response.out.write('City:  <input name="City" type="text"><br>')
        self.response.out.write('<br>')
        self.response.out.write('State: <input name="State" type="text">')
        self.response.out.write('<input type="submit"></input>')
        self.response.out.write('</form>')
        Zipcode = self.request.get("Zipcode")
        apikey = "8834c18fbba046abb1c9bc3f3095ba32"
#         self.City = self.Request.get('City')
#         self.State = self.Request.get('State')
        # urldata =  "https://congress.api.sunlightfoundation.com/legislators/"+str(Zipcode)
        urldata = request.get("https://congress.api.sunlightfoundation.com/legislators/locate?callback?",auth={
		'apikey' : apikey,
        'zip': Zipcode})
        weburl = urllib2.urlopen(urldata)
        self.response.out.write('<Here are the results>')
        self.response.out.write("webcode" + str(weburl.getcode()))
        if weburl.getcode()==200:
            self.response.out.write(weburl.read())
        self.response.out.write('</body></html>')
    
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
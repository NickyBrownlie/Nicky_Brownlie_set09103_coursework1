from flask import Flask, render_template
app = Flask(__name__, template_folder='/home/tc/Nicky_Brownlie_set09103_coursework1/templates')

from dataset import *



@app.route('/')
def homepage():
  return render_template('homepagetemplate.html')

@app.route('/allmovie/theshining/')
def movie():
  var1 = theshining
  return render_template('movie1.html', theshining=theshining, var1=var1)

@app.route('/allmovie/thedeparted/')
def movie1():
  var1 = thedeparted
  return render_template('movie1.html', thedeparted=thedeparted, var1=var1)

@app.route('/allmovie/thewolfofwallstreet/')
def movie2():
  var1 = thewolfofwallstreet
  return render_template('movie1.html', thewolfofwallstreet=thewolfofwallstreet, var1=var1)

@app.route('/allmovie/savingprivateryan/')
def movie3():
  var1 = savingprivateryan
  return render_template('movie1.html', savingprivateryan=savingprivateryan, var1=var1)

@app.route('/allmovie/fullmetaljacket/')
def movie4():
  var1 = fullmetaljacket
  return render_template('movie1.html', fullmetaljacket=fullmetaljacket, var1=var1)

@app.route('/allmovie/')
def allmovie():
  return render_template('allmovies.html', theshining=theshining,
                                            thedeparted=thedeparted,
                                            thewolfofwallstreet=thewolfofwallstreet,
                                            savingprivateryan=savingprivateryan,
                                            fullmetaljacket=fullmetaljacket)
@app.route('/directors/')
def directors():
  return render_template('directors.html', theshining=theshining,
                                           thedeparted=thedeparted,
                                           thewolfofwallstreet=thewolfofwallstreet,
                                          savingprivateryan=savingprivateryan,
                                          fullmetaljacket=fullmetaljacket)

if __name__==("__main__"):
  app.run(host='0.0.0.0', debug=True)

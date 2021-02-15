from flask import Flask,render_template,request,url_for,redirect
import data
app = Flask(__name__ )

@app.route('/')
@app.route('/crowdengine/')
def crowdengine():
    return render_template('mainpage.html',movie_list = data.movieslist)

@app.route('/pyhackons/')
def pyhackons():
    return render_template('pyhackons.html')

@app.route('/crowdengine/<string:name>')
def movie_name(name):
    
    if name not in data.movieslist:
        return render_template('error.html',error="Name Not Found")
    return render_template('movies.html' ,name = name)

@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html',error='Problem occured')

@app.errorhandler(404)
def page_not_found(e):
    
    return render_template('error.html',error='Page Not found')

@app.route('/crowdengine/pre/')
def pre():
    name = request.args.get('page')
    index = data.movieslist.index(name)
    name = data.page('pre',index)
    return redirect(url_for('movie_name',name = name) )
    
   

@app.route('/crowdengine/next/')
def next():
    name = request.args.get('page')
    index = data.movieslist.index(name)
    name = data.page('next',index)
    return redirect(url_for('movie_name',name = name))

@app.route('/crowdengine/write/',methods=["POST"])   
def write_db():
    
    if request.method == 'POST':
        
        movie = request.form["moviescount"]
        actor = request.form["name"]
        dur = request.form["screenduration"]
        insta = request.form["instagramfollowers"]
        dress = request.form["dressmatchmeter"]
        criticscore = request.form["criticscore"]
        consistency = request.form["consistency"]
        
        data.write(movie=movie,actor=actor,duration=dur,insta=insta,dress=dress,consistency=consistency,criticscore=criticscore)
        
    return render_template('movies.html',p="ok" ,name=actor)



if __name__ == "__main__":
    app.run(debug=True)

    

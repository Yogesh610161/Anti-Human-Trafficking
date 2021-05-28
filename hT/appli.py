from flask import Flask,render_template,request,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from send_email1 import send_email1



app=Flask(__name__,static_url_path='')
@app.route('/cols/<path:path>')
def send_css(path):
    return send_from_directory('cols',path)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:yogesh80@localhost/DR1'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://zciksrenmroncp:24933fc7857ef8e3b3968fef53990af0d628ed5297ab09a36c92b6a91fd21e09@ec2-54-235-177-183.compute-1.amazonaws.com:5432/deppeut66ahamj?sslmode=require'
db=SQLAlchemy(app)
class Data(db.Model):
    __tablename__="dataa"
    X=db.Column(db.Integer,primary_key=True,unique=True)
    Y=db.Column(db.Integer,unique=True)
    X1=db.Column(db.Integer,unique=True)
    Y1=db.Column(db.Integer,unique=True)
    location=db.Column(db.String(100))
    holder_name=db.Column(db.String(50))
    email=db.Column(db.String(50))


    def __init__(self,X,Y,X1,Y1,location,holder_name,email):
        self.X=X
        self.Y=Y
        self.X1=X1
        self.Y1=Y1
        self.location=location
        self.holder_name=holder_name
        self.email=email

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/success",methods=['POST'])
def success():
    if request.method=='POST':
        X=request.form["dna_rec1"]
        Y=request.form["dna_rec2"]
        X1=request.form["dna_rec3"]
        Y1=request.form["dna_rec4"]
        holder_name=request.form["hold_rec"]
        location=request.form["loc_rec"]
        email=request.form["email_rec"]
        send_email(X,Y,X1,Y1,holder_name,location,email)
        if db.session.query(Data).filter(Data.X==X).count()==0:
            data=Data(X,Y,X1,Y1,location,holder_name,email)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        else:
            return render_template('index.html',text="Same entry! Please put a new one.")
@app.route("/search")
def search():
        return render_template("search.html")
        #X=request.form["dn_re1"]
        #Y=request.form["dn_re2"]
        #X1=request.form["dn_re3"]
        #Y1=request.form["dn_re4"]
        #email=request.form["dn_email"]
        #obj=db.session.query(Data).filter_by(X='x').first()
        #vari=obj.Y
        #send_email1(vari)
        #return render_template("search.html")

@app.route("/wait",methods=['POST'])
def wait():
        x=request.form["dn_re1"]
        y=request.form["dn_re2"]
        x1=request.form["dn_re3"]
        y1=request.form["dn_re4"]
        email1=request.form["dn_email"]
        obj=db.session.query(Data).filter(Data.X==x).first()
        vari=obj.Y
        vari1=obj.location
        vari2=obj.X1
        vari3=obj.Y1
        vari4=obj.holder_name

        send_email1(vari,email1,vari1,vari2,vari3,vari4)
        return render_template("wait.html")

if __name__=="__main__":
    app.debug=True
    app.run()

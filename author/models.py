from flask_blog import db
#from blog.models import Post

class Author(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	fullname=db.Column(db.String(80))
	email=db.Column(db.String(35))
	username=db.Column(db.String(80))
	password=db.Column(db.String(60))
	is_author=db.Column(db.Boolean)
	
	posts= db.relationship('Post',backref='author',lazy='dynamic')
	
	def __init__(self, fullname, email,username,password,is_author=False):
		self.fullname=fullname
		self.email=email
		self.username=username
		self.password=password
		self.is_author=is_author
		
	def __repr__(self):
		return '<Author %r>' % self.username
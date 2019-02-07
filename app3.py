from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# db.init_app(app)

class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    # author = db.Column(db.String, nullable=False)
    # created_at = db.Column(db.String, nullable=False)
    
db.create_all()

@app.route("/")
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)
    
@app.route("/create")
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    """ ORM을 사용하여, 데이터를 저장한다."""
    
    a = Article(title=title, content=content)
    db.session.add(a)
    db.session.commit()
    return redirect('/')
    
@app.route("/delete/<int:article_id>")
def delete(article_id):
    """ 해당하는 글을 DB에서 삭제한다."""
    article = Article.query.get(article_id)
    db.session.delete(article)
    db.session.commit()
    
    return redirect("/")
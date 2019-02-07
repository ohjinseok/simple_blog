from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# db.init_app(app)

class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, nullable=False)
    
db.create_all()

def localtime():
    time_now = datetime.datetime.now()
    time_now = time_now + datetime.timedelta(hours=9)
    return time_now.strftime("%Y-%m-%d %H:%M:%S")
    
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/articles')
def articles():
    articles = Article.query.all()
    return render_template('articles.html', articles = articles)
    
@app.route('/articles/new')
def articles_new():
    return render_template('articles_new.html')
    
@app.route('/articles/create', methods=['POST'])
def articles_create():
    title = request.form['title']
    content = request.form['content']
    author = request.form['author']
    
    article = Article(title=title, content=content, author=author, created_at=localtime())
    db.session.add(article)
    db.session.commit()
    
    return redirect('/articles/{}'.format(article.id))
    
@app.route('/articles/<int:articles_id>')
def articles_detail(articles_id):
    article = Article.query.get(articles_id)
    return render_template('articles_detail.html', article=article)
    
@app.route('/articles/<int:articles_id>/edit')
def articles_edit(articles_id):
    article = Article.query.get(articles_id)
    return render_template('articles_edit.html', article=article)
    
@app.route('/articles/<int:articles_id>/update', methods=['POST'])
def articles_update(articles_id):
    title = request.form['title']
    content = request.form['content']
    author = request.form['author']
    
    article = Article.query.get(articles_id)
    article.title = title
    article.content = content
    article.author = author
    article.created_at = localtime()
    db.session.commit()
    
    return redirect('/articles/{}'.format(articles_id))
    
@app.route('/articles/<int:articles_id>/delete')
def articles_delete(articles_id):
    article = Article.query.get(articles_id)
    db.session.delete(article)
    db.session.commit()
    return redirect('/articles')
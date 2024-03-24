from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'gelecekbilimde'

# Basit bir blog veritabanı (şimdilik bir liste olarak tutuluyor)
blog_posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/post/<int:id>')
def post(id):
    post = None
    for p in blog_posts:
        if p['id'] == id:
            post = p
            break
    return render_template('post.html', post=post)

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = {'id': len(blog_posts) + 1, 'title': title, 'content': content}
        blog_posts.append(post)
        return redirect(url_for('index'))
    return render_template('new_post.html')

@app.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = None
    for p in blog_posts:
        if p['id'] == id:
            post = p
            break
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        return redirect(url_for('index'))
    return render_template('edit_post.html', post=post)

@app.route('/delete_post/<int:id>')
def delete_post(id):
    for index, post in enumerate(blog_posts):
        if post['id'] == id:
            del blog_posts[index]
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

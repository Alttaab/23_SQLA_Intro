"""Blogly application."""

from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, User, Post, Tag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "pass"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    return redirect('/posts')

# USER ROUTES


@app.route("/users")
def list_users():
    users = User.query.order_by(User.last_name).all()
    return render_template('users/user_list.html', users=users)


@app.route("/users/new", methods=['GET'])
def new_user_form():
    return render_template('users/new_user.html')


@app.route('/users/new', methods=["POST"])
def create_new_user():
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()
    flash(f" '{new_user.full_name}' profile created.")

    return redirect('/users')


@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.query.get(user_id)
    return render_template('users/user_details.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['GET'])
def edit_user_form(user_id):
    user = User.query.get(user_id)
    return render_template('users/edit_user.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    edited_user = User.query.get(user_id)

    edited_user.first_name = request.form['first_name']
    edited_user.last_name = request.form['last_name']
    edited_user.image_url = request.form['image_url'] or None

    db.session.add(edited_user)
    db.session.commit()
    flash(f" '{edited_user.full_name}' profile edited.")

    return redirect('/users')


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    user_full_name = user.full_name
    db.session.delete(user)
    db.session.commit()
    flash(f" '{user_full_name}' removed.")
    return redirect('/users')

# POST ROUTES


@app.route("/posts")
def list_posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('posts/post_list.html', posts=posts)


@app.route('/users/<int:user_id>/posts/new', methods=['GET'])
def new_post_form(user_id):
    user = User.query.get(user_id)
    tags = Tag.query.order_by(Tag.name).all()
    return render_template('posts/new_post.html', user=user, tags=tags)


@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def create_new_post(user_id):
    user = User.query.get(user_id)
    tag_ids = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    new_post = Post(
        title=request.form['title'],
        content=request.form['content'],
        user=user,
        tags=tags)

    db.session.add(new_post)
    db.session.commit()

    flash(f"Post '{new_post.title}' published.")

    return redirect(f'/posts/{new_post.id}')


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get(post_id)
    return render_template('posts/post_details.html', post=post)


@app.route('/posts/<int:post_id>/edit', methods=['GET'])
def edit_post_form(post_id):
    post = Post.query.get(post_id)
    tags = Tag.query.order_by(Tag.name).all()
    return render_template('posts/edit_post.html', post=post, tags=tags)


@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def update_post(post_id):
    edited_post = Post.query.get(post_id)

    edited_post.title = request.form['title']
    edited_post.content = request.form['content']

    tag_ids = [int(num) for num in request.form.getlist("tags")]
    edited_post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    db.session.add(edited_post)
    db.session.commit()
    flash(f"Post '{edited_post.title}' edited.")

    return redirect(f'/posts/{post_id}')


@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    post_title = post.title
    user_id = post.user.id
    db.session.delete(post)
    db.session.commit()
    flash(f"Post '{post_title}' removed.")
    return redirect(f'/users/{user_id}')

# TAG ROUTES


@app.route('/tags')
def list_tags():
    tags = Tag.query.order_by(Tag.name).all()
    return render_template('tags/tag_list.html', tags=tags)


@app.route('/tags/<int:tag_id>')
def posts_with_tag(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template('tags/tag_detail.html', tag=tag)


@app.route('/tags/new', methods=['GET'])
def new_tag_form():
    return render_template('tags/new_tag.html')


@app.route('/tags/new', methods=['POST'])
def create_new_tag():
    new_tag = Tag(name=request.form['name'])

    db.session.add(new_tag)
    db.session.commit()

    flash(f"Tag '{new_tag.name}' added.")

    return redirect('/tags')


@app.route('/tags/<int:tag_id>/edit', methods=['GET'])
def edit_tag_form(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template('tags/edit_tag.html', tag=tag)


@app.route('/tags/<int:tag_id>/edit', methods=['POST'])
def update_tag(tag_id):
    edited_tag = Tag.query.get(tag_id)

    edited_tag.name = request.form['name']

    db.session.add(edited_tag)
    db.session.commit()
    flash(f"Tag '{edited_tag.name}' edited.")

    return redirect(f'/tags/{tag_id}')


@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
    tag = Tag.query.get(tag_id)
    tag_name = tag.name
    db.session.delete(tag)
    db.session.commit()
    flash(f"Tag '{tag_name}' removed.")
    return redirect(f'/tags')

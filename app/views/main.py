from flask import render_template, redirect, url_for, flash, Blueprint, request, jsonify
from app import db
from app.forms import SignUpForm, LoginForm, EditProfileForm, PostForm, EditPostForm
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Post
from bcrypt import hashpw, gensalt
from datetime import datetime

main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET'])
def index():
    return render_template('landing.html')


@main_bp.route('/profile', methods=['GET'])
@login_required
def display_profile():
    return render_template('user/profile.html')


@main_bp.route('/edit-profile', methods=['POST', 'GET'])
def update_profile():
    form = EditProfileForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.password_hash = form.password_hash.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('main.display_profile'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.password_hash.data = current_user.password_hash
        
    return render_template('user/update-profile.html', form=form, current_user=current_user)


@main_bp.route('/post', methods=['POST', 'GET'])
@login_required
def post():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, user_id=current_user.user_id, created_at=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        flash('Your post has been added.')
        return redirect(url_for('auth.dashboard'))

    return render_template('main/post.html', form=form)


@main_bp.route('/update_post', methods=['POST'])
@login_required
def update_post():
    post_id = request.form['post_id']
    content = request.form['content']
    post = Post.query.get(post_id)
    if post and post.user_id == current_user.user_id:
        post.content = content
        db.session.commit()
        return jsonify({"success": True, "message": "Post updated successfully!"})
    return jsonify({"success": False, "message": "Post not found or unauthorized!"})



"""
@main_bp.route('/editpost/<int:id>', methods=['POST', 'GET'])
@login_required
def edit_post(id):
    form = EditPostForm()

    post = Post.query.get_or_404(id)

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.updated_at = form.updated_at.data
        db.session.commit()
        flash('Your post was edited successfully!')
        return redirect(url_for('auth.dashboard'))
    elif request.method=='GET':
        form.title.data = post.title
        form.content.data = post.content
        form.updated_at.data = post.updated_at

    return render_template('main/edit-post.html', id=id, post=post, form=form)
"""

@main_bp.route('/delete/<int:id>', methods=['GET'])
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post successfully deleted')
    return redirect(url_for("auth.dashboard"))


@main_bp.route('/about')
def about():
    return render_template('main/about.html')
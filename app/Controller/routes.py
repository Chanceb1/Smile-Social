from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user 
from config import Config

from app import db
from app.Model.models import Post, Tag
from app.Controller.forms import PostForm, SortForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    posts = Post.query.order_by(Post.timestamp.desc())
    sortPosts = SortForm()
    if sortPosts.validate_on_submit():
        if (sortPosts.my_posts.data==True): #if checkbox is selected, show only user's posts
            if (int(sortPosts.sort.data) == 4):
                posts = current_user.get_user_posts().order_by(Post.timestamp.desc())
            elif (int(sortPosts.sort.data) == 3):
                posts = current_user.get_user_posts().order_by(Post.title.desc())
            elif (int(sortPosts.sort.data) == 2):
                posts = current_user.get_user_posts().order_by(Post.likes.desc())
            elif (int(sortPosts.sort.data) == 1):
                posts = current_user.get_user_posts().order_by(Post.happiness_level.desc())

        else: #if checkbox is'nt selected sort normally
            if (int(sortPosts.sort.data) == 4): 
                posts = Post.query.order_by(Post.timestamp.desc())
            elif (int(sortPosts.sort.data) == 3):
                posts = Post.query.order_by(Post.title.desc())
            elif (int(sortPosts.sort.data) == 2):
                posts = Post.query.order_by(Post.likes.desc())
            elif (int(sortPosts.sort.data) == 1):
                posts = Post.query.order_by(Post.happiness_level.desc())

    return render_template('index.html', title="Smile Portal", posts=posts, form=sortPosts)

@bp_routes.route('/postsmile', methods=['GET', 'POST'])
@login_required
def postsmile():
    postForm = PostForm() 
    if postForm.validate_on_submit():
        newPost = Post(title=postForm.title.data, body=postForm.body.data, happiness_level=postForm.happiness_level.data, user_id=current_user.id)
        for t in postForm.tag.data:
            p = Tag.query.filter_by(name=t.name).first()
            newPost.tags.append(p)
        db.session.add(newPost)
        db.session.commit()
        flash('Your Smile post {} is created!'.format(postForm.title.data)) 
        return redirect(url_for('routes.index'))
    return render_template('create.html', form = postForm)  

@bp_routes.route('/like/<post_id>', methods=['POST'])
@login_required
def like(post_id):
    thePost = Post.query.filter_by(id = post_id).first()
    thePost.likes = thePost.likes + 1
    db.session.add(thePost)
    db.session.commit()
    return redirect(url_for('routes.index'))


@bp_routes.route('/delete/<post_id>', methods=['DELETE', 'POST'])
@login_required
def delete_post(post_id):
    thePost = Post.query.filter_by(id = post_id).first()
    if (thePost != None):
        for t in thePost.tags:
            thePost.tags.remove(t)
        db.session.add(thePost)
        db.session.commit()
        db.session.delete(thePost)
        db.session.commit()
        flash('Post successfully deleted')
    return redirect(url_for('routes.index'))
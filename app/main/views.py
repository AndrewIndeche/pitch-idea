from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import PitchForm,UpdateProfile,CommentForm
from .. import db,photos
from . import main
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitches=Pitch.query.all()
    Jokes = Pitch.query.filter_by(category = 'Jokes').all()
    Inspiration= Pitch.query.filter_by(category = 'Inspiration').all()
    Random = Pitch.query.filter_by(category = 'Random').all()
    return render_template('index.html', Jokes = Jokes ,Inspiration = Inspiration, pitches = pitches,Random= Random)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', form = form)

@main.route('/user/<uname>',methods=['GET','POST'])
@login_required
def profile(uname):
  user = User.query.filter_by(username=uname).first()
  pitches=Pitch.query.filter_by(user_id=user.id)
  if user is None:
    abort(404)
  title = f'{user.username}'
  return render_template('profile/profile.html',title=title,user = user,pitches=pitches)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/updateprofile.html',form =form)

@main.route('/categories/<pitch_category>')
def categories(pitch_category):
    pitch = Pitch.get_category(pitch_category)

    identification = Pitches.user_id
    posted_by = User.query.filter_by(id=identification).first()
    return render_template('categories.html', pitch=pitch, posted_by=posted_by)

@main.route('/comments/<int:pitch_id>', methods=['GET','POST'])
@login_required
def pitch_comments(pitch_id):
    comments = Comment.get_comments(pitch_id)

    pitch = Pitch.query.get(pitch_id)
    pitch_posted_by = pitch.user_id
    user = User.query.filter_by(id=pitch_posted_by).first()

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.pitch_comment.data
        new_comment = Comment(comment=comment, pitch_id=pitch_id, user_id=current_user.get_id())
        new_comment.save_c()
        return redirect(url_for('main.pitch_comments',pitch_id = pitch_id))

    return render_template('comments.html',form=form, comments=comments, pitch = pitch, user=user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

    return render_template('new_pitch.html',form =form)


@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(users = current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in pitch:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(users = current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))

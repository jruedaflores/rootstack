from flask import Flask, redirect, render_template, request, session, url_for
from flask_googlemaps import GoogleMaps, Map

from .session import get_token, set_token, get_username_token
from .models.user import User
from .services.job_service import get_jobs, get_job
from .services.user_service import get_access_token, get_profile

app = Flask(__name__)
app.secret_key = '1q2w3e4r5t6y7u8i9o'

GoogleMaps(app)
# GoogleMaps(app, key="")


@app.before_request
def setup():
    session.permanent = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        username = request.form['username']
        password = request.form['password']

        access_token = get_access_token(username, password)
        if access_token:
            set_token(username, access_token)
            return redirect(url_for('profile'))
    return render_template('login.html')


@app.route('/profile')
def profile():
    username, token = get_username_token()
    if username:
        user = User(username)
        if token:
            user = get_profile(user, token)
            if user.id:
                return render_template('profile.html', user=user)
    return redirect(url_for('index'))


@app.route('/jobs')
def jobs():
    token = get_token()
    if token:
        job_ids = get_jobs(token)
        headers = ['id', 'title', 'description', 'date', 'status', '']
        return render_template('jobs.html', headers=headers, objects=job_ids)
    return redirect(url_for('index'))


@app.route("/gmap")
def gmap():
    token = get_token()
    if token:
        job_ids = get_jobs(token)
        markers = []
        for job_id in job_ids:
            markers.append(job_id.get_marker())
        sndmap = Map(
            identifier="fullmap",
            varname="fullmap",
            style=(
                "height:100%;"
                "width:100%;"
                "top:0;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
            ),
            lat=20.219457379766567,
            lng=-9.759846594592345,
            markers=markers,
            zoom="2"
        )
        return render_template('gmap.html', sndmap=sndmap)
    return redirect(url_for('index'))


@app.route('/gmap/<job_id>')
def gmap_job(job_id):
    token = get_token()
    if token:
        job = get_job(job_id, token)
        markers = []
        if job:
            markers.append(job.get_marker())
            sndmap = Map(
                identifier="fullmap",
                varname="fullmap",
                style=(
                    "height:100%;"
                    "width:100%;"
                    "top:0;"
                    "left:0;"
                    "position:absolute;"
                    "z-index:200;"
                ),
                lat=markers[0]['lat'],
                lng=markers[0]['lng'],
                markers=markers,
                zoom="5"
            )
            return render_template('gmap.html', sndmap=sndmap)
    return redirect(url_for('index'))

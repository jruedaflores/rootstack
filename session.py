from flask import session


def set_token(username, access_token):
    session['username'] = (username, access_token)


def get_token():
    if 'username' in session:
        session_user = session['username']
        if session_user and len(session_user) >= 2:
            return session_user[1]
    return False


def get_username_token():
    if 'username' in session:
        session_user = session['username']
        user, token = False, False
        if session_user:
            user = session_user[0]
            if len(session_user) >= 2:
                token = session_user[1]
    return user, token

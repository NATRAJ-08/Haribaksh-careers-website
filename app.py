from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, get_user_by_username, add_user_to_db
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = b'\xea\x07b\x80\x12\xd2g\x12\x16\xb2\xbc\xc1\xea\\\x88/\xcdQ\t{\xc7\xf5r:'  # Use your generated secret key


@app.route('/')
def root():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    print('User ID in session:', session.get('user_id'))
    if 'user_id' not in session:
        return redirect(url_for('login'))

    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not found", 404
    return render_template('jobpage.html', job=job)


@app.route("/job/<int:id>/apply", methods=['POST'])
def apply_to_job(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('application_submitted.html',
                           application=data,
                           job=job)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = get_user_by_username(username)

        print('Login attempt:', username)

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            flash('Login successful!', 'success')
            print('Login successful, redirecting to home...')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
            print('Invalid login attempt.')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password,
                                                 method='pbkdf2:sha256')

        if get_user_by_username(username):
            flash('Username already exists', 'danger')
        else:
            add_user_to_db(username, hashed_password)
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

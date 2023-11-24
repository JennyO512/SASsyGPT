from flask import Flask, jsonify
from flask import Flask, render_template, request, jsonify, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import login_user, current_user, logout_user, login_required, LoginManager
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash
import os
import openai
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Initialize Flask-Login's LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # Return the user object from the user ID, typically from your database
    return User.query.get(int(user_id))


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    position = db.Column(db.String(300), nullable=True)
    letter = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)




# This route gets the base page, its' like the 1st page that shows up #changed from home to index
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base2.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user is not None:
            return "Username already exists. Please choose a different one."
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            session['logged_in'] = True # set the session
            return redirect(url_for('dashboard'))
    return render_template('login.html')    

@app.route("/logout")
def logout():
    logout_user()
    session.pop('user_id', None)
    session.pop('logged_in', None)  # Clear your custom session variable
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', username=user.username)



@app.route('/chat', methods=['POST', 'GET'])
def create_cover_letter():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        position = request.form.get('position')
        
        if position:  # Ensure position is not empty
            openai_api_key = os.environ.get('OPENAI_API_KEY')

            prompt = f"Act as a full stack IBM SAS JCL Mainframe programmer. Help debug SAS programs or provide code snippets of SAS with JCL. Here is the question: {position}"
            completions = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            letter = completions.choices[0].text   
            
            new_chat = Chat(user_id=session['user_id'], position=position, letter=letter)
            db.session.add(new_chat)
            db.session.commit()

            return render_template('base2.html', letter=letter, position=position)
        else:
            # Handle the case where position is empty
            flash('Please enter a question.', 'error')

    return render_template('base2.html')

    
        
        
    # Handling for GET request
    return render_template('base2.html')

# Example of fetching chat with pagination
@app.route('/chat/history')
def chat_history():
    page = request.args.get('page', 1, type=int)
    chats = Chat.query.filter_by(user_id=session['user_id']).paginate(page=page, per_page=25)
    return render_template('chat_history.html', chats=chats)

#@app.route('/')
#def index():
#    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=os.getenv("PORT", default=5000))

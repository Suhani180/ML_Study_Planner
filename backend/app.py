from flask import Flask, request, jsonify, render_template
from recommend import get_recommendation
from database import initialize_db, get_all_subjects

app = Flask(__name__)

db = initialize_db()

@app.route('/')
def home():
    subjects = get_all_subjects()
    return render_template('index.html', subjects=subjects)

@app.route('/<subject>')
def subject_page(subject):
    return render_template(f'{subject}.html', subject=subject)

@app.route('/<subject>/<difficulty>')
def difficulty_page(subject, difficulty):
    return render_template(f'{subject}_{difficulty}.html', subject=subject, difficulty=difficulty)

@app.route('/recommend', methods=['GET'])
def recommend():
    subject = request.args.get('subject')
    difficulty = request.args.get('difficulty')
    recommendations = get_recommendation(subject, difficulty)
    return jsonify({"resources": recommendations})

if __name__ == '__main__':
    app.run(debug=True)

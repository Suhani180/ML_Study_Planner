import pandas as pd

def load_data():
    data = [
        {"subject": "Math", "topic": "Algebra", "difficulty": "Easy", "resource": "https://math4kids.com/algebra"},
        {"subject": "Math", "topic": "Probability", "difficulty": "Medium", "resource": "https://math3kids.com/probability"},
        {"subject": "Math", "topic": "Geometry", "difficulty": "Hard", "resource": "https://advancedmath.com/geometry"},
        {"subject": "Science", "topic": "Physics", "difficulty": "Easy", "resource": "https://physicsfun.com"},
        {"subject": "Science", "topic": "Biology",
        "difficulty": "Medium", "resource":"https://biologyfun.com"},
        {"subject": "Science", "topic": "Chemistry", "difficulty": "Hard", "resource": "https://chemistryexperiments.com"}
    ]
    return pd.DataFrame(data)

df = load_data()

def get_recommendation(subject, difficulty):
    filtered = df[(df['subject'] == subject) & (df['difficulty'] == difficulty)]
    return filtered['resource'].tolist() if not filtered.empty else ["No resources found"]

from flask import Flask, request, render_template, redirect, url_for , flash

app = Flask(__name__, template_folder='templates')
app.secret_key = 'Here_is_hiden123'

# Home redirect
@app.route('/')
def index():
    return redirect(url_for('home'))

# Home page
@app.route('/home', methods=['GET'])
def home():
    data = {
        'name': 'Mohammed Alawsh',
        'interest': 'Back-end developer'
    }
    return render_template('home.html', data=data)

# Info page
@app.route('/info', methods=['GET'])
def info():
    info = {
        'degree': 'BS Software Engineer',
        'description': 'Passion software engineer building real-world projects with solid design and control',
        'Area of interest': {
            'interest-1': 'Backend development',
            'interest-2': 'AI features integration',
            'interest-3': 'Machine learning integration'
        }
    }
    return render_template('info.html', info=info)

# Skills page
@app.route('/skills', methods=['GET'])
def skills():
    skills = {
        'programming language': 'Python, HTML, CSS, JS, C++, Java',
        'framework': 'Flask, Django, React',
        'tech skill': {
            'DSA': 'Data structure design',
            'algorithm': 'Algorithm analysis',
            'DS': 'Data science (KNN, Naive Bayes, Decision Trees, Clustering)'
        }
    }
    return render_template('skills.html', skills=skills)

# Contact page (GET + POST)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
    contact_info = {
        'phone': '+92 3167949699',
        'email': 'm1.alawsh44@gmail.com'
    }
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_phNO = request.form.get('phNO')
        user_mess = request.form.get('message')

        if user_name and user_phNO:
            flash(f'Thanks for contacting us {user_name}, we will reach you soon.','success')
            return render_template('contact.html',contact_info=contact_info)

    return render_template('contact.html', contact_info=contact_info)


# Correct entry point
if __name__ == "__main__":
    app.run(debug=True)
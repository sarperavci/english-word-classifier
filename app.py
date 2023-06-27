from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for processing the form submission
@app.route('/search', methods=['POST'])
def search():
    text = request.form['text']
    words = {
        'B2': set(),
        'C1': set(),
        'C2': set()
    }

    # Read the word lists for each level
    with open('words/b2.txt', 'r') as b2_file, open('words/c1.txt', 'r') as c1_file, open('words/c2.txt', 'r') as c2_file:
        b2_words = set(word.strip() for word in b2_file.readlines())
        c1_words = set(word.strip() for word in c1_file.readlines())
        c2_words = set(word.strip() for word in c2_file.readlines())
    # Find words from each level in the provided text
    for word in text.split():
        if word in b2_words:
            words['B2'].add(word)
        if word in c1_words:
            words['C1'].add(word)
        if word in c2_words:
            words['C2'].add(word)

    return render_template('result.html', words=words)

if __name__ == '__main__':
    app.run()

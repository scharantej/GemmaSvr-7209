
# Import the necessary modules.
from flask import Flask, render_template

# Create a Flask application.
app = Flask(__name__)

# Define the route for the home page.
@app.route('/')
def home():
    # Render the index.html template.
    return render_template('index.html')

# Run the Flask application.
if __name__ == '__main__':
    app.run(debug=True)

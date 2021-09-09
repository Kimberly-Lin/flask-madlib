from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def display_form():
    """Generate and populate form with the list of prompts stories need"""
    prompts = silly_story.prompts
    return render_template("questions.html", prompts = prompts)

# After form submission from "/", get input, save them
# Redirect to /results which displays what silly_stories.generate should output

@app.get("/result")
def generate_story():
    """Move to /result directory, display generated story based on form input"""
    results = silly_story.generate(request.args)
    return render_template("story.html", generated_story = results)
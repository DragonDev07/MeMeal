import openai
import requests
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load .env file with keys
load_dotenv()

# Get and set the openai api key from the .env file
# openai.api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = "insert key here"

# Function to generate a recipe using the OpenAI API and inspiration from the edamam API
def generate_recipe(dietary_restrictions, allergies, query, user_input, edamam_data):
    prompt = f"The full input from the user is: {user_input} generate a recipe that is {' and '.join(dietary_restrictions)} and does not include {' or '.join(allergies)}. It should also include {' and '.join(query)}Make sure to include the name of the recipe at the top. Also, you can use the following recipe as inspiration: {edamam_data['hits'][0]['recipe']['label']} in the text please dont include line breaks and instead do <br>"
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(completions.choices[0].text)
    return completions.choices[0].text

def handle_input(user_input):
    input_list = user_input.split()
    dietary_restrictions = []
    allergies = []
    query = []
    for word in input_list:
        if word in ["alcohol-cocktail", "alcohol-free", "celery-free", "crustacean-free", "dairy-free", "DASH", "egg-free", "fish-free", "fodmap-free", "gluten-free", "immuno-supportive", "keto-friendly", "kidney-friendly", "kosher", "low-potassium", "low-sugar", "lupine-free", "Mediterranean", "mollusk-free", "mustard-free", "no-oil-added", "paleo", "peanut-free", "pescatarian", "pork-free", "red-meat-free", "sesame-free", "shellfish-free", "soy-free", "sugar-conscious", "sulfite-free", "tree-nut-free", "vegan", "vegetarian", "wheat-free"]:
                dietary_restrictions.append(word)
        elif word in ["peanut", "tree-nut", "shellfish", "fish", "dairy", "egg", "soy", "wheat"]:
                allergies.append(word)
        elif word in ["chicken", "beef", "pork", "fish", "vegetables", "soup", "asian", "chinese", "curry"]:
                query.append(word)
    
    if not dietary_restrictions:
        dietary_restrictions = ["alcohol-free"]
    if not allergies:
        allergies = ["peanut"]
    if not query:
        query = ["chicken"]

    edamam_app_id = "insert key here"
    edamam_app_key = "insert key here"

    edamam_url = f"https://api.edamam.com/api/recipes/v2?type=public&q={query[0]}&app_id={edamam_app_id}&app_key={edamam_app_key}&health={dietary_restrictions[0]}&excluded={allergies[0]}"

    print(edamam_url)

    edamam_response = requests.get(edamam_url)
    edamam_data = edamam_response.json()

    recipe = generate_recipe(dietary_restrictions, allergies, query, user_input, edamam_data)
    return recipe

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe_endpoint():
    data = request.get_json()
    recipe = handle_input(data['user_input'])

    return recipe

if __name__ == "__main__":
    app.run(debug=True)

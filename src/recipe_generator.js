// recipe_generator.js

function generate_recipe() {
    var user_input = document.getElementById("user_input").value;
    fetch('http://localhost:5000/generate_recipe', {
      method: 'POST',
      body: JSON.stringify({'user_input': user_input}),
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(response => response.text())
    .then(data => {
      document.getElementById("output").innerHTML = data;
    });
  }  
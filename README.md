<h1 align="center">
    <img src="https://github.com/DragonDev07/MeMeal/blob/main/images/MeMealLogo.png?raw=true" alt="Logo">
</h1>

<h1 align="center">MeMeal</h1>
<p align="center">Get recipes, tailored to your needs and dietary restrictions!</p>

<br>
<p align="center">
  <a href="#usage">Usage</a> •
  <a href="#inspiration">Inspiration</a> •
  <a href="#functionality">Functionality</a> •
  <a href="#build-process">Build Process</a> •
  <a href="#challenges">Challenges</a> •
  <a href="#whats-next">Whats next?</a> •
  <a href="#what-i-learnt">What I learnt</a> •
  <a href="#hackathon">Hackathon</a>
</p>
</br>

### Usage
To use the website, visit "https://dragondev07.github.io/MeMeal/src/index.html" and enter your restrictions!

### Inspiration
My inspiration for this project was not knowing what to eat for lunch when I was thinking about what project to make for this Hackathon.

### Functionality
At the moment, MeMeal will take an input from the user on the website, then identify the keywords about dietary restrictions, to then make a call to the Edamam API and get a recipe which is then fed into OpenAI's text-davinci-003 model as inspiration to generate a recipe.

### Build Process
The main backend for MeMeal is written in python, which I decided was the best option even though its not very fast as I would be easily able to request data from Enamam (Recipe API) and also would be able to access openai's library to make calls to their models very easily too. The backend is also currently deployed on Deta.sh

### Challenges
The biggest challenge that I faced during the hacking time was working on the frontend, and how to get that to connect to the backend which is written in python.

### Whats Next
In the future, I would like to continue working on this project to refine it and make it more dynamic. 
For example, right now, there are set words that the use for the program to be able to function correctly, but I could pass these through chatGPT to get me the response I want and get the users dietary restrictions.
I would also like to work on refining the frontend and making it work and look better.

### What I Learnt
During the hacking time I learnt how to make a route in python using Flask to be able to call functions from JS and make a frontend. 
This is what allowed me to be able to make the semblence of a website I have right now.

### Hackathon
This project was originally made for Treasure Hacks 3.0 Hackathon in 2023 <3

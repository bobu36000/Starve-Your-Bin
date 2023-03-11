from flask import Flask, render_template, request, redirect, url_for
import openai
import unittest


app = Flask(__name__)

#Defining functions and their directories


@app.route("/GenerateRecipe<servingSize><givenIngredients><otherIngredientsAllowed>")
def FindRecipe(servingSize, givenIngredients, otherIngredientsAllowed=False):
    
    if otherIngredientsAllowed:
        otherIngredientsAllowed = 'You are allowed to add ingredients not listed to the recipe.'
    
    else:
        otherIngredientsAllowed = 'You are not allowed to add other ingredients to the recipe.'
    
    openai.api_key = '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'
    completion = openai.Completion.create(engine = "text-davinci-003", prompt=f'Give me a recipe for x people that use ingredients y. Where x and y are, {servingSize} and {givenIngredients}. {otherIngredientsAllowed}. Any oven temperatures should be in celcius.', max_tokens = 2000)
    entireRecipe = completion.choices[0]['text']
    return(entireRecipe)



#Emailing system



#Login page python
@app.route("/login", )
def login():
    return render_template()

@app.route("/cake<usr>") 
def user(usr):
    return f"<h1>{usr}</h1>" 


#Defining HTML directories.

@app.route('/generateRecipe/')
def showRecipe():
    return render_template('showRecipe.html', content = FindRecipe(servingSize, givenIngredients, otherIngredientsAllowed=False))

@app.route('/AccountSettings.html/')
def AccountSettings():
    return render_template("AccountSettings.html")
@app.route('/ChooseIngredients.html/')
def ChooseIngredients():
    return render_template("ChooseIngredients.html")
@app.route('/Favourites.html/')
def Favourites():
    return render_template("Favourites.html")
@app.route('/Main.html/Friends.html/')
def Friends():
    return render_template("Friends.html")
@app.route('/FriendsSettings.html/')
def FriendsSettings():
    return render_template("FriendsSettings.html")
@app.route('/GeneratedRecipes.html/')
def GeneratedRecipes():
    return render_template("GeneratedRecipes.html")
@app.route('/idk.html/')
def idk():
    return render_template("idk.html")
@app.route('/Ingredients.html/')
def Ingredients():
    return render_template("Ingredients.html")
@app.route('/Main.html/')
def Main():
    if request.method == "POST":
        pass
    
    
    else:
        return render_template("Main.html")
@app.route('/Main.html/Pantry.html/')
def Pantry():
    return render_template("Pantry.html")
@app.route('/Main.html/Recipe.html/')
def Recipe():
    return render_template("Recipe.html")
@app.route('/Register.html/', methods=["POST", "GET"])
def Register():
    return render_template("Register.html")
@app.route('/ServingSize.html/')
def ServingSize():
    return render_template("ServingSize.html")
@app.route('/Main.html/Settings.html/')
def Settings():
    return render_template("Settings.html")
@app.route('/')
@app.route('/Welcome.html/')
@app.route('/Register.html/Welcome.html/')
def Welcome():
    return render_template("Welcome.html")




@app.route('/Login.html/', methods=["POST", "GET"])
def Login():
    if request.method == "POST":
        #Need to save this for future
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        
        return redirect(url_for("Main"))
    
    else:
        return render_template("Login.html")
    


######

if __name__ == "__main__":
    
    app.run()
    
#<p>{{content}}</p>
from flask import Flask
from Objects import *

burger_sauce = Recipe("Burger Sauce")
burger_sauce.add_ingredient(Ingredient("Mayo", 2, "kg"))
burger_sauce.add_ingredient(Ingredient("Ketchup", 0.5, "kg"))
burger_sauce.add_ingredient(Ingredient("Pickles", 0.2, "kg"))
burger_sauce.add_ingredient(Ingredient("Relish", 0.3, "kg"))

tartar = Recipe("Tartar")
tartar.add_ingredient(Ingredient("Mayo", 2, "kg"))
tartar.add_ingredient(Ingredient("Dill", 0.5, "kg"))
tartar.add_ingredient(Ingredient("Pickles", 0.2, "kg"))

pico = Recipe("Pico")
pico.add_ingredient(Ingredient("Tomatoes", 3, "kg"))
pico.add_ingredient(Ingredient("Onion", 2, "kg"))
pico.add_ingredient(Ingredient("Dill", 0.1, "kg"))
pico.add_ingredient(Ingredient("Cilantro", 0.2, "kg"))

today = Prep_List("june 11th 2022")
today.add_recipe(pico, 1)
today.add_recipe(tartar, 2)
today.add_recipe(burger_sauce, 2)

today.build_volumes_today()
today.print_volumes_today()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>" + str(today.print_volumes_today()) + "<p>"

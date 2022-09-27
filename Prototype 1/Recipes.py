from Objects import *

fajita_mix = Recipe("Fajita_Mix", 4)
fajita_mix.add_ingredient(Ingredient("Cornstarch", 15, 'ml'))
fajita_mix.add_ingredient(Ingredient("Chili Powder", 10, 'ml'))
fajita_mix.add_ingredient(Ingredient("Salt", 5, 'ml'))
fajita_mix.add_ingredient(Ingredient("Paprika",5 , 'ml'))
fajita_mix.add_ingredient(Ingredient("White Sugar",5 , 'ml'))
fajita_mix.add_ingredient(Ingredient("Onione Powder",2.5 , 'ml'))
fajita_mix.add_ingredient(Ingredient("Garlic Powder",2.5 , 'ml'))
fajita_mix.add_ingredient(Ingredient("Ground Cumin",2.5 , 'ml'))
fajita_mix.add_ingredient(Ingredient("Cayenne",1.25 , 'ml'))
#pico.list_ingredients()


#Serves 6
Hashe_beef = Recipe("Hashe de Beouf", 6)
Hashe_beef.add_procedure("""1.Fold the bay leaf, thyme, parsley stems,
 and peppercorns in a square of cheesecloth and tie the corners with
 a piece of kitchen twine. Leave one string long enough so that you can
 tie it to the handle of your pot to make it easier to retrieve.\n
3. In a heavy-bottomed saucepan, melt the butter over a medium heat
 until it becomes frothy.\n
4. Add the mirepoix—onions, carrots, and celery—and sauté for a few
 minutes until lightly browned. Don't let it burn.\n
5. With a wooden spoon, stir the flour into the mirepoix a little bit
 at a time until it is fully
 incorporated and forms a thick paste (this is your roux).\n
6. Lower the heat and cook the roux for another 5 minutes or so, until
 it just starts to take on a very light brown color. Again, don't let it burn.\n
7. Using a wire whisk, slowly add the stock and tomato purée to the roux,
 whisking vigorously to make sure it's free of lumps.\n
8. Bring to a boil, lower the heat, and add the sachet. Simmer for about 50 minutes,
 or until the total volume has reduced by about 1/3, stirring frequently to make
 sure the sauce doesn't scorch at the bottom of the pan.\n
9. Use a ladle to skim off any impurities that rise to the surface. \n
10. Remove the sauce from the heat and retrieve the sachet. \n
11. For an extra smooth consistency, carefully pour the sauce through a
wire mesh strainer lined with a piece of cheesecloth.\n
12. If you won't be serving the sauce right away, keep it covered and warm until
you're ready to use it. Otherwise, serve hot and enjoy!

It's commonly used as a starting point for a number of sauces, most famously demi-glace.
To make demi-glace, you'd combine equal parts espagnole and brown stock along with
additional mirepoix (and probably another sachet) and reduce it by half (hence demi).\n""")
Hashe_beef.add_ingredient(Ingredient("Bay Leaf", 1, 'ml'))
Hashe_beef.add_ingredient(Ingredient("Dried Thyme", 2.5, 'ml'))
Hashe_beef.add_ingredient(Ingredient("Parsley Stems", 4, 'ml'))
Hashe_beef.add_ingredient(Ingredient("Whole Black Peppercorns", 8, 'ml'))
Hashe_beef.add_ingredient(Ingredient("Margarine", 30, 'ml'))
Hashe_beef.add_ingredient(Ingredient("Diced Onion", 125, 'ml'))
Hashe_beef.add_ingredient(Ingredient("Diced Carrot", 62.5, 'ml'))
Hashe_beef.add_ingredient(Ingredient("Diced Celery", 62.5, 'ml'))
Hashe_beef.add_ingredient(Ingredient("AP Flour", 30, 'ml'))
Hashe_beef.add_ingredient(Ingredient("Brown Stock (beef)", 750, 'ml'))
Hashe_beef.add_ingredient(Ingredient("Tomatoe Puree", 30, 'ml'))



deCabRoll = Recipe("Deconstructed Cabbage Roll", 6)
deCabRoll.add_procedure("""1. Cook beef and onions till brown and crumbly (~ 7 mins)
2. Drain grease then add rest of ingredients and bring to boil
3. reduce to simmer, cover and cook for ~30 minutes""")
deCabRoll.add_ingredient((Ingredient("Ground Beef", 1000, 'ml')))
deCabRoll.add_ingredient((Ingredient("Large Onion", 1, 'each')))
deCabRoll.add_ingredient((Ingredient("Head of Cabbage", 1, 'each')))
deCabRoll.add_ingredient((Ingredient("Diced Tomatoes", 29, 'ounces')))
deCabRoll.add_ingredient((Ingredient("Tomatoe Sauce", 8, 'ounces')))
deCabRoll.add_ingredient((Ingredient("Water", 0.5, 'cup')))
deCabRoll.add_ingredient((Ingredient("Garlic Cloves", 2, 'each')))
deCabRoll.add_ingredient((Ingredient("Salt", 10, 'ml')))
deCabRoll.add_ingredient((Ingredient("Black Pepper", 5, 'ml')))

pieBars = Recipe("Pie Bars", 16)
pieBars.add_procedure("""1. Preheat oven to 350f
2. Cream butter, sugar, and salt until light and fluffy
3. Add eggs one at a time, beating well after each egg. Beat in extracts.
4. Gradually add in flour
5. Spread dough to cover bottom of greased parchment lined baking sheet
6. Spread pie filling on top
7. Drop dollops of dough over filling. Bake for 30-35 minutes till golden brown
8. Let cool completeley. Cut in to portions.
(Optional icing)
9. Mix confectioners sugar, extracts and enough milk till silky consistency is achieved.
10. Drizzle mixture ontop of the bars.""")
pieBars.add_ingredient((Ingredient("Butter", 1, 'cup')))
pieBars.add_ingredient((Ingredient("Sugar", 2, 'cup')))
pieBars.add_ingredient((Ingredient("Salt", 5, 'ml')))
pieBars.add_ingredient((Ingredient("Eggs", 4, 'each')))
pieBars.add_ingredient((Ingredient("Vanilla Extract", 5, 'ml')))
pieBars.add_ingredient((Ingredient("Flour", 3, 'cup')))
pieBars.add_ingredient((Ingredient("Pie Filling", 21, 'ounce')))

brownies = Recipe("Brownies", 16)
brownies.add_procedure("""
1. Preheat oven to 350 degrees F (175 degrees C).
Grease and flour an 8-inch square pan
2. Melt butter. Stir in sugar, eggs, and vanilla.
3. Beat in cocao, flour, salt, and baking powder until all ingredienets are wet.
4. Bake for 25 to 30 minutes.
""")
brownies.add_ingredient((Ingredient("Butter", 0.5, 'cup')))
brownies.add_ingredient((Ingredient("Sugar", 1, 'cup')))
brownies.add_ingredient((Ingredient("Salt", 1/4, 'tsp')))
brownies.add_ingredient((Ingredient("Eggs", 2, 'each')))
brownies.add_ingredient((Ingredient("Vanilla Extract", 1, 'tsp')))
brownies.add_ingredient((Ingredient("Flour", 0.5, 'cup')))
brownies.add_ingredient((Ingredient("Cocao Powder", 1/3, 'cup')))
brownies.add_ingredient((Ingredient("Baking Powder", 1/4, 'tsp')))

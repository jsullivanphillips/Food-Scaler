from Objects import *
from Recipes import *

today = Prep_List("july 23rd 2022")
today.add_recipe(Hashe_beef, 20)
#today.list_recipes()

today.build_volumes_today()
today.list_recipes()
print(today.print_volumes_today())
Hashe_beef.print_procedure()

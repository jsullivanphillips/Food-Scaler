class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    def __str__(self):
        return str(self.name) + " " + str(self.quantity) + " " + str(self.unit)

    def multiply(self, operator):
        self.quantity = self.quantity * operator
        self.clean()

    def clean(self):
        if self.unit == 'tsp':
            if self.quantity > 3:
                self.unit = 'tbspn'
                self.quantity = self.quantity / 3
        if self.unit == 'tbspn':
            if self.quantity > 4:
                self.unit = 'cup'
                self.quantity = self.quantity / 4
        if self.unit == 'ounces':
            if self.quantity > 16:
                self.unit = 'pounds'
                self.quantity = self.quantity / 16
        if self.unit == 'ml':
            if self.quantity > 250:
                self.unit = "cup"
                self.quantity = self.quantity / 250
        if (self.unit == "cup"):
            if self.quantity > 4:
                self.unit = "liter(s)"
                self.quantity = self.quantity / 4


class Recipe:
    def __init__(self, name, serves):
        self.name = name
        self.ingredients = []
        self.serves = serves
        self.procedure = ''
    def __str__(self):
        self.print_conversion_chart()
        self.print_ingredients()
        self.print_procedure()
        return ''
    # constructors
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    def add_procedure(self, procedure):
        self.procedure = procedure
    # math functions
    def multiply_recipe(self, operator):
        for ingredient in self.ingredients:
            ingredient.multiply(operator)
    def modify_to_serve(self, num_diners):
        operator = round(num_diners / self.serves)
        self.multiply_recipe(operator)
        self.serves = num_diners
    # print functions
    def print_conversion_chart(self):
        print("""
        CONVERSION CHART
        ----------------
        1 tsp    ==  5    ml
        1 tbspn  ==  15   ml
        1/4 cup  ==  ~60  ml
        1/2 cup  ==  ~120 ml
        1 cup    ==  250  ml
        1 liter  ==  4    cups    == 1000 ml
        1 gallon ==  3.8
        1 pound  ==  16   ounce\n
        ||""" + self.name + " for " + str(self.serves) + "||\n")
    def print_ingredients(self):
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(ingredient)
    def print_procedure(self):
        print(
        """            ----------------
            P R O C E D U R E
            ----------------""")
        print(self.procedure)

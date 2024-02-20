import json
import sys


class RecipeWriter:
    def __init__(self) -> None:
        self.read_file()

        self.ingredients = {}
        self.method_steps = []
        self.recipe_data = {}
        self.running = True

    def get_name_and_category(self):
        self.name = input("Name of recipe\n")
        if self.name.casefold() == "q":
            self.exit_program()
        self.category = input("\nCategory of recipe\n")
        if self.category.casefold() == "q":
            self.exit_program()

    def get_ingredients(self):
        ingredient = input("\nName ingredient\n")
        if ingredient.casefold() == "q":
            self.exit_program()
        if not ingredient.casefold() == "n":
            quantity = input("\nName quantity\n")
            if quantity.casefold() == "q":
                self.exit_program()
            if not quantity.casefold() == "n":
                self.ingredients[ingredient.casefold()] = quantity
                self.get_ingredients()

    def get_method_steps(self):
        step = input("\nDescribe step.\n")
        if step.casefold() == "q":
            self.exit_program()
        if not step.casefold() == "n":
            self.method_steps.append(step)
            self.get_method_steps()

    def set_recipe_data(self):
        # self.recipe_data["name"] = self.name
        self.recipe_data["category"] = self.category.casefold()
        self.recipe_data["ingredients"] = self.ingredients
        self.recipe_data["method"] = self.method_steps

    def read_file(self):
        with open("recipes.json", "r") as file:
            self.recipe_list = json.load(file)
        print(self.recipe_list)

    def write_to_file(self):
        if self.running:
            self.recipe_list[self.name.casefold()] = self.recipe_data
            with open("recipes.json", "w") as file:
                json.dump(self.recipe_list, file)

    def run(self):
        self.start_message()
        self.get_name_and_category()
        self.get_ingredients()
        self.get_method_steps()
        self.set_recipe_data()
        self.write_to_file()

    def start_message(self):
        print("\n" + 60 * "=" + "\n")
        print("\033[1m" + "Recipe writer running." + "\033[0m" + "\n")
        print("Press q + enter to quit.")
        print("Press n + enter to continue from ingredients or method.")
        print("\n" + 60 * "=" + "\n")

    def exit_program(self):
        print("\nStopped running.\n")
        sys.exit()


recipe_writer = RecipeWriter()
recipe_writer.run()

import json


class RecipeFileGenerator:
    def __init__(self, file_name) -> None:
        self.name = file_name
        self.get_json_data()
        # print(self.ingredients)
        # print(self.method_steps)

    def get_json_data(self):
        with open(f"testing_file_generation/{self.name}.json", "r") as file:
            self.recipe_dict = json.load(file)
        self.category = self.recipe_dict["category"]
        self.subcategory = self.recipe_dict["subcategory"]
        self.ingredients = self.recipe_dict["ingredients"]
        self.method_steps = self.recipe_dict["method"]
        self.tips = self.recipe_dict["tips"]

    def create_method_string(self):
        steps_string = ""
        for step in self.method_steps:
            steps_string += f"<li>{step}</li>"
        self.method_string = f'<div class="container method-container"><h2>Method</h2><ol class="method-list">{steps_string}</ol></div>'

    def create_ingredients_string(self):
        rows = ""
        for ingredient in self.ingredients.items():
            row = f"<tr><td>{ingredient[0].capitalize()}</td><td>{ingredient[1]}</td></tr>"
            rows += row
        self.ingredients_string = f'<div class="container ingredients-container"><h2>Ingredients</h2><table class="ingredients-table">{rows}</table></div>'

    def create_tips_string(self):
        general_string = ""
        links_string = ""
        for i in self.tips["general"]:
            general_string += f"<p>{i}</p>"
        for i in self.tips["links"].items():
            links_string += f'<a href="{i[1]}">{i[0]}</a>'

        print(self.tips)
        self.tips_string = f'<div class="container tips-container"><h2>Tips</h2>{general_string}{links_string}</div>'

    def create_file(self):
        with open(f"{self.category}/{self.subcategory}/{self.name}.html", "w") as file:
            file.write(
                f"""<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="../../css/recipe_pages.css" />
    <title>{self.name.title()}</title>
  </head>
  <body>
  <div class='main-container'>
  <div class = 'container title-container'>
    <h1>{self.name.title()}</h1>
    <p class='description'>temp desc</p>
    </div>
    {self.ingredients_string}
    {self.method_string}
    {self.tips_string}
    </div>
  </body>
</html>"""
            )

    def run(self):
        self.create_ingredients_string()
        self.create_method_string()
        self.create_tips_string()
        self.create_file()


bob = RecipeFileGenerator("test_dict")
bob.run()

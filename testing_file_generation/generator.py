import json


class FileGenerator:
    def __init__(self, file_name) -> None:
        self.name = file_name
        self.get_json_data()
        print(self.ingredients)
        print(self.method_steps)

    def get_json_data(self):
        with open(f"testing_file_generation/{self.name}.json", "r") as file:

            self.recipe_dict = json.load(file)
        self.ingredients = self.recipe_dict["ingredients"]
        self.method_steps = self.recipe_dict["method"]

    def create_method_string(self):
        steps_string = ""
        for step in self.method_steps:
            steps_string += f"<li>{step}</li>"
        self.method_string = f"<ol class='method-list'>{steps_string}</ol>"

    def create_ingredients_string(self):
        rows = ""
        for ingredient in self.ingredients.items():
            row = f"<tr><td>{ingredient[0].capitalize()}</td><td>{ingredient[1]}</td></tr>"
            rows += row
        self.ingredients_string = f"<table class='ingredients-table'>{rows}</table>"
        print(self.ingredients_string)

    def create_file(self):
        with open(f"testing_file_generation/files/{self.name}.html", "w") as file:
            file.write(
                f"""<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{self.name.title()}</title>
  </head>
  <body>
  <div class='main-container'>
    <h1>{self.name.title()}</h1>
    <div class="ingredients-container">
    {self.ingredients_string}</div>
    <div class="method-container">
    {self.method_string}</div></div>
    
  </body>
</html>"""
            )

    def run(self):
        self.create_ingredients_string()
        self.create_method_string()
        self.create_file()


bob = FileGenerator("test_dict")
bob.run()

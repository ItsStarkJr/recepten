import string
from datetime import date
from tkinter import *

import customtkinter
from utils import check_string_is_empty, strip_casefold, write_to_json_file


class AddRecipe:
    def __init__(self) -> None:

        self.widget_background_colour = "#101010"
        self.app_setup()
        self.recipe_data = {}

    def app_setup(self):
        customtkinter.set_appearance_mode(
            "dark"
        )  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme(
            "blue"
        )  # Themes: "blue" (standard), "green", "dark-blue"

        self.root = customtkinter.CTk()
        self.root.geometry("1280x1180+300+100")
        self.root.title("Add Recipe")
        self.root.bind("<Escape>", self.close_app)

        self.frame_1 = customtkinter.CTkFrame(master=self.root)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_1 = customtkinter.CTkLabel(
            master=self.frame_1,
            justify=customtkinter.LEFT,
            text="Enter new line to separate ingredients/method steps.             Separate ingredients and their amount by a forward slash (/).",
            text_color="grey",
        )
        self.label_1.pack(pady=10, padx=10)

        # Title frame

        self.title_frame = customtkinter.CTkFrame(self.frame_1)
        self.title_frame.pack(pady=10)

        self.name_entry = customtkinter.CTkEntry(
            master=self.title_frame,
            placeholder_text="Name",
            width=325,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            border_width=0,
            height=40,
        )
        self.category_entry = customtkinter.CTkEntry(
            master=self.title_frame,
            placeholder_text="Category",
            width=325,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            height=40,
            border_width=0,
        )
        self.subcategory_entry = customtkinter.CTkEntry(
            master=self.title_frame,
            placeholder_text="Subcategory",
            width=325,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            height=40,
            border_width=0,
        )
        self.description_label = customtkinter.CTkLabel(
            master=self.title_frame,
            text="Description (case sensitive):",
            text_color="grey",
        )
        self.description_box = customtkinter.CTkTextbox(
            master=self.title_frame,
            width=1020,
            height=150,
            fg_color=self.widget_background_colour,
            corner_radius=0,
        )

        self.description_box.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.description_label.grid(row=1, column=1, padx=10)
        self.name_entry.grid(row=0, column=0, padx=10, pady=10)
        self.category_entry.grid(row=0, column=1, padx=10, pady=10)
        self.subcategory_entry.grid(row=0, column=2, padx=10, pady=10)

        # Input frame

        self.input_frame = customtkinter.CTkFrame(self.frame_1)
        self.input_frame.pack(pady=10)

        self.buttons_frame = customtkinter.CTkFrame(self.frame_1)
        self.buttons_frame.pack(pady=10)

        self.ingredients_label = customtkinter.CTkLabel(
            master=self.input_frame, text="Ingredients:", text_color="grey"
        )
        self.ingredients_box = customtkinter.CTkTextbox(
            master=self.input_frame,
            width=500,
            height=500,
            corner_radius=0,
            fg_color=self.widget_background_colour,
        )

        self.method_label = customtkinter.CTkLabel(
            master=self.input_frame, text="Method (case sensitive):", text_color="grey"
        )
        self.method_box = customtkinter.CTkTextbox(
            master=self.input_frame,
            width=500,
            height=500,
            corner_radius=0,
            fg_color=self.widget_background_colour,
        )

        self.ingredients_label.grid(row=1, column=0, padx=10)
        self.method_label.grid(row=1, column=1, padx=10)
        self.ingredients_box.grid(row=2, column=0, padx=10, pady=10)
        self.method_box.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        self.preview_button = customtkinter.CTkButton(
            master=self.buttons_frame,
            command=self.create_preview_window,
            text="Preview",
            corner_radius=0,
            fg_color="#252525",
            hover_color="#404040",
        )
        self.submit_button = customtkinter.CTkButton(
            master=self.buttons_frame,
            command=self.submit,
            text="Submit",
            corner_radius=0,
            fg_color="#252525",
            hover_color="#404040",
        )

        self.preview_button.grid(row=0, column=0, padx=10, pady=10)
        self.submit_button.grid(row=0, column=1, padx=10, pady=10)

    def get_name(self):
        self.name = strip_casefold(self.name_entry.get())
        self.recipe_data["name"] = self.name

    def get_date(self):
        self.recipe_data["date"] = date.today().strftime("%d/%m/%Y")

    def get_category(self):
        self.recipe_data["category"] = strip_casefold(self.category_entry.get())

    def get_subcategory(self):
        self.recipe_data["subcategory"] = strip_casefold(self.subcategory_entry.get())

    def get_description(self):
        self.recipe_data["description"] = self.description_box.get(0.0, "end").strip()

    def get_ingredients(self):
        processed_ingredients = {}
        temp_ingredients = self.ingredients_box.get(0.0, "end").strip().split("\n")
        temp_processed_ingredients = [
            i for i in temp_ingredients if not check_string_is_empty(i)
        ]
        for i in temp_processed_ingredients:
            try:
                split_ingredient_amount = i.split("/")

                processed_ingredients[strip_casefold(split_ingredient_amount[0])] = (
                    strip_casefold(split_ingredient_amount[1])
                )
            except:
                processed_ingredients[strip_casefold(i)] = ""

        self.recipe_data["ingredients"] = processed_ingredients

    def get_method(self):
        temp_steps = self.method_box.get(0.0, "end").strip().split("\n")
        processed_method = [
            i.strip() for i in temp_steps if not check_string_is_empty(i)
        ]

        self.recipe_data["method"] = processed_method

    def create_preview_window(self):
        self.get_recipe_data()
        ingredients_preview_string=""
        for i in self.recipe_data["ingredients"].items():
            ingredients_preview_string+=f"{i[0]} {i[1]}\n"
        method_preview_string=""
        for i, step in enumerate(self.recipe_data["method"]):
            method_preview_string+=f"{i+1}. {step}\n"
        preview_window = customtkinter.CTkToplevel(self.root)
        preview_window.geometry("768x1180+2230+100")
        preview_window.title("Preview")
        self.preview_name_label = customtkinter.CTkLabel(
            master=preview_window, text=f"Name:\n{self.recipe_data["name"]}", text_color="grey", justify="left"
        )
        self.preview_category_label = customtkinter.CTkLabel(
            master=preview_window, text=f"Category:\n{self.recipe_data["category"]}", text_color="grey", justify="left"
        )
        self.preview_subcategory_label = customtkinter.CTkLabel(
            master=preview_window, text=f"Subcategory:\n{self.recipe_data["subcategory"]}", text_color="grey", justify="left"
        )
        self.preview_description_label = customtkinter.CTkLabel(
            master=preview_window, text=f"Description:\n{self.recipe_data["description"]}", text_color="grey", justify="left"
        )
        self.preview_ingredients_label = customtkinter.CTkLabel(
            master=preview_window, text=f"Ingredients:\n{ingredients_preview_string}", text_color="grey", justify="left"
        )
        self.preview_method_label = customtkinter.CTkLabel(
            master=preview_window, text=f"Method:\n{method_preview_string}", text_color="grey", justify="left"
        )
        self.preview_name_label.pack(pady=10, padx=10, anchor="w")
        self.preview_category_label.pack(pady=10, padx=10, anchor="w")
        self.preview_subcategory_label.pack(pady=10, padx=10, anchor="w")
        self.preview_description_label.pack(pady=10, padx=10, anchor="w")
        self.preview_ingredients_label.pack(pady=10, padx=10, anchor="w")
        self.preview_method_label.pack(pady=10, padx=10, anchor="w")

    def submit(self):
        self.get_recipe_data()
        write_to_json_file(self.name, self.recipe_data, "json_data/recipes")

    def get_recipe_data(self):
        self.get_name()
        self.get_date()
        self.get_category()
        self.get_subcategory()
        self.get_description()
        self.get_ingredients()
        self.get_method()
        print(self.recipe_data)

    def create_pop_up(self, title, text):
        # pop_up = customtkinter.CTkInputDialog(text=text, title=title)
        pass
        
        

    def close_app(self, event=None):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


add_recipe = AddRecipe()
add_recipe.run()

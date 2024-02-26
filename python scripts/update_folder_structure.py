import json
import os


class UpdateFolderStructure:
    def __init__(self) -> None:
        self.get_json_data()
        self.added_folders = []

    def get_json_data(self):
        with open("./json_data/categories.json", "r") as file:

            self.categories_dict = json.load(file)

    def create_category_folders(self):
        for i in self.categories_dict:

            if not os.path.exists(i):
                os.mkdir(i)
                self.added_folders.append(i)

    def create_sub_category_folders(self):
        for i in self.categories_dict.items():
            subcategories = i[1]
            for j in subcategories:
                if not os.path.exists(f"{i[0]}/{j}"):
                    os.mkdir(f"{i[0]}/{j}")
                    self.added_folders.append(f"{i[0]}/{j}")

    def end_run_message(self):
        print("\n" + 40 * "=" + "\n")
        if len(self.added_folders) > 0:
            for i in self.added_folders:
                print(f"Added {i}.")
            print("Folder structure up to date.")
        else:
            print("No new folders added.")
            print("Folder structure up to date.")
        print("\n" + 40 * "=" + "\n")

    def run(self):
        self.create_category_folders()
        self.create_sub_category_folders()
        self.end_run_message()


update_folder_structure = UpdateFolderStructure()
update_folder_structure.run()

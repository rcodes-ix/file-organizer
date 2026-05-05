import os
import shutil


folder = input("Enter folder path: ")


files = os.listdir(folder)

for file in files:
    full_path = os.path.join(folder, file)

    if os.path.isfile(full_path):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            category = "Images"
        elif file.lower().endswith(".exe"):
            category = "Softwares"
        elif file.lower().endswith(".pdf"):
            category = "PDFs"
        else:
            category = "Others"
        
        category_path = os.path.join(folder, category)
        os.makedirs(category_path, exist_ok=True)
        
        destination = os.path.join(category_path, file)

        counter = 2
        name, ext = os.path.splitext(file)

        while os.path.exists(destination):
            new_name = f"{name}{counter}{ext}"
            destination = os.path.join(category_path, new_name)
            counter += 1

        
        shutil.move(full_path, destination)

        print(f"Moved {file} → {category}")



        
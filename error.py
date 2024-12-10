import json

with open('./config/themes.json', 'r') as file:
    try:
        data = json.load(file)
        print("JSON valid!")
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")
      

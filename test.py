import json
file_path = '/home/neel/Desktop/HyperLink/Automatic Job Selection/combined_jobs1.json'

with open(file_path, 'r') as file:
    data = json.load(file)

print(len(data)) 
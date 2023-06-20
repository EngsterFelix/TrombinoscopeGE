import csv
import json

csv_file = 'saisonniers.csv'  # Chemin vers votre fichier CSV
json_file = 'employe.json'  # Chemin pour enregistrer le fichier JSON

data = []

# Mappage des colonnes du fichier Excel aux clés du dictionnaire JSON
field_mapping = {
    'nom': 'nom',
    'prenom': 'prenom',
    'village': 'village',
    'telephone': 'telephone'
}

# Ouvrir le fichier CSV et lire les données en utilisant le délimiteur ;
with open(csv_file, 'r') as file:
    csv_data = csv.DictReader(file, delimiter=';')
    for row in csv_data:
        # Créer un nouveau dictionnaire en utilisant le mappage des colonnes
        new_row = {}
        for json_key, excel_key in field_mapping.items():
            new_row[json_key] = row[excel_key]

        data.append(new_row)

# Écrire les données dans un fichier JSON
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)
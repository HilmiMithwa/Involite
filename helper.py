import re
from datetime import datetime
import json

def load_data():
    """Load JSON data from a file."""
    try:
        with open("database.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return None
    

def save_data(data):
    """Save JSON data to a file."""
    with open("database.json", "w") as file:
        json.dump(data, file, indent=4)


def validate_input(prompt, pattern, cast_type=str, default=None, validate_date=False):
    """Validate user input against a regex pattern and additional checks like date validation."""
    while True:
        user_input = input(prompt)
        if not user_input and default is not None:
            return default
        
        # Validasi format menggunakan regex
        if re.match(pattern, user_input):
            # Jika validate_date True, lakukan validasi tanggal lebih dari hari ini
            if validate_date:
                try:
                    input_date = datetime.strptime(user_input, "%Y-%m-%d").date()
                    today = datetime.today().date()
                    if input_date > today:
                        print("Tanggal tidak boleh lebih dari tanggal hari ini!")
                        continue  # Minta input ulang
                except ValueError:
                    print("Tanggal tidak valid! Periksa kembali format atau tanggal yang dimasukkan.")
                    continue  # Minta input ulang

            return cast_type(user_input)
        
        print("Input tidak valid. Silakan coba lagi.")
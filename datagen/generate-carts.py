import json
import random
import csv 
import uuid


products_file_path = "products.csv"
users_file_path = "user_uuids.csv"
products_list = []
user_ids = []
selected_product_options = []
cart_data = []

def save_to_csv(data, filename):
    keys = ['cart_id', 'user_id', 'product_id', 'selected_options', 'quantity', 'created_at', 'updated_at']
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def process_options(options_str):
    options = json.loads(options_str.replace('\'', '\"')) 
    selected_options = {key: random.choice(value) for key, value in options.items()}
    return selected_options

def generate_order_data():

    with open(products_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products_list.append(row)

    with open(users_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            user_ids.append(row[0])

    for entry in products_list:
        product_id = entry['product_id']
        options_str = entry['options']
        selected_options = process_options(options_str)

        cart_data.append({
            "cart_id": uuid.uuid4(),
            "user_id": random.choice(user_ids),
            "product_id": product_id,
            "selected_options": selected_options,
            "quantity": random.randint(1, 5),
            "created_at": "tmp",
            "updated_at": "tmp"
        })
        # print(cart_data)

    return cart_data
 

result = generate_order_data()
save_to_csv(result, 'cart.csv')
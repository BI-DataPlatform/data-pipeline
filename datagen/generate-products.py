import json
import random
import datetime
import csv
import uuid
from itertools import combinations

with open('datagen/categories.json', 'r', encoding='utf-8') as file:
    categories = json.load(file)

with open('datagen/options.json', 'r', encoding='utf-8') as file:
    options = json.load(file)

i = 0

def generate_uuids(count):
    uuids = [str(uuid.uuid4()) for _ in range(count)]
    return uuids


def read_uuids_from_csv(file_path):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        uuids = [row[0] for row in reader]
    return uuids

# 중복을 피하기 위한 Serial Number 
serial_numbers = {}
def generate_product_data():
    product_data = []
    prefixes = ["킹", "왕", "짱", "굳", "굿", "존맛", "꿀맛", "지존"]
    uuids = read_uuids_from_csv("store_uuids.csv")
    
    global i
    # 대분류 (food, beverage, dessert)
    for main_category, sub_categories in categories.items():
        # 중분류 (korean, chinese, ...)

        for sub_category, items in sub_categories.items():
            # 옵션 카테고리 동적 선택
            category_options_key = f"{main_category}_options"  # 예: food_options, beverage_options
            sub_category_options = options.get(category_options_key, {}).get(f"{sub_category}_options", {})
            # 모든 항목에 대한 데이터 생성
            for item in items:
                for prefix in prefixes:
                    product_name = f"{prefix} {item}"
                    for year in range(1950, 2031):

                        for option_count in range(3, 9):  # 3~8개의 옵션 조합
                            for option_combination in combinations(sub_category_options.items(), option_count):
                                option_data = {opt[0]: opt[1] for opt in option_combination}
                                # if i == 100:
                                #    return product_data
                                product_id = generate_product_id(main_category, sub_category, product_name, year)

                                start_date = datetime.datetime(1950, 1, 1)
                                end_date = datetime.datetime(2050, 1, 1)

                                date1 = random_date(start_date, end_date)
                                date2 = random_date(start_date, end_date)

                                product_data.append({
                                    "product_id": product_id,
                                    "store_id": random.choice(uuids),
                                    "name": product_name,
                                    "options": option_data,
                                    "created_at": min(date1, date2),
                                    "updated_at": max(date1, date2)
                                })
    return product_data

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def generate_product_id(main_category, sub_category, product_name, year):
    global i
    i = i + 1

    key = f"{main_category}-{sub_category}-{product_name}-{year}"
    serial = serial_numbers.get(key, 00000000) + 1
    serial_numbers[key] = serial
    return f"{main_category[:3]}-{sub_category[:3]}-{str(serial).zfill(8)}-{year}"


def save_to_csv(data, filename):
    keys = ['product_id', 'store_id', 'name', 'options', 'created_at', 'updated_at']
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

product_data = generate_product_data()
save_to_csv(product_data, 'products.csv')



# print(f"CSV 파일이 'products1.csv'로 저장되었습니다.")

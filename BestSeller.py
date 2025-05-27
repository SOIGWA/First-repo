import csv

csv_file_path = 'best_sellers.csv'

best_selling_book = None
max_sales = 0

try:
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  

        for row in csv_reader:
            current_sales = float(row[4])
            if current_sales > max_sales:
                max_sales = current_sales
                best_selling_book = row

    output_file_path = 'bestseller_info.csv'
    with open(output_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])

        if best_selling_book:
            csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])

        print('Best selling info written to', output_file_path)

except FileNotFoundError as e:
    print(f"Error reading the file: {e}")

import csv

def generate_frequency_file(input_file, output_file):
    # Dictionary to store name frequencies
    name_frequencies = {}

    # Read input file and populate name frequencies
    with open(input_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  

        with open(output_file, 'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['Name', 'Gender'])  
            for row in reader:
                try:
                    name, gender, frequency, include = row[0].split(',')
                    frequency = int(frequency.strip())
                    for _ in range(frequency):
                        writer.writerow([name, gender])
                except (ValueError, IndexError):
                    print(f"Skipping row {row}, invalid format or missing data.")



input_file = "input.csv"  
output_file = "output.csv" 
generate_frequency_file(input_file, output_file)

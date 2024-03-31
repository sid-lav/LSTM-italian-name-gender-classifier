import csv

def count_final_characters(file_path):
    final_char_freq = {'f': {}, 'm': {}}

    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for name, gender in reader:
            if name:
                final_char = name.strip()[-1]
                gender_lower = gender.lower()
                final_char_freq[gender_lower][final_char] = final_char_freq[gender_lower].get(final_char, 0) + 1

    return final_char_freq


def save_results_to_file(file_path, results):
    with open(file_path, 'w') as file:
        for distribution, gender_freq_dict in results.items():
            file.write(f"Distribution: {distribution.capitalize()}\n")
            for gender, frequency_dict in gender_freq_dict.items():
                total_freq = sum(frequency_dict.values())
                file.write(f"Gender: {gender.capitalize()}, Total: {total_freq}\n")
                sorted_freq = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)[:3]  # Limit to top 3
                for char, freq in sorted_freq:
                    percentage = (freq / total_freq) * 100 if total_freq > 0 else 0
                    file.write(f"{char}: {freq} ({percentage:.2f}%)\n")
                file.write("\n")


paths = ["1999.csv", "2014.csv", "1999_output.csv", "2014_output.csv", "usa_names.csv"]  
results = {}

for file_path in paths:
    gender_freq = count_final_characters(file_path)
    distribution = file_path.split('/')[-1].split('.')[0]  
    results[distribution] = gender_freq

output_file = "final_character_frequencies.txt"
save_results_to_file(output_file, results)
print(f"Results saved to {output_file}")

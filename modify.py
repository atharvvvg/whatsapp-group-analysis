#importing req libraries
import csv

def fix_multilines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    corrected_lines = []
    current_line = ""

    #Data Wrangling
    #Adjusting extracted data according to my need:
    #here I wanted the each message to be in a newline so that Tableau could easily understand it
    for line in lines:
        line = line.strip()
        if line.startswith("["):
            if current_line:
                corrected_lines.append(current_line)
            current_line = line
        else:
            current_line += " " + line

    if current_line:
        corrected_lines.append(current_line)

    #Output data to new file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for line in corrected_lines:
            timestamp_index = line.index(']')
            writer.writerow([line[:timestamp_index+1], line[timestamp_index+1:].strip()])

input_file = "[file loc]/_chat.txt"
output_file = "_chat_fixed.csv"
fix_multilines(input_file, output_file)

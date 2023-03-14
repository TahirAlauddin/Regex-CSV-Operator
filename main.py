import re
import csv

# Define the regex pattern to match
regex_file = open('regex.txt')
regex = regex_file.read()
pattern = re.compile(regex, re.IGNORECASE)


def read_csv_regex_matched(source):
    # Open source.csv for reading
    with open(source, 'r') as source_file:
        reader = csv.reader(source_file)

        # Create an empty list to store the lines matching the regex
        matching_lines = []

        # Iterate through the lines in source.csv
        for row in reader:
            # Check if the line matches the regex
            if pattern.search(' '.join(row)):
                # If it does, add it to the list of matching lines
                matching_lines.append(row)
    return matching_lines


def read_csv_regex_didnt_matched(source):
    # Open source.csv for reading
    with open(source, 'r') as source_file:
        reader = csv.reader(source_file)

        # Create an empty list to store the lines matching the regex
        non_matching_lines = []

        # Iterate through the lines in source.csv
        for row in reader:
            # Check if the line matches the regex
            if not pattern.search(' '.join(row)):
                # If it does, add it to the list of matching lines
                non_matching_lines.append(row)
    return non_matching_lines


def write_csv(destination, lines, mode='w') -> None:
    
    # Open destination.csv for writing
    with open(destination, mode) as dest_file:
        writer = csv.writer(dest_file)

        # Strip newline characters from the input data
        lines = [row for row in lines if row and row[0].strip()]

        # Write the matching lines to destination.csv
        for row in lines:
            dest_file.write('"' + '","'.join(row) + '"' + '\n')


def main():
    matching_lines = read_csv_regex_matched('source.csv')
    write_csv('destination.csv', matching_lines, mode='a')
    non_matching_lines = read_csv_regex_didnt_matched('source.csv')
    write_csv('source.csv', non_matching_lines, mode='w')


if __name__ == '__main__':
    main()
    
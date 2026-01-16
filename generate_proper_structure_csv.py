import csv

# Import properly structured messages
from playbook_messages_proper_structure import messages

# Read the original CSV
input_file = 'octopus_export-message_clayworks_1_12_2026.csv'
output_file = 'octopus_export-message_clayworks_1_12_2026_proper_structure.csv'

with open(input_file, 'r', encoding='utf-8-sig') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)

    # Add 'Personalized Message' to fieldnames
    fieldnames = reader.fieldnames + ['Personalized Message']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    matched_count = 0
    unmatched_count = 0

    for row in reader:
        linkedin_url = row['Link']

        # Get the personalized message for this LinkedIn URL
        if linkedin_url in messages:
            row['Personalized Message'] = messages[linkedin_url]
            matched_count += 1
        else:
            row['Personalized Message'] = ''
            unmatched_count += 1
            print(f"Warning: No message found for {linkedin_url}")

        writer.writerow(row)

print(f"\n=== Properly Structured CSV Generated ===")
print(f"Total contacts: {matched_count + unmatched_count}")
print(f"Matched with messages: {matched_count}")
print(f"Unmatched: {unmatched_count}")
print(f"Format: Opener → Problem + Solution → Low-friction CTA")
print(f"Output file: {output_file}")

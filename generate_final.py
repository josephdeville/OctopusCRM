import csv

# Import final messages with copywriting skill applied
from playbook_messages_final import messages

# Read the original CSV
input_file = 'octopus_export-message_clayworks_1_12_2026.csv'
output_file = 'octopus_export-message_clayworks_1_12_2026_final.csv'

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

print(f"\n=== Final CSV with Copywriting Skill Applied ===")
print(f"Total contacts: {matched_count + unmatched_count}")
print(f"Matched with messages: {matched_count}")
print(f"Unmatched: {unmatched_count}")
print(f"\nFollowing Technical Writing & GTM Communication Skill guidelines:")
print(f"- No forbidden phrases (I hope this..., Just following up, etc.)")
print(f"- No em dashes")
print(f"- Professional but not stuffy")
print(f"- Direct but not blunt")
print(f"- Specific pain points")
print(f"- Social proof with similar companies")
print(f"\nFormat: Observation → Pain point → I [verb] for [industry] → CTA with social proof")
print(f"\nOutput file: {output_file}")

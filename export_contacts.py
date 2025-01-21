import requests

# Replace this with your actual Brevo API key
API_KEY = 'your_brevo_api_key'

# Brevo API endpoint for retrieving contacts
API_URL = 'https://api.brevo.com/v3/contacts'

# Set up the headers for the API request
headers = {
    'api-key': API_KEY,
    'content-type': 'application/json',
    'accept': 'application/json'
}

# Function to get all contacts
def get_all_contacts():
    contacts = []
    offset = 0
    limit = 500  # Brevo API limit per request

    while True:
        params = {
            'limit': limit,
            'offset': offset
        }
        response = requests.get(API_URL, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            contacts.extend(data['contacts'])
            if len(data['contacts']) < limit:
                break
            offset += limit
        else:
            print(f"Failed to retrieve contacts: {response.status_code}")
            break

    return contacts

# Function to extract email addresses from contacts
def extract_email_addresses(contacts):
    email_addresses = [contact['email'] for contact in contacts]
    return email_addresses

# Main function to export email addresses
def export_email_addresses():
    contacts = get_all_contacts()
    email_addresses = extract_email_addresses(contacts)

    # Save email addresses to a file
    with open('contacts_email_addresses.txt', 'w') as file:
        for email in email_addresses:
            file.write(f"{email}\n")

    print("Email addresses have been exported to contacts_email_addresses.txt")

# Run the export function
if __name__ == "__main__":
    export_email_addresses()
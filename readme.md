
```markdown
# Brevo Contacts Email Exporter

This Python script allows you to export all your contacts' email addresses from Brevo using the Brevo API. The script retrieves all contacts, extracts their email addresses, and saves them to a text file.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Requests Library**: Install the `requests` library if you haven't already. You can install it using pip:
   ```bash
   pip install requests
   ```

## Setup

1. **Get Your Brevo API Key**:
   - Log in to your Brevo account.
   - Go to the API settings or API keys section.
   - Generate a new API key if you don't have one already. Copy the API key.

2. **Replace Placeholder in Script**:
   - Open the `export_contacts.py` script.
   - Replace `'your_brevo_api_key'` with your actual Brevo API key.

## Running the Script

1. **Save the Script**:
   - Save the following Python script as `export_contacts.py`:

   ```python
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
   ```

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where `export_contacts.py` is saved.
   - Run the script using Python:
     ```bash
     python export_contacts.py
     ```

## Output

The script will create a file named `contacts_email_addresses.txt` in the same directory. This file will contain all the email addresses of your contacts, each on a new line.

## Notes

- Ensure that your Brevo API key has the necessary permissions to access contact data.
- Be cautious with your API key; do not share it publicly.
---

Happy exporting!
```

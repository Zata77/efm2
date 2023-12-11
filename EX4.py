def Add():
    # Open the 'contact.txt' file in append mode
    file = open("contact.txt", "a")

    # Prompt the user to input contact details
    nom = input("Enter first name: ")
    prenom = input("Enter last name: ")
    tel = input("Enter telephone number: ")
    contact_type = input("Enter contact type: ")

    # Write the contact details to the file
    file.write("\n")               # Move to a new line in the file
    file.write(nom)                # Write the first name
    file.write("; ")               # Separate fields with a semicolon and a space
    file.write(prenom)             # Write the last name
    file.write("; ")
    file.write(tel)                # Write the telephone number
    file.write("; ")
    file.write(contact_type)       # Write the contact type

    # Close the file to save changes
    file.close()

def supprimer():
    # Read contacts from the file
    contacts = []
    with open('contact.txt', 'r') as file:
        lines = file.readlines()
        contacts = [line.strip().split(';') for line in lines]

    # Filter out contacts of type 'personnel'
    contacts = [contact for contact in contacts if contact[3].strip().lower() != 'personnel']

    # Write the remaining contacts back to the file
    with open('contact.txt', 'w') as file:
        for contact in contacts:
            file.write('; '.join(contact) + '\n')

# Add a new contact
Add()
# Remove contacts of type 'personnel'
supprimer()
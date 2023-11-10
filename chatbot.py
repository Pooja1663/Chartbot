import re

def get_celebrity_info(celebrity_name, celebrity_data):
    match = None
    for entry in celebrity_data:
        if celebrity_name.lower() in entry['name'].lower():
            match = entry
            break

    if match:
        # Extract information using regular expressions
        date_of_birth = re.search(r'(?i)date\s*of\s*birth:\s*(\S+)', match['info'])
        occupation = re.search(r'(?i)occupation:\s*(\S+)', match['info'])
        age = re.search(r'(?i)age:\s*(\S+)', match['info'])
        nationality = re.search(r'(?i)nationality:\s*(\S+)', match['info'])

        # Print the extracted information
        print(f'Date of Birth: {date_of_birth.group(1) if date_of_birth else "N/A"}')
        print(f'Occupation: {occupation.group(1) if occupation else "N/A"}')
        print(f'Age: {age.group(1) if age else "N/A"}')
        print(f'Nationality: {nationality.group(1) if nationality else "N/A"}')
    else:
        print(f'Celebrity not found in the dataset.')

# Example usage:
celebrity_data = [
    {'name': 'Olivia rodrigo', 'info': 'Date of Birth: february 20, 2003\nOccupation: American singer\nAge: 20\nNationality: American'},
    {'name': 'Rakshith shetty', 'info': 'Date of Birth: june 6, 1983\nOccupation: Actor\nAge: 40\nNationality: Indian'},
    # Add more celebrity data as needed
]

def main():
     print("Hello! this is your celebrity information chatbot.\n")
     while True:
         user_input = input("get some information about the celebrityR, or type 'exit' to quit: ")
         if user_input.lower() == 'exit':
             print("Bye!Talk to later")
             break
             
         else:
             celebrity_name = user_input
             print("Here is your information:")
             info =  get_celebrity_info(celebrity_name, celebrity_data)
             
if __name__ == "__main__":
    main()
from flask import Flask, request, jsonify
import random
app = Flask(__name__)

class StringGenerator:

    def __init__(self):
        pass

    def valid(self, num_letters):
        # Generated a string with "a" followed by "b"
        sub_string_a = "a" * num_letters
        sub_string_b = "b" * num_letters
        generated_string = sub_string_a + sub_string_b
        return generated_string
    def invalid(self, num_letters):
        generated_string = "".join(random.choice(["a", "b"]) for _ in range(num_letters))
        return generated_string

    def generateStrings(self):
        string_set = set()   # Using a set to avoid duplicate data
        # Generated unique strings 
        while len(string_set) < random.randint(5 , 11):
            option = random.choice([0, 1])
            num_letters = random.randint(0, 10)  # 0 to 10, because we take into account the case where the string is empty
            
            if option == 1:
                generated_string = self.valid(num_letters)
            else:
                # Case where we generate a string with random numbers of letters "a" and/or "b" 
                generated_string = self.invalid(num_letters)
            
            # Add only if is in a set
            if generated_string not in string_set:
                string_set.add(generated_string)  

        # Create a .txt file 
        txt_content = "============================\n"
        txt_content += "       GENERATED STRINGS     \n"
        txt_content += "============================\n\n"

        # Add a index to each string
        for i, string in enumerate(string_set, start=1):
            txt_content += f"{i}. {string}\n"

        # Save content of each string in a .txt file
        with open("generated_strings.txt", "w", encoding="utf-8") as file:
            file.write(txt_content)

        print("The generated strings have been saved in 'generated_strings.txt'.")

        return string_set





```

 ██████╗███████╗ ██████╗        ██████╗ ██████╗  █████╗ 
██╔════╝██╔════╝██╔════╝   --   ██╔══██╗██╔══██╗██╔══██╗
██║     █████╗  ██║  ███╗  --   ██████╔╝██║  ██║███████║
██║     ██╔══╝  ██║   ██║  --   ██╔═══╝ ██║  ██║██╔══██║
╚██████╗██║     ╚██████╔╝       ██║     ██████╔╝██║  ██║
 ╚═════╝╚═╝      ╚═════╝        ╚═╝     ╚═════╝ ╚═╝  ╚═╝ 
                                                                  

```

## 📖 Description
- This project is an implementation of a context free grammar into a push down automata.

## 📚 Class Information
- **Class Number:** 7308  

## 👨‍🏫 Teacher
- **Adolfo Andrés Castro Sánchez** 

## 👨‍🎓 Students
- **Alejandro Tiado Ramírez** 
- **Simón Sloan García Villa**  

## 💻 System Information
 - The script was made using Python 3.13.2

 - The operating systems we used for the testing and programming were Windows 11 and Kali Linux (Version 2024.4).

## 🛠️ Tools used for the project:
- Visual Studio as the code editor.
- Git for version control.
- GitHub was used to upload the code to the cloud.

## ❓ How to run the project
**Just clone the repository and run the main.py file**

## 🧠 Approach to the problem
In the process of building the PDA, it was necessary to remember the equivalences to pass from a CFG to a PDA. 
In this ideas line, initially, we had a CFG defined as follows: 


    S-> aSb | ε , in the form G = {N,Σ,P,S}

and we convert that to this PDA: 
 N = (Q, Σ, 𝜞, 𝜹, 𝒔, 𝑭 )
where 

    Q = {q0,q1}
    Σ = {a,b}
    𝜞 = {S,A}
    𝜹 = transitions in the corresponding format 
    s = q0 
    F = {qo,q1}
    
With this context, we create these production rules:
        
    (i)   (q0, ε, S), (q0, ε) 
    (ii)  (q0, a, S), (q0, A) 
    (iii) (q0, a, A), (q0, AA) 
    (iv)  (q0, b, A), (q1, ε) 
    (v)   (q1, b, A), (q1, ε)

We did it in this way to ensure the possible cases where the string to analyze has an equal number of a's in a row as b's, and 
don't have incongruences in the form : 
 abab or aabbb 
that would be accepted if we reduce these productions rules.

## 📝 Code Explanation

### First algorithm

```python
import random

class StringGenerator:

    def __init__(self):
        pass

    def valid(self, num_letters):
        # Generated a string with "a" followed by "b"
        sub_string_a = "a" * num_letters
        sub_string_b = "b" * num_letters
        generated_string = sub_string_a + sub_string_b
        return generated_string                                     

```

In case the variable option (which is random) equals 1, this function will be called and will create valid strings from 1 to 10 the same numbers of a’s in a row as b’s. That’s why we create two substrings composed of as many letters of the variable num_letters defined which is a random variable with a range from 1 to 10. At the end, we concatenate both substrings and return it.  

```python

 def invalid(self, num_letters):
    generated_string = "".join(random.choice(["a", "b"]) for _ in range(num_letters))
    return generated_string                          

```

In case option (random variable) is equal to 0, this function will be called and will create invalid strings in range according to the content of variable num_letters which is also a random variable. Then it will return the string generated. 


```python

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

```

This function is the main one from algorithm1 due to it creates a set of valid and invalid strings. So for example, at first it creates an empty set which we´ll fill out later. Then we start to fill it out with a random number in the range of 5 to 11, which might be the length of the set of strings. Then we initialized by each iteration a random variable call option in the range 0 to 1, which will allow us to decide whether to call a valid or invalid function explained before. Then we initialized the variable num_letters which is going to be the length of each string. After that, we call the corresponding option by the variable option and then we add this string to the set of generated strings if it was not in the set already. 

```python
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

```

This is an added value part of the code that exports a .txt file with the generated strings in readable beauty format that can be the input of future versions of the code. To explain it, basically, at first, we´re creating a .txt file with the title “Generated strings”. Then we add each string iterating the set of strings. After that, we save the content of the file and print a message of confirmation. 

### Second algorithm

```python
        
class PDA:
    def __init__(self):
        self.starting_pile_symbol = "S" # Give the PDA starting parameters
        self.starting_state = "q0"                                                          

```

We define the class PDA, where we are going to code all the structures of our PDA. We start by initializing the class with the starting pile symbol "S" and the starting state "q0". 

```python
    def transitions(self , stack , current_state , char): # Here we define all rules of the automata, taking in to account the production rules of the grammar
        
        if(len(stack) != 0):
            
            if (current_state == "q0" and char == "" and stack[-1] == "S"):
                stack.pop()
                return 1 , current_state
            elif (current_state == "q0" and char == "a" and stack[-1] == "S"):
                stack.pop()
                stack.append("A")
                return 2 , current_state
            elif (current_state == "q0" and char == "a" and stack[-1] == "A"):
                stack.append("A")
                return 3 , current_state
            elif (current_state == "q0" and char == "b" and stack[-1] == "A"):
                stack.pop()
                current_state = "q1"
                return 4 , current_state
            elif (current_state == "q1" and char == "b" and stack[-1] == "A"):
                stack.pop()
                return 5 , current_state
            else:
                return -1 , current_state
        else:
            return -1 , current_state
        
        # In case we dont find any rule that match the current state and char, we return -1, meaning that the string is not valid
 

```

Here, we define all the transition rules of our PDA, transition rules already defined in the approach to the problem.

```python
    def is_valid(self, string):
        stack = []
        stack.append(self.starting_pile_symbol) # Start the stack with the starting pile symbol

        if len(string) == 0: # If the string is empty, we return true, because the grammar accepts epsilon
            return True , [1]

        transitions_done = []

        current_state = self.starting_state
        
        for char in string:

            transition , current_state = self.transitions(stack, current_state, char)
            if transition == -1: 
                transitions_done.append(transition) 
                return False , transitions_done # Break when we find a transition that is not valid
            
            transitions_done.append(transition)  # Append every number of the transitions done 
            

        if (len(stack) != 0):
            return False , transitions_done   # If the stack is not empty, we return false, because the string is not valid
        
        return True , transitions_done  # Else, we return true, because the string is valid

```
We define a method that is going to check if a string can be read by the PDA. It is going to store the set of transitions made for getting to an acceptance state. This would be crucial for the trird algorithm.

```python
 def return_valid_strings(self , set_of_strings): # Method for returning only the valid strings with their transitions
        
        accepted_transitions = []
        accepted_strings = []

        for string in set_of_strings:
            

            accepted , transitions_done = self.is_valid(string)

            if accepted:
                accepted_transitions.append(transitions_done)
                accepted_strings.append(string)
            
        return accepted_strings , accepted_transitions

```

Here we have a method for returning only the accepted strings and their transitions. 

### Third algorithm

```python
        
from tabulate import tabulate

class Rules_table:
    def aplied_rules(self , string ,  transitions_done):
                
        set_of_applied_rules = [["", f"q0 , {string} , S"]] # Start with the initial state, the string given and the starting pile symbol
        
        pile = "" # Start with an empty pile (Its just for showing the transitions done on the pile)

        for number in transitions_done:
            string = string[1:] # Remove the first letter of the string for every iteration

            if len(string) == 0:
                string = "ε" # If the string is empty, we replace it with epsilon

            # Append every rule used depending on the number of the transition done

            if(number == 1): 
                set_of_applied_rules.append(["(i)" ,  "q0, ε, ε"]) 
            elif(number == 2):
                pile = pile + "A"
                set_of_applied_rules.append(["(ii)" , f"q0 , {string} , {pile}"])
                
            elif(number == 3):
                pile = pile + "A"
                set_of_applied_rules.append(["(iii)" , f"q0 , {string} , {pile}"])
                
            elif(number == 4):
                pile = pile[1:]
                if pile == "":
                    pile = "ε"
                set_of_applied_rules.append(["(iv)" , f"q1 , {string} , {pile}"])
                
            elif(number == 5):
                pile = pile[1:]
                if pile == "":
                    pile = "ε"
                set_of_applied_rules.append(["(v)" , f"q1 , {string} , {pile}"])

        table = tabulate(set_of_applied_rules, headers=["Rules", "Computation of M on input x"], tablefmt="grid")
        print(table) 

        print("\n")

                                                  
```

We are going to import tabulate to print the results prettier. We are iterating through every transition made to the string, so we only need to associate the transition's number with its corresponding rule. When we iterate through all the transitions, we print the resulting table with all the rules applied, the resulting string by every step taken, and the symbols of the pile. 


### Main

```python
from ALGORITHM_1_LFCO_2025_AT_SS import StringGenerator
from ALGORITHM_2_LFCO_2025_AT_SS import PDA
from ALGORITHM_3_LFCO_2025_AT_SS import Rules_table
import random   

# Create instances of the classes
stringGenerator = StringGenerator()
pda = PDA()
rules_table = Rules_table()                                                

```
Here we just create instances of the classes and import the algorithms made earlier.

```python
# Run the first algorithm

set_of_strings = stringGenerator.generateStrings()

emojis=["🔥", "🌟","💎", "📊", "👨‍💻", "💡", "⌨️", "🖱️", "🥑"]
print("🎲 Generating random strings... 🎲\n")

for idx, s in enumerate(set_of_strings, 1):
    emoji = random.choice(emojis)
    print(f"✨ String {idx}: {emoji}  \"{s}\"")

```

We print each string created with some emojis for a nicer style.

```python
# Run the second algorithm

print("\n🧠 Checking if the strings are valid... 🧠\n")

results = []

for string in set_of_strings:
    accepted, _ = pda.is_valid(string)

    checkmark = "✅" if accepted else "❌"
    results.append((string, checkmark))

for idx, (s, result) in enumerate(results, 1):
    print(f"{idx}. {s} {result}")

valid_strings , valid_transitions = pda.return_valid_strings(set_of_strings) # Get only the valid strings and their transitions

```

We print if the string is accepted or not, adding an emoji to make it clearer. Then, we execute the .return_valid_strings to get only the accepted strings and their transitions. This is going to be useful for following the structure given.

```python

# Run the third algorithm

print("\n📊 Applying rules... 📊\n")


for i in range(len(valid_strings)):
    
    string = valid_strings[i]
    transitions_done = valid_transitions[i]

    rules_table.aplied_rules(string , transitions_done)

```

We execute the third algorithm for every string accepted, iterating for the strings and transitions accepted by the PDA.






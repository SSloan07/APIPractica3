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
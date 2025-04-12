class PDA:
    def __init__(self):
        self.starting_pile_symbol = "S" # Give the PDA starting parameters
        self.starting_state = "q0"

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

    def return_valid_strings(self , set_of_strings): # Method for returning only the valid strings with their transitions
        
        accepted_transitions = []
        accepted_strings = []

        for string in set_of_strings:
            

            accepted , transitions_done = self.is_valid(string)

            if accepted:
                accepted_transitions.append(transitions_done)
                accepted_strings.append(string)
            
        return accepted_strings , accepted_transitions
            
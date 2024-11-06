class FiniteStateAutomaton:
    def __init__(self):
        # Define the states and initial state
        self.state = 'START'

    def transition(self, char):
        # Transition rules based on the current state and input character
        if self.state == 'START':
            if char == 'a':
                self.state = 'A'
            else:
                self.state = 'START'
        elif self.state == 'A':
            if char == 'b':
                self.state = 'ACCEPT'
            elif char == 'a':
                self.state = 'A'
            else:
                self.state = 'START'
        elif self.state == 'ACCEPT':
            if char == 'a':
                self.state = 'A'
            else:
                self.state = 'START'

    def is_accepted(self):
        # Check if the current state is the accept state
        return self.state == 'ACCEPT'

    def run(self, input_string):
        # Process each character in the input string
        for char in input_string:
            self.transition(char)
        # Return whether the string is accepted or not
        return self.is_accepted()


# Example usage
fsa = FiniteStateAutomaton()

# Test strings
test_strings = ["abab", "aab", "abc", "cab", "xxab"]

for string in test_strings:
    if fsa.run(string):
        print(f"The string '{string}' is accepted by the automaton.")
    else:
        print(f"The string '{string}' is not accepted by the automaton.")

# Lets define the error codes in a class. 
# This will allow us to sperate them from the main code.
# Defining a class means we wont need to import the whole file 

class Error():
    def __init__(self):
        self.error_codes = {
            -1: 'Cows exceeds stalls.',
            -2: 'Duplicate stall coordinates have been input.',
            -3: 'Unable to calculate distance with a single stall', 
            -4: 'Negative stall coordinates are not permitted.'

        }   

    def get_error(self, val):
        return self.error_codes[val]
    
    def add_error(self, key, msg):
        self.error_codes[key] = msg
        

       
# Written by Ralph Louis Gopez
# You know our stupid high-school subjects such as Physics and Chemistry wants to do stupid
# Given, Unknown, Formula, Solution, Answer Format which is totally unnecessary so 
# here I am making my life easier. This script provides an abstraction for the GUFS part,
#
# I make everything as practical and efficient as possible, there are three things you can do 
# with this: add a variable with a value, set the formula, print the result
#
# Take for example the formula c = sqrt{a + b} and I have a = 9 and b = 16
#  
# [SETTING A VARIABLE]
# Setting a variable with a value means I simply provide its codename, 
# actual name to be written as a variable, and its value to be written:
# create_symbol('a_var', 'a', '9')
# create_symbol('b_var', 'b', '16')
# 
# [USING A FORMULA]
# Using a formula, I have to provide the exact name of the unknown that will be written and the formula
# to be applied:
# use_formula('c', 'sqrt{ a_var + b_var }')
# 
# [PRINTING THE RESULT]
# An instance automatically saves its result when use_formula is called, hence:
# print_result() would do the trick


# Related to 
# https://documentation.libreoffice.org/assets/Uploads/Documentation/en/MG7.0/MG70-MathGuide.pdf

class MathText:
    prefix = '""'
    affix = 'newline'

    def __init__(self):
        """Initialize a new MathText parser"""
        self.symbols = []
        self.result = None
        pass

    def create_symbol(self, name, key, value):
        """Add a variable with a value for the formula"""

        # name is easy name, key refers to its typed key as variable, value refers to its typed value
        # example: create_symbol('a_var', 'a', '9')
        self.symbols.append({ 'name': name, 'key': key, 'value': value })
        return self
    
    def _fix(self, string):
        return f'{MathText.prefix} {string} {MathText.affix}'

    def use_formula(self, unknown, formula):
        """Set the formula to be used and printed later on with the GUFS-format"""
        
        # Dictionary of strings obviously
        result = {
            'given': self._fix('Given:'),
            'unknown': self._fix('Unknown:') + '\n' + self._fix(f'{unknown}'),
            'formula': self._fix('Formula:'),
            'solution': self._fix('Solution:'),
        }
        
        # The two other variables will be mutated a lot
        # The first one, is just a copy to make things a bit clear
        proper = formula
        formula_result = proper
        solution_result = proper

        # This simply generates or replaces everything necessary
        # to generate their own respective parts of the answer
        for symbol in self.symbols:
            result['given'] += '\n' + self._fix(f"{symbol['key']} = {symbol['value']}")
            formula_result = formula_result.replace(symbol['name'], symbol['key'])
            solution_result = solution_result.replace(symbol['name'], symbol['value'])
        
        result['formula'] += '\n' + self._fix(f'{unknown} = {formula_result}')
        result['solution'] += '\n' + self._fix(f'{unknown} = {solution_result}')
        
        self.result = result
        return self

    def print_result(self):
        """ Print the result """
        if self.result:
            print('\n\n'.join(self.result.values()))
        else:
            print('Please specify the formula to use with method use_formula')
        return self

if __name__ == "__main__":
    # Both these have the same result
    # Sample Usage 1
    print('[USAGE 1]')
    gufs = MathText()
    gufs.create_symbol('a_var', 'a', '9')
    gufs.create_symbol('b_var', 'b', '16')
    gufs.use_formula('c', 'sqrt{ a_var + b_var }')
    gufs.print_result()

    # Sample Usage 2
    print('\n[USAGE 2]')
    gufs_chained = MathText()
    gufs_chained.create_symbol('a_var', 'a', '9').create_symbol('b_var', 'b', '16').use_formula('c', 'sqrt{ a_var + b_var }').print_result()
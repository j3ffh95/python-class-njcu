'''
P9.1 We want to add a button to the tally counter in Section 9.2 that 
allows an operator to undo an accidental button click. Provide a method
    def undo(self)
that simulates such a button. As an added precaution, make sure that the 
operator cannot click the undo button more often than the click button.

def undo(self):
    if self._value > 0:
        self._value = self._value - 1

'''

'''

P9.2 Simulate a tally counter that can be used to admit a limited number 
of people. First, the limit is set with a call to
    def setLimit(self, maximum)
If the click button is clicked more often than the limit, simulate an alarm 
by printing out a message “Limit exceeded”.

def setLimit(self, maximum):
    self._max = maximum

def click(self):
    if self._value > self._max:
        print("Limit exceeded")
        return
    self._value += 1
    

'''

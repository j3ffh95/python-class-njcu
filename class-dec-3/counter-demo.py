# This program demostrates the Counter class.

# Import the Counter class form the counter module.
from counter import Counter

tally = Counter()
tally.reset()
# tally.click()
# tally.click()
# # tally.undo()

# result = tally.getValue()
# print("Value:", result)

# tally.click()
# result = tally.getValue()
# print("Value:", result)

tally.setLimit(2)
tally.click()

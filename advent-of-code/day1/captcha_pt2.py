# http://adventofcode.com/2017/day/1
"""
--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
"""

def read_input():
  input = open("input2.txt","r").read()
  return input;

def main():
  input = read_input()
  input_length = len(input)
  halfway = int(input_length / 2);
  sum = 0
  nextNum = 0

  for index, num in enumerate(input):
    try:
      nextNum = input[index + halfway]
    except IndexError:
      # Find distance to the end of the input
      distance = input_length - index
      # Continue this many more items to hit the index + halfway element.
      cont = halfway - distance
      nextNum = input[cont]

    if (index != input_length - 1):
      if(num == nextNum):
        sum += int(num)
  
  print("Sum is: " + str(sum))
  return sum

if __name__ == '__main__':
  main()

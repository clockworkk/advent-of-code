# http://adventofcode.com/2017/day/1
"""
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
"""

def read_input():
  input = open("input.txt","r").read()
  return input;

def check_first_last(sum, input):
  """
  Because it is circular, if the last digit and the first digit are the same
  then it should be added to the sum.
  """
  if (input[0] == input[-1]):
    sum += int(input[0])
  
  return sum

def main():
  input = read_input()
  input_length = len(input)
  sum = 0

  sum = check_first_last(sum, input)

  for index, num in enumerate(input):
    # nextNumber is the next number unless its the last item in the input
    nextNum = input[index+1] if (index != input_length -1) else input[index]

    if (index != input_length - 1):
      if(num == nextNum):
        sum += int(num)
  
  print("Sum is: " + str(sum))
  return sum

if __name__ == '__main__':
  main()

import sys,glob,os
sys.path.append(glob.glob(os.getcwd())[0] + "/../../day5/python")
from intcode import Intcode


# Use different input method depending on python version
if sys.version_info.major == 3:
    def read_input(): return input()
else:
    def read_input(): return raw_input()

class Cryo:
  """ Class playing the game of navigating through the rooms """

  def __init__(self,file):
    """ Initialize the intcode """
    self.ic = Intcode(file = file, reset = False, verbose = False)

  def play(self):
    """ Use the input from the terminal to play the game """
    message, row = [], ""
    while True:
      cond, output = self.ic()

      # Run until we are promted an input
      if output is None:

        # Print current message
        for row in message:
          print(row)

        # Read user input
        self.ic.input = [ord(i) for i in str(read_input()) + '\n']

        if (chr(self.ic.input[0]) == 'q') or cond:
          return

        # Reset message
        message, row = [], ""

        # Wake the intcode computer
        self.ic.idle = False

      # Otherwise build the screen
      else:
        # New line
        if output == 10:
          message.append(row)
          row = ""
        # Add to the row
        else:
          row += chr(output)
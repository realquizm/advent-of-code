import math
import time
def fuel_counter(masses):
  """ Function that computes the fuel needed for the input masses.
  Expected input is required to either be a list/tuple or scalar"""
  if isinstance(masses,(tuple,list)):
    return sum(fuel_counter(mass) for mass in masses)
  return max(int(math.floor(masses/3)-2),0)

def fuel_needed_total(mass):
  """ Function that computes the fuel needed for the mass and its own fuel.
  Expected input is a scalar """
  required_fuel = fuel_counter(mass)
  if required_fuel > 0:
    return required_fuel + fuel_needed_total(required_fuel)
  return 0

def fuel_counter_extended(masses):
  """ Function that computes the fuel needed for the input masses and the extra 
  fuel needed for the new fuel itself. Expected input is required to either be 
  a list/tuple or scalar"""
  if isinstance(masses,(tuple,list)):
    return sum(fuel_counter_extended(mass) for mass in masses)
  return fuel_needed_total(masses)

def main():
  # Open data file and read through all lines
  file_location = "../data/input.txt"
  try:
    with open(file_location) as f:
      masses = f.readlines()

    # Remove whitespace characters at end of each line
    masses = [int(x.strip()) for x in masses]

    # Part one
    t0 = time.time()
    part_one = fuel_counter(masses)
    time_part_one = round((time.time()-t0)*1e3)
    print("Solution to part one: %s (time taken %s[ms])" % \
        (part_one, time_part_one))

    t0 = time.time()
    part_two = fuel_counter_extended(masses)
    time_part_two = round((time.time()-t0)*1e3)
    print("Solution to part two: %s (time taken %s[ms])" % \
        (part_two, time_part_two))
    
  except IOError:
    print("Cannot find file at: " + file_location)

if __name__ == "__main__":
  main()

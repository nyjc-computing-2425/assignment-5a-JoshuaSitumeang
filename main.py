def to_hms(seconds: int) -> list:
    """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    """
    # Type your code below
    pass

def to_gms(seconds):
  """A function that takes in an integer argument (seconds) containing the number of seconds"""
  
  seconds = input('Enter the number of seconds (integer): ')
  seconds = int(seconds)

  minutes, seconds = divmod(seconds, 60)
  hours, minutes = divmod(minutes, 60)

  print("The duration is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
"""Convert to and from Roman numerals

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2004/05/05 21:57:20 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

import re
#Define exceptions
class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass

convertMap = (('M',  1000),
              ('CM', 900),
              ('D',  500),
              ('CD', 400),
              ('C',  100),
              ('XC', 90),
              ('L',  50),
              ('XL', 40),
              ('X',  10),
              ('IX', 9),
              ('V',  5),
              ('IV', 4),
              ('I',  1))


def toRoman(n):
    """convert integer to Roman numeral"""
    # Make sure the input is right
    if not (0 < n < 4000):
        raise OutOfRangeError("Range have to be between (1 .. 3000)")
    if int(n) != n:
        raise NotIntegerError("Input not an integer")

    result = ""
    for literal, numeral in convertMap:
        while n >= numeral:
            result += literal
            n -= numeral
    return result

def fromRoman(s):
    """convert Roman numeral to integer"""
    # Make sure the input is right
    #Define pattern to detect valid Roman numerals
    romanNumeralPattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
    if not re.search(romanNumeralPattern,s):
        raise InvalidRomanNumeralError('Not a Roman number')

    index = 0
    result = 0
    for literal, numeral in convertMap:
        while s[index:index+len(literal)] == literal:
            index += len(literal)
            result += numeral
    return result

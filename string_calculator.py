# imports
import re


class StringCalculator:
    numbers_re = r'([0-9]{1,})'
    def add(self, string_numbers):
        total = 0
        matches = re.findall(self.numbers_re, string_numbers)
        for number in matches:
            total +=int(number)
        return total
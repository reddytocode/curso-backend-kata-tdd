# imports
from logging import exception
import re


class StringCalculator:
    numbers_re = r'(-?[0-9]{1,})'
    negative_numbers_re = r'-[0-9]{1,}'

    def add(self, string_numbers):
        total = 0
        matches = re.findall(self.numbers_re, string_numbers)

        if any(re.match(self.negative_numbers_re, matched_value)
                        for matched_value in matches):
            negatives = []
            values = ''
            for number in matches:
                if re.match(self.negative_numbers_re, number):
                    negatives.append(number)
                    values = ','.join(negatives)
                    raise_error = 'negatives not allowed: {}'.format(values)
            raise Exception(raise_error)
        else:
            for number in matches:
                total +=int(number)
            return total

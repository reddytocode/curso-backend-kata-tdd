## Reto Curso Django - Ada School

Reto tomado de [wix/tdd-katas](https://github.com/wix/tdd-katas#readme)


## Greeter

#### Before you start:
* **Try not to read ahead.**
* **Do one task at a time. The trick is to learn to work incrementally.**

This kata demonstrates the problems of static scoped functions and objects.

All tests should always pass, regardless of environment conditions.

1. Write a `Greeter` class with `greet` function that receives a `name` as input and outputs `Hello <name>`. The signature of `greet` should not change throughout the kata. You are allowed to construct `Greeter` object as you please.
2. `greet` trims the input
3. `greet` capitalizes the first letter of the name
4. `greet` returns `Good morning <name>` when the time is 06:00-12:00
5. `greet` returns `Good evening <name>` when the time is 18:00-22:00
6. `greet` returns `Good night <name>` when the time is 22:00-06:00
7. `greet` logs into console each time it is called

=================================================================================================
## String Calculator

#### Before you start:
* **Try not to read ahead.**
* **Do one task at a time. The trick is to learn to work incrementally.**
Make sure you only test for correct inputs. there is no need to test for invalid inputs for this kata
This kata is one of the simplest and best ways to practice step-by-step fluent tdd, and provides an easy way to get proficient in a language.

1. Write a method add under an object StringCalculator that, given a delimited string, returns the sum of the numbers in the string.

2. An empty string returns zero '' => 0
3. A single number returns the value '1' => 1 '2' => 2
4. Two numbers, comma delimited, returns the sum '1,2' => 3 '10,20' => 30
5. Two numbers, newline delimited, returns the sum '1\n2' => 3
6. Three numbers, delimited either way, returns the sum '1\n2,3\n4' => 10
7. Negative numbers throw an exception with the message '-1,2,-3' => 'negatives not allowed: -1,-3'
##### stop here if you are a beginner. Continue if you can finish the steps so far in less than 30 minutes.

8. Numbers greater than 1000 are ignored
9. A single char delimiter can be defined on the first line starting with // (e.g //#\n1#2 for a ‘#’ as the delimiter)
10. A multi char delimiter can be defined on the first line starting with // (e.g. //###\n1###2 for ‘###’ as the delimiter)
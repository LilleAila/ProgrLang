# Interpreter

Run `main.py shell` to get a shell, run `main.py <path-to-file>` to run a file

# Programming language interpreter

## Numbers
```
Negative: -5
Float   : 2.5
Integer : 5
```
```
+: Add     : 3 + 2 = 5
-: Subtract: 4 - 3 = 1
*: Multiply: 3 * 3 = 9
/: Divide  : 8 / 2 = 4
%: Modulo  : 9 % 2 = 1
^: Exponent: 2 ^ 3 = 8
```

## Strings
Strings are created with single or double quotes:
`"<string>"` or `'<string>'`
```
*: Multiply   : "Hello, " + "World!" = "Hello, World!"
+: Concatenate: "Test " * 3 = "Test Test Test"
```

## Lists
Lists are created with square brackets and values are separated with commas:
`["element1", "element2"]`
A list can store any value.
The first element in a list is [0]
```
+: Add item     : [1, 2] + 3 = [1, 2, 3]
-: Remove item  : [1, 2] - 0 = [2]
*: Combine lists: [1, 2] * [3, 4] = [1, 2, 3, 4]
/: Get item     : [1, 2] / 1 = 2
```

## Variables
Assign variables with the `var` keyword
```
var a = 4
var b = "string"
var c = [1, 2, 3, 4]
```

## Comparison
```
==: Returns 1 if items are equal
!=: Returns 1 if items are not equal
not: inverts value
```
```
> : Left is more than right
< : Right is more than left
>=: Left is more than or equal to right
<=: Right is more than of equal to left
```
```
and: both sides are true
or : at lest one side is true
```
## If statements
### Single line:
```
if <comparison> then <value> elif <comparison> then <value> else <value>
```
### Multiple lines:
```
if <comparison> then
    <code>
elif <comparison> then
    <code>
else
    <code>
end
```
Elif and else are optional

## Loops
Use `continue` to continue to next iteration

Use `break` to stop the loop
### For loop
```
for i = 0 to <end value> step <step value> then
    <code>
end
```
Step is optional
### While loop
```
var a = 0
while a < 10 then
    print(a)
    var a = a + 1
end
```

## Functions
### Single line:
```
func <name>(arg1, arg2) -> <value to return>
func add(a, b) -> a + b
```
### Multiple lines:
Use `return` keyword to return a value
```
func <name>(arg1, arg2)
    <code>
end
```
```
func add(a, b)
    return a + b
end
```

## Built-in functions
```
print(value): Print a value
print_ret(value): Print and return a valur
input(): Input a string in the console
input_int(): Input an integer in the console
```
```
is_number(value): Check if a value is a number
is_string(value): Check if a value is a string
is_list(value): Check if a value is a list
is_function(value): Check if a value is a function
```
```
append(list, value): Append value to end of list
pop(list, index): Remove and return element at index
set(list, index, value): Set item in list at index
extend(listA, listB): Combine two lists
len(list): Get length of list
```
```
clear, cls, clear(), cls(): Clear the screen
run(filename): Run a file
```

## Built-in variables
```
math_pi: pi
math_e: e
```
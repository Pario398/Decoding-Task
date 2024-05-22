# Secret Message Decoder

## Description
This project contains a Python function named `decode` that reads an encoded message from a .txt file and returns its decoded version as a string. The function decodes a hidden message based on the arrangement of numbers into a "pyramid" structure.

## How It Works
The function reads a text file where each line contains a number followed by a word. The numbers are placed into a pyramid in ascending order, with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the numbers increase consecutively. The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line. All other words are ignored.

For example, given the following input file:
``
1 I 
2 love 
3 computers 
4 and 
5 you 
6 too
``

The function will return the message "I love computers".

## Usage
To use the `decode` function, replace `'path_to_your_file.txt'` with the actual path to your text file when calling the function. For example:

```python
print(decode('path_to_your_file.txt'))
```
This will print the decoded message to the console.

Running the Script
To run the script in the terminal, navigate to the script’s directory and type python decode.py. This will execute the script and print the decoded message to the console.

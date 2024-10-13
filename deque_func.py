from collections import deque

def is_palindrome(input_string):
    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    char_deque = deque(normalized_string)
    
    while len(char_deque) > 1:
        left_char = char_deque.popleft()
        right_char = char_deque.pop()
        
        if left_char != right_char:
            return False

    return True

input_str = "A man, a plan, a canal, Panama"
if is_palindrome(input_str):
    print(f'"{input_str}" є паліндромом')
else:
    print(f'"{input_str}" не є паліндромом')

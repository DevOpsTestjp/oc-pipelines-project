def hello_world(name=None): 
    """Return a greeting message""" 
    if name: 
        return f"Hello, {name}!" 
    return "Hello, World!" 
 
def add_numbers(a, b): 
    """Add two numbers""" 
    return a + b 
 
def is_palindrome(text): 
    """Check if a string is a palindrome""" 
    cleaned = text.lower().replace(" ", "") 
    return cleaned == cleaned[::-1] 
 
if __name__ == "__main__": 
    print(hello_world()) 

from app.main import hello_world, add_numbers, is_palindrome 
 
def test_hello_world_default(): 
    result = hello_world() 
    assert result == "Hello, World!" 
 
def test_hello_world_with_name(): 
    result = hello_world("John") 
    assert result == "Hello, John!" 
 
def test_add_numbers_positive(): 
    result = add_numbers(5, 3) 
    assert result == 8 
 
def test_add_numbers_negative(): 
    result = add_numbers(-5, -3) 
    assert result == -8 
 
def test_is_palindrome_true(): 
    assert is_palindrome("racecar") is True 
    assert is_palindrome("A man a plan a canal Panama") is True 
 
def test_is_palindrome_false(): 
    assert is_palindrome("hello") is False 

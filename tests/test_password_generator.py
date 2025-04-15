from lib.password_generator import Password_generator
import string

'''
When I call #generate_password
I get a password returned
'''
def test_a_password_is_returned():
    password_generator = Password_generator()
    assert password_generator.generate_password()

'''
When I call #generate_password
a secure password is returned
'''
def test_returned_password_is_over_20_characters():
    password_generator = Password_generator()
    assert len(password_generator.generate_password()) > 20

def test_returned_password_has_3_instances_of_special_characters():
    password_generator = Password_generator()
    password = password_generator.generate_password()
    count = 0
    required_characters = string.punctuation
    for letter in password:
        if letter in required_characters:
            count+=1
    assert count > 2

def test_returned_password_has_at_least_1_capital_letter():
    password_generator = Password_generator()
    password = password_generator.generate_password()
    has_capital = False
    for letter in password:
        if letter.isupper():
            has_capital = True
    assert has_capital

def test_returned_password_has_at_least_1_lower_case_letter():
    password_generator = Password_generator()
    password = password_generator.generate_password()
    has_lower = False
    for letter in password:
        if letter.islower():
            has_lower = True
    assert has_lower

def test_returned_password_has_not_been_used_before():
    password_generator = Password_generator()
    password1 = password_generator.generate_password()
    password2 = password_generator.generate_password()
    assert password2 not in password_generator.used_passwords
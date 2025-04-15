from lib.password_generator import Password_generator

'''
When I call #generate_password
I get a password returned
'''
def test_a_password_is_returned():
    password_generator = Password_generator()
    assert password_generator.generate_password()

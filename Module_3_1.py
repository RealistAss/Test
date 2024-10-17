calls = 0
def count_calls():
    print(calls)
def string_info(string):
        print(string.upper())
        print(string.lower())
def is_contains(string, list_to_search):
             a = [x.lower() for x in list_to_search]
             if string.lower() in a:
                print(True)
             else:
                print(False)
                print(string, a)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

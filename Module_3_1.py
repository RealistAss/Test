calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return(string.lower(), string.upper(), len(string))

def is_contains(string, list_to_search):
       count_calls()
       return string.lower() in (x.lower() for x in list_to_search)



print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)

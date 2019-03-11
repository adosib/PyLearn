# Formatted strings
greeting = 'Hello'
name = 'Ado'
message = '{}, {}. Welcome!'.format(greeting, name)  # {} is a placeholder
print(message)

# F strings
# Does the same as above
message_ = f'{greeting}, {name}. Welcome!'
print(message_)

# The advantage is that you can call methods on the variable easily within the placeholder
message_ = f'{greeting}, {name.lower()}. Welcome!'
print(message_)

# Get info about methods available on strings
print(help(str))

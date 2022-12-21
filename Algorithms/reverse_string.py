def reverse(mystring):
    split_str = mystring.split()
    if type(mystring) != str or len(split_str) < 2:
        return 'nothing to reverse'
    else:
        new_string = ' '.join(split_str[::-1])
        return new_string


string = 'my name is Idris'
string2 = ''
print(reverse(string))
print(reverse(string2))

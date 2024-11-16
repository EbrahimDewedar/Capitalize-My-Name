x = input("type first")
y = input("type last")
def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f"the result is \n {first_name} {last_name}"
print(format_name(x, y))


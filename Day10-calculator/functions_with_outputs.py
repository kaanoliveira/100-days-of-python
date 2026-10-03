def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

format_name("AnGela", "YU")

def format_name2(f_name, l_name):
    formated_f_name2 = f_name.title()
    formated_l_name2 = l_name.title()
    return f"{formated_f_name2} {formated_l_name2}"

formated_string = format_name2("AnGela", "YU")
print(formated_string)

len("Angela")         #len = function; "Angela" = input; "output = output (result of the function)"
output = len("Angela")

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)
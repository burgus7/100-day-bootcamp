def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "Invalid inputs."
    return f"{first_name.title()} {last_name.title()}"

print(format_name("sHwEtA", "burGULa"))


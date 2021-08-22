config = {}
with open("config.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        key, value = line.split("=")
        value = value.replace("\n", "")
        config[key] = value
        print(f"Added key {key} with value {value}")

user_key = input("Which key would you like to see? ")
if user_key not in config:
    print(f"I don't know the key {user_key}")
else:
    val = config[user_key]
    print(f"Current value for {user_key}:{val}")
    next_step = input("Would you like to change?[y/n]")

    if next_step == "y":
        new_val = input("What is the new value? ")
        config[user_key] = new_val

        with open("config.txt", "w") as f:
            for key, value in config.items():
                l = f"{key}={value}\n"
                f.write(l)
ips = []
user_in = ""

while user_in != "done":
    user_in = input("IP addressor type done to exit: ")
    if user_in != "done":
        ips.append(user_in)

print(f"Your IPs are: {ips}")
# See what an OS is based on (Dictionary)

os = {
    "unix": "Independent",
    "bsd": "UNIX",
    "macos": "BSD",
    "gnu/linux": "Independent, Unix-like",
    "minix": "Independent, Unix-like",
}

print("Enter an operating system name to see what it is based on")
while True:
    inp = input("\n> ")
    print(os.get(inp, "\nOperating system not found"))

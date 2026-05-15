"""Ask the user to enter a number of seconds (e.g. 3725).
Convert it to hours, minutes, and remaining seconds using // and %. Print in the format 1h 2m 5s."""


total = int(input("Enter seconds (e.g. 3725): "))
hours = total // 3600
remaining = total % 3600
minutes = remaining // 60
seconds = remaining % 60
print(f"{hours}h {minutes}m {seconds}s")

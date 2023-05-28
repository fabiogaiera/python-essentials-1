# LAB

hours = int(input("Starting time (hours): "))
minutes = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

# Write your code here.

additional_hours = (minutes + duration) // 60
hours = (hours + additional_hours) % 24
minutes = (minutes + duration) % 60

print(hours, ":", minutes, sep="")

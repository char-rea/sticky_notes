# program to get input from user for triathalon award and output the award they get based on their time

swimming = int(input("Enter your swimming time in minutes: "))
cycling = int(input("Enter your cycling time in minutes: "))
running = int(input("Enter your running time in minutes: "))

total_time = swimming + cycling + running

print("Your total time is: ", total_time, "minutes")

if total_time <= 100:
    award = "Provinvial colours"
elif total_time <= 105:
    award = "Provincial half colours"
elif total_time <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

print("Your award is: ", award)      
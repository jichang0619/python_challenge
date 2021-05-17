# Written by Jichang_Kim

def is_on_list(days_list, day):
  if day in days_list:
    return "True"
  else:
    return "False"

def get_x(days_list, num):
  return days_list[num]

def add_x(days_list, day):
  days_list = days_list.append(day)

def remove_x(days_list, day):
  days_list = days_list.remove(day)

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

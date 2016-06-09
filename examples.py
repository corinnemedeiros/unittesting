# Conditional
def get_winner(name_a, score_a, name_b, score_b):
    if score_a > score_b:
        return name_a
    elif score_b > score_a:
        return name_b
    else:
        return name_a + ' ' + name_b

# for loop
def calculate_total(num_list):

    result = 0
    for num in num_list:
        result += num
    return result

# class
class Contact(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = []

    def add_hobby(self, hobby):
        if hobby not in self.hobbies:
            self.hobbies.append(hobby)


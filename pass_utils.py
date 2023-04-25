import random
import string 

def generate_pass(word_list, pass_length):
    password_container = ""
    for words in word_list:
        password_container += "".join(list(words.word))
    
    password = ""
    for i in range(int(pass_length)):
        password += "".join(random.choice(password_container))
    
    return password

# example usage
#my_pass = generate_pass(["Ice Cream", "WaterMellon", "12345667788"], 14)
#print(my_pass)

def check_pass(password):
    score = 0
    for char in password:
        if char in string.ascii_uppercase:
            score += 5
        elif char in string.ascii_lowercase:
            score += 2
        elif char in string.digits:
            score += 3
        elif char in string.punctuation:
            score += 5
            
    return score

#pass_score = check_pass(my_pass)
#print(pass_score)


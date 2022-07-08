from random import *
import os

os.system("clear")
GIVEN_QUESTIONS = {}
CIRCUIT = '''  ---> [Current 1]     ---> [Current 3]
-----{res_1}------------{res_3}------
|                 | [Current 2]     |
|                 | [Voltage 2]     |
{volt_1}       {res_2}        {volt_3}
|                 |                 |
|                 |                 |
-------------------------------------
'''

def random_number(value):
    if value == "voltage": return randint(30,50)
    elif value == "resistance": return randint(5,10)
    else: return None

def fill_data_questions():

    # FILL UP LEFT NODE
    voltage = random_number(value="voltage")
    resistance = random_number(value="resistance")
    GIVEN_QUESTIONS["left"] = {
            "voltage" : voltage,
            "resistance" : resistance,
            "current" : round(voltage/resistance, 2)}
    
    # FILL UP RIGHT NODE
    voltage = random_number(value="voltage")
    resistance = random_number(value="resistance")
    GIVEN_QUESTIONS["right"] = {
            "voltage" : voltage,
            "resistance" : resistance,
            "current" : round(voltage/resistance, 2)}
    
    # FILL UP CENTER NODE
    center_current = GIVEN_QUESTIONS["left"]["current"] - GIVEN_QUESTIONS["right"]["current"]
    resistance = random_number(value="resistance")
    GIVEN_QUESTIONS["center"] = {
        "voltage" : round(center_current * resistance, 2),
        "resistance" : resistance,
        "current" : round(center_current, 2)}
    
def display_circuit():
    
    print(CIRCUIT.format(
        volt_1 = str(GIVEN_QUESTIONS["left"]["voltage"]) + " Volts", 
        res_1 = str(GIVEN_QUESTIONS["left"]["resistance"]) + " Ohms",
        res_2 = str(GIVEN_QUESTIONS["center"]["resistance"]) + " Ohms", 
        res_3 = str(GIVEN_QUESTIONS["right"]["resistance"]) + " Ohms",
        volt_3 = str(GIVEN_QUESTIONS["right"]["voltage"]) + " Volts"
        ))

 

fill_data_questions()
display_circuit()
print(GIVEN_QUESTIONS)
quiz_is_starting = True
while quiz_is_starting:
    # Solve for Current 1
    print("Solve for Current 1")
    ans = input("Your answer: ")
    if ans == str(GIVEN_QUESTIONS["left"]["current"]):
        print("Correct!")

        # Solve for Current 3
        print("Solve for Current 3")
        ans = input("Your answer: ")

        if ans == str(GIVEN_QUESTIONS["right"]["current"]):
            print("Correct!")

            # Solve for Current 2
            print("Solve for Current 2")
            ans = input("Your answer: ")
            if ans == str(GIVEN_QUESTIONS["center"]["current"]):
                print("Correct!")

                # Solve for Voltage 2
                print("Solve for Voltage 2")
                ans = input("Your answer: ")

                if ans == str(GIVEN_QUESTIONS["center"]["voltage"]):
                    print("Congrats! You got it all!")
                    quiz_is_starting = False
                else:
                    print(f"Wrong! Correct answer is {GIVEN_QUESTIONS['center']['voltage']}")

            else:
                print(f"Wrong! Correct answer is {GIVEN_QUESTIONS['center']['current']}")
        
        else:
            print(f"Wrong! Correct answer is {GIVEN_QUESTIONS['right']['current']}")

    else:
        print(f"Wrong! Correct answer is {GIVEN_QUESTIONS['left']['current']}")

    quiz_is_starting = False
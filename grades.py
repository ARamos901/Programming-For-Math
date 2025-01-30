#Aiden Ramos
#Math261
# This program will find the sum of the grades of a student and display their final grade

import time
#imported time so every prompt does not show up super fast for the user

total_quiz=0
low=99

#loops to get quiz grades
for i in range(5):
    temp_grade=int(input(f"\nPlease enter the grade for quiz {i+1}: "))
    
    if temp_grade<low:
        low=temp_grade
    #logic to see which test grade to drop
    
    #adds current grade to total
    total_quiz+=temp_grade
    
    

#drops lowest grade
total_quiz=total_quiz-low

#gets final quiz perctange
quiz_perctange=round((total_quiz/4)*.20,1)
time.sleep(1.5)

total_test=0
for i in range(2):
    temp_grade=int(input(f"\nPlease enter the grade for test {i+1}: "))
    
    #adss current test to total
    total_test+=temp_grade

#gets final test perctange
test_perctange=round((total_test/2)*.50,1)


time.sleep(1.5)
exam=int(input("\nPlease enter the grade for the final exam: "))

#gets final exam perctange
exam_perctange=round(exam*.30,1)

#adds them all together to get final grade
final_grade=round(quiz_perctange+test_perctange+exam_perctange,1)

time.sleep(1)
print("\nGetting the final grade...\n")
time.sleep(3)


#logic to display final grade to user
if final_grade>89.5:
    print("Your final letter grade in the course was an A.")
    
elif final_grade>84.5 and final_grade<89.4:
    print("Your final letter grade in the course was a B+.")
    
elif final_grade>79.5 and final_grade<84.4:
    print("Your final letter grade in the course was a B.")

elif final_grade>74.5 and final_grade<79.4:
    print("Your final letter grade in the course was a C+.")

elif final_grade>69.5 and final_grade<74.4:
    print("Your final letter grade in the course was a C.")

elif final_grade>64.5 and final_grade<69.4:
    print("Your final letter grade in the course was a D+.")

elif final_grade>59.5 and final_grade<64.4:
    print("Your final letter grade in the course was a D.")

else:
    print("Your final letter grade in the course was an F.")

time.sleep(.5)

print(f"\nYour final average in the course was a {final_grade}.")

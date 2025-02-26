#Aiden Ramos
# MTH 261
# Stats Program
# This program will ask the user for a series of user input decimal numbers
# and then find the median, mean, and standard deviation of the data set.

import time as T

# Mean Function

def mean(numbers):
    # Initialize total variable
    total = 0
    # Loop to sum the numbers
    for num in numbers:
        total += num
    # Calculate mean by dividing total by the number of list elements
    mean_value = total / len(numbers)
    return f"{mean_value:.2f}"


# Median Function
def median(numbers):
    # Bubble Sort using for loops
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i] 

    n = len(numbers)
    # Finding the middle index number
    middle_num = n // 2
    
    # If even, average the two middle numbers
    if n % 2 == 0:
        median_value = (numbers[middle_num - 1] + numbers[middle_num]) / 2
    else:
        # If odd, return the middle number, also needs to return a float and not a string
        median_value = float(numbers[middle_num])
    return f"{median_value:.2f}"


# Standard Deviation Function
def standard_deviation(numbers):
    #Initialize Variable for mean and variance
    mean_value = float(mean(numbers))
    variance_sum = 0

    #For loop to total squared differences from mean
    for num in numbers:
        difference = num - mean_value
        # Squaring and adding to total
        variance_sum += (difference**2)
    # Calculate Standard Deviation
    standard_deviation_value = (variance_sum / len(numbers))**0.5
    return f"{standard_deviation_value:.2f}"


# Main Function
def main():
    print("\nPlease answer the questions below to get the Mean, Median, and Standard Deviation of an input list.")
    
    T.sleep(2)

    # Collect numbers from user
    num_count = int(input("\nHow many numbers will you enter: "))
    numbers = []

    for i in range(num_count):
        T.sleep(1)
        #appends numbers to list
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Display Calculations
    print()
    print("\nResults: ")
    print("\nMean:", mean(numbers))
    print("\nStandard Deviation:", standard_deviation(numbers))
    print("\nMedian:", median(numbers))


main()



#Zoom Link:https://gmercyu.zoom.us/rec/play/ygXl0X4kSyntffOvSzfHJTSW4mR_lioqNHk5LqjHiO9v4kALM2pAnn_EXvMh6AD_dRhIj_rn_9bWsqKs.3PmyiphLMP7phcvI?accessLevel=meeting&canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fgmercyu.zoom.us%2Frec%2Fshare%2Fv15fIBWHgYrMuKJtymZDQKM2bHhCUlFtL0Cyw2FmTuoi1p_LGhiSDeXmmWHRPfxo.MZNIVGjeXqnHgd1a
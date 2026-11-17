
def average_score(*args, **kwargs):
    # Use *args for average calculation
    nums = 0
    for num in args:
        nums = nums + num
    average = nums/len(args)

    #print("the average is: {}".format(average))

    for key, value in kwargs.items():
        print(f"{key} = {value}")

    return average

if __name__ == '__main__':
    print(average_score(4, 3, 2, 4, first_name='Carol', last_name='Danvers', major='World_domination'))
    
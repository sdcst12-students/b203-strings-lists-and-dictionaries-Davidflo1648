#!python3

'''
use a for loop to iterate through all possible integers to find the factors of 24
'''
def main(myNumber = 24):
    factors = []

    for i in range(1, myNumber + 1):
        if myNumber % i == 0:
            factors.append(i)
    return factors

print(main())


if __name__ == "__main__":
    main()
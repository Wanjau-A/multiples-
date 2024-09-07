def main():
    number = int(input("Enter number: "))
    result = compute_compactibility(number)
    print(result)


def compute_compactibility(number):
    for i in range(0,101):
        if number % 3 ==  (1, 6, 9, 12):
            return "fizz"
        elif number % 5 == (1, 5, 10, 15, 20):
            return "buzz"
        elif number % 3 and number % 5:
            return"fizzbuzz"
        
if __name__ == "__main__":
    main() 
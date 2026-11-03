def is_even(n: int) -> bool:
    return n % 2 == 0
    

if __name__ == "__main__":
    n = int(input("input random number: "))
    print(is_even(n))
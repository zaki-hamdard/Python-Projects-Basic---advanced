print("Welcome to the prime number checker! \n")

get_number = input("Till which number do you want me to check the prime numbers? default: '100' ")

if not get_number:
    get_number = 100
else:
    get_number = int(get_number)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_numbers = [i for i in range(2, get_number + 1) if is_prime(i)]

print(f"Prime Numbers up to {get_number} are {prime_numbers}")

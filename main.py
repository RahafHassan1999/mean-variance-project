from mean_var_std import calculate

def get_user_input():
    while True:
        try:
            user_input = input("Enter 9 numbers separated by spaces: ")
            numbers = list(map(float, user_input.strip().split()))
            if len(numbers) != 9:
                raise ValueError
            return numbers
        except ValueError:
            print("❌ Please enter exactly 9 valid numbers.")

def print_results(results):
    print("\n✅ Calculation Results:\n")
    for key, value in results.items():
        print(f"{key.title()}: {value}")

if __name__ == "__main__":
    data = get_user_input()
    results = calculate(data)
    print_results(results)
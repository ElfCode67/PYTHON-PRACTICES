import random

# Generate random numbers using list comprehension
numbers = [random.randint(1, 100) for _ in range(15)]
print(f"🔢 Random numbers: {numbers}")

# Lambda functions for operations
even_filter = lambda x: x % 2 == 0
double = lambda x: x * 2
square = lambda x: x ** 2

# Game menu
while True:
    print("\n" + "="*40)
    print("🎮 NUMBER FUN GAME")
    print("1. Get even numbers")
    print("2. Double all numbers")
    print("3. Square all numbers")
    print("4. Find numbers > 50")
    print("5. Generate new numbers")
    print("6. Exit")
    
    choice = input("Choose (1-6): ")
    
    if choice == "1":
        evens = [n for n in numbers if even_filter(n)]
        print(f"✨ Even numbers: {evens}")
        
    elif choice == "2":
        doubled = [double(n) for n in numbers]
        print(f"📈 Doubled: {doubled}")
        
    elif choice == "3":
        squared = [square(n) for n in numbers]
        print(f"🔲 Squared: {squared}")
        
    elif choice == "4":
        big_nums = [n for n in numbers if n > 50]
        print(f"⭐ Numbers > 50: {big_nums}")
        
    elif choice == "5":
        numbers = [random.randint(1, 100) for _ in range(15)]
        print(f"🔄 New numbers: {numbers}")
        
    elif choice == "6":
        print("👋 Goodbye!")
        break
        
    else:
        print("❌ Invalid choice!")
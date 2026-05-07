import requests
import random

BASE_URL = "http://localhost:8000"

def displayGreetings():
    print("Welcome to Python")
    
def Calc(n):
    print (type(n))
    
    ans=(n/10) *10
    print(ans)

def randomNumber():
    number = random.random()
    print(number)
    dice = random.randrange(1, 7)
    print(dice)
    
def contionalStatements():
    n = 10
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
        
def loops():
    for i in range(1, 11):
        print(i)

def whileLoop():
    n = 1
    while n <= 10:
        print(n)
        n += 1
def listExample():
    fruits = ["apple", "banana", "cherry",10]
    fruits.append("mango")
    print(fruits)

def dictExample():
    person = {"name": "Ram", "age": 30, "city": "Kathmandu"}
    print(person)

def setExample():
    unique_numbers = {1, 2, 3, 4, 5}
    print(unique_numbers)
    
def tupleExampe():
    coordinates = (10, 20,"Ram")
    x, y = coordinates
    print(x, y)



def check_api_home():
    """Call the default API route."""
    try:
        response = requests.get(f"{BASE_URL}/")
        response.raise_for_status()
        print("\nAPI Home Response:")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error calling API home: {e}")
    finally:        
        print("API home check completed.")

def main():
    # displayGreetings()
    Calc(286.78)
    randomNumber()
    listExample()
    numP = int(input("Enter a number: "))

if __name__ == "__main__":
    main()
    
    
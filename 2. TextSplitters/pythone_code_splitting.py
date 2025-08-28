from langchain_text_splitters import RecursiveCharacterTextSplitter , Language

text = """
def add_numbers(a, b):
    return a + b

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Main execution
if __name__ == "__main__":
    print(greet_user("Gagan"))
    print("Sum of 5 + 7:", add_numbers(5, 7))
    print("Is 17 prime?", is_prime(17))
    print("Reverse of 'Python':", reverse_string("Python"))
    print("Factorial of 5:", factorial(5))
"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 150, 
    chunk_overlap=0
)

chunks = splitter.split_text(text) 

print( len(chunks))

print( chunks[0])

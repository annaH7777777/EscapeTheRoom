#How can you catch an exception and still see the original error?
#except Exception as e

try:
    result = 10 / 0
except Exception as e:
    print(f"Error: {e}")
# → Error: division by zero
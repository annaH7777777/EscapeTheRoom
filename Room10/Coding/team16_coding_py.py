def analyze_text(data: list):
    total = len(data)
    contains_python = 0
    
    for sentence in data:
        if "python" in sentence.lower():
            contains_python += 1
    
    return {
        "total": total,
        "contains_python": contains_python
    }


if __name__ == "__main__":
    print(analyze_text([
        "I love Python",
        "python is great",
        "I like Java",
        "PYTHON is powerful"
    ]))

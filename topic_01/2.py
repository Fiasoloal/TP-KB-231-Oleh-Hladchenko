# Виконати тестування функцій, 
# що працюють з рядками: strip(), capitalize(), title(), upper(), lower().
def test_string_functions(s):
    stripped = s.strip()
    capitalized = s.capitalize()
    titled = s.title()
    uppercased = s.upper()
    lowercased = s.lower()

    return {
        "strip": stripped,
        "capitalize": capitalized,
        "title": titled,
        "upper": uppercased,
        "lower": lowercased
    }

string = "  hello world  "
results = test_string_functions(string)
for func, result in results.items():
    print(f"{func}: {result}")

# Q6: How do you catch exceptions in Python?
# Options:
#   - catch
#   - try / except
#   - check
#   - handle
# Answer: try / except
#
# Explanation:
# Python uses `try / except` (not `try / catch` as in Java/JS/C++).
# Structure:
#     try:
#         <code that might raise>
#     except <ExceptionType> as e:
#         <handle it>
#     else:
#         <runs only if no exception was raised>
#     finally:
#         <always runs — cleanup like closing files>
# Best practice: catch the *specific* exception you expect, not a bare
# `except:` — a bare except also swallows KeyboardInterrupt and SystemExit,
# which hides real problems and makes debugging miserable.


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"  caught: {e}")
        return None
    except TypeError as e:
        print(f"  caught TypeError: {e}")
        return None
    else:
        print(f"  no error, result = {result}")
        return result
    finally:
        print(f"  finally: done with safe_divide({a}, {b})")


print("-- 10 / 2 --")
safe_divide(10, 2)
print("-- 10 / 0 --")
safe_divide(10, 0)
print("-- 10 / 'x' --")
safe_divide(10, "x")

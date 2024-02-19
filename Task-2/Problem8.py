import random
import string

try:
    password = string.ascii_letters + string.digits
    print("".join(random.choices(password, k=8)))
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
from set import StringSet
from sys import exit

if __name__ == "__main__":
    d_string_set = StringSet("dog", "dear", "deal", "sal", "seal", "cat", "tiger")
    print(d_string_set.query("de"))

    exit(0)

import sys

def function(test):
    print("function works")

function("test")
for line in sys.stdin:
    print("Check " + line)

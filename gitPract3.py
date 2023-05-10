import sys

def print1(*values:object, sep: str = None):
    values = [str(i) for i in values]
    if sep == None:
        values = ' '.join(values)
    else:
        values = sep.join(values)
    sys.stdout.write(values)

print1("Hello", "world", "!")


import re

text = """
102  Py Python
302  C Cu
321  R Ruby
"""
print(re.split("\s+", text))
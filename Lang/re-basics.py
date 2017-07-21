"""
literals, sets, ranges, alternatives, and escapes
all tests here print 2: offset where pattern found
"""

import re

pattern, string = "A.C.", "xxABCDxx"
matchobj = re.search(pattern, string)
if matchogj:
    print(matchobj.start())

pattobj = re.compile("A.*C.*")
matchobj = pattobj.search("xxABCDxx")
if matchobj:
    print(matchobj.start())

print(re.search(" *A.C[DE][D-F][^G-ZE]G\t+ ?", "..ABCDEFG\t..").start())

print(re.search("(A|X)(B|Y)(C|Z)D", "..AYCD..").start())
print(re.search("(?:A|X)(?:B|Y)(?:C|Z)D", "..AYCD..").start())
print(re.search("A|XB|YC|ZD", "..AYCD..").start())
print(re.search("(A|XB|YC|ZD)YCD", "..AYCD..").start())

print(re.search(r"\bABCD", "..ABCD ").start())
print(re.search(r"ABCD\b", "..ABCD ").start())
s


































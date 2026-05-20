Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> dna = input("Enter DNA sequence: ")
...
... a = dna.count("A")
... t = dna.count("T")
... c = dna.count("C")
... g = dna.count("G")
...
... total = len(dna)
...
... gc_content = ((g + c) / total) * 100
...
... print("\n--- DNA Analysis ---")
... print("A:", a)
... print("T:", t)
... print("C:", c)
... print("G:", g)
...
... print("GC Content:", round(gc_content, 2), "%")
...
... rna = dna.replace("T", "U")
...
... print("RNA Sequence:", rna)
...
Enter DNA sequence: ATCGTTAGC

--- DNA Analysis ---
A: 2
T: 3
C: 2
G: 2
GC Content: 44.44 %
RNA Sequence: AUCGUUAGC
>>>

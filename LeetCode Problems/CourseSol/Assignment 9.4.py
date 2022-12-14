"""
9.4 Write a program to read through the mbox-short.txt
 and figure out who has sent the greatest number of mail messages.
 The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
  The program creates a Python dictionary that maps the sender's mail address to a count of the number of
  times they appear in the file.
  After the dictionary is produced, the program reads through the dictionary
  using a maximum loop to find the most prolific committer.
"""
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
frommail = {}
counter = 0
for lines in handle:
    line = lines.rstrip()
    words = line.split()
    if len(words)>0 and words[0]=="From":
        frommail[words[1]] = frommail.get(words[1],0) + 1

largestvalue = -1
resword = None
for k,v in frommail.items():
    #print(k,v)
    if v>largestvalue:
        largestvalue = v
        resword = k
print(resword,largestvalue)




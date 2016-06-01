# Fibonacci
#   This program dislays a specific number in the Fibonacci Sequence.
# Kevin Kredit

def main():
    print "This program dislays a specific number in the Fibonacci Sequence."
    m = input ("Input the number in the Fibonacci sequence you want to print: ")
    x = 1
    n = 0
    for i in range (m):
        a = n + x
        x = n
        n = a
    print a 
      
main()


# for other programs:
def base(fr,to,num):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    b10num,newnum = 0,''
    for n in num:
        b10num = b10num*fr+alphabet.index(n)
    while b10num >= to:
        newnum = alphabet[b10num%to]+newnum
        b10num /= to
    return alphabet[b10num]+newnum

while True:
    fr = input('Current base: ')
    to = input('Desired base: ')
    num = raw_input('Number to be converted: ')
    print '\nThe base',to,'value is: ',base(fr,to,num)+'\n'

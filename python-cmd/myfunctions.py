def base(fr,to,num):#fr = current base, to = desired base, num = #
    num = str(num)
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    bten,newnum = 0,''
    for n in num:
        bten = bten*fr+alphabet.index(n)
    while bten >= to:
        newnum = alphabet[bten%to]+newnum
        bten /= to
    return alphabet[bten]+newnum

def asciitotext(nums):#nums = list of numbers
    message = ''
    for num in nums:
        message += chr(num)
    return message

def texttoascii(message):#message = string of letters
    nums = []
    for ch in message:
        nums.append(ord(ch))
    return nums

def fib(term):#term = term# in fib. seq., term 0 = 0
    curr,new = 0,1
    for i in range(term):
        curr, new = new, curr+new
    return curr

def sidea(side):#side = side length
    x = 1.0
    ret = []
    while True:
        b = (side**2)/(2.0*x)-(x/2.0)
        c = b+x
        print b,c
        if side > b or b > c: break
        if b == int(b) and c == int(c) and side <= b:
            ret.append([float(side),float(b),float(c)])
        x += 1.0
    return ret

def sideb(side):#side = side length
    x = 1.0
    ret = []
    while True:
        a = (2*x*(side+x/2.0))**0.5
        c = side+x
        if a > side or side > c: break
        if a == int(a) and c == int(c) and side >= a and side <= c:
            ret.append([float(a),float(side),float(c)])
        x += 1.0#x+2
    return ret
        
def sidec(side):#side = side length
    x = 1.0
    ret = []   
    while True:
        a = (2*x*(side-x/2.0))**0.5
        b = side-x
        if a > b or b > side: break
        if b == int(b) and a == int(a) and b <= side:
            ret.append([float(a),float(b),float(side)])
        x += 1.0#x+2
    return ret

def quadratic(a,b,c):#a,b,c = equation coefficients
    try:
        discRoot = (b*b-4*a*c)**0.5
        return (-b+discRoot)/(2*a),(-b-discRoot)/(2*a)
    except ValueError:
        return False,False

def prime(num):#num = # to be tested for prime
    #handle 2 situation
    if num%2 == 0: return bool(num==2)
    z = 3.0
    while z**2 <= num:
        if num%z == 0 and z*(num/z) == num:return False
        z += 2.0
    return True

def nprime(n):#n = nth prime
    primer_gen = iter_primes()
    for x in xrange(n):
            result = primer_gen.next()
    return result

def primelist(n):#n = len of list
    primer_gen = iter_primes()
    primes = []
    for x in xrange(n):
            primes.append(primer_gen.next())
    return primes

def iter_primes():
    # handle trivial case
    yield 2
    val = 1
    primesq_pairs = []
    while True:
        curr = None
        while (curr is None):
            val += 2
            curr = val
            for prime, square in primesq_pairs:
                if (curr < square):
                    break
                if (curr % prime == 0):
                    curr = None
                    break
        primesq_pairs.append ((curr, curr**2))
        yield curr

def acronym(message):#message = text to be converted to acronym
    import string
    acr = ''
    for word in string.split(message):
        acr += word[0]
    return string.upper(acr)

def nor(a,b):#a,b = bool values
    return bool(not(a or b))

def nand(a,b):#a,b = bool values
    return bool(not(a and b))

def xor(a,b):#a,b = bool values
    return bool(a and not b or b and not a)

def xnor(a,b):#a,b = bool values
    return bool(not(a and not b or b and not a))

def gcd(a,b):#a,b = nums to have gcd returned
    while b != 0:
        a,b = b,a%b
    return abs(a)

def lcm(a,b):#a,b = nums to have lcm returned
    return a*b/gcd(a,b)

def shuffle(lst):#shuffles a list into a random order
    '''Input a list ot be shuffled'''
    from random import randrange
    shuffled = []
    for i in range(len(lst)):
        shuffled.append(lst.pop(randrange(0,len(lst))))
    return shuffled

def rollDie(numberDice):#returns numberDice values of 1-6 in a list
    from random import randrange
    dieList = []
    for i in range(int(numberDice)):
        dieList.append(randrange(1,7))
    return dieList
    

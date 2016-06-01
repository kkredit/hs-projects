# bonev.py
#       A program to calculate, classify, and count all bonev sequences 
#         of a specific lenght###, and print them to a file.
# Kevin Kredit
# 8/25/10

def main():
    length = input('Length: ')
    # print len(3)###to calculate the number of seqs
    ltolseqs = seqn([1],1,length-1,True)
    print ltolseqs
    ltozseqs = seqn([1],2,length-1,True)
    print ltozseqs
    ztozseqs = []
    ztolseqs = []
    for seq in ltolseqs:
        newseq = []
        for n in seq:
            newseq.append(n+1)
        ztozseqs.append(newseq)
    for seq in ltozseqs:
        newseq = []
        for n in seq:
            newseq = [n]+newseq
        ztolseqs.append(newseq)
    print '1to1:\n',ltolseqs
    print '1to2:\n',ltozseqs
    print '2to2:\n',ztozseqs
    print '2to1:\n',ztolseqs
    input()

def seqn(seq,end,togo,orig):
    if togo == 0:
        return seq+[end]
    else:
        if togo > abs(seq[0]-end)+2:
            if orig:
                return [seq[:len(seq)-1]+seqn([seq[len(seq)-1]+1],end,togo-1,False),\
                       seq[:len(seq)-1]+seqn([seq[len(seq)-1]-1],end,togo-1,False),\
                       seq[:len(seq)-1]+seqn([seq[len(seq)-1]],end,togo-1,False)]
            else:
                return seq[:len(seq)-1]+seqn([seq[len(seq)-1]+1],end,togo-1,False),\
                       seq[:len(seq)-1]+seqn([seq[len(seq)-1]-1],end,togo-1,False),\
                       seq[:len(seq)-1]+seqn([seq[len(seq)-1]],end,togo-1,False)
        add = 1
        if 0 < seq[0] - end:
            add = -1
        elif togo == abs(seq[0]-end)+2:
            if orig:
                return [seq[:len(seq)-1]+seqn([seq[len(seq)-1]+add],end,togo-1,False),\
                       seq[:len(seq)-1]+seqn([seq[len(seq)-1]],end,togo-1,False)]
            else:
                return seq[:len(seq)-1]+seqn([seq[len(seq)-1]+add],end,togo-1,False),\
                       seq[:len(seq)-1]+seqn([seq[len(seq)-1]],end,togo-1,False)
        #elif togo == abs(seq[0]-end)+1:
        else:
            if orig:
                return [seq[:len(seq)-1]+seqn([seq[len(seq)-1]],end,togo-1,False)]
            else:
                return seq[:len(seq)-1]+seqn([seq[len(seq)-1]],end,togo-1,False)

main()






        

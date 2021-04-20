def repl(re,ye,word):
    for y in range(len(c)):
                if c[y]==word:
                    n=input('yes or no')
                    if n=="yes":
                        c[y]=re
                    else:
                        pass
    k=' '.join(c)
    print(k)
    y=open(a,"w")
    y.write(k)
    y.close()
def rep(re,ye,word):
    for y in range(len(c)):
                if c[y]==word:
                    c[y]=re
    k=' '.join(c)
    print(k)
    y=open(a,"w")
    y.write(k)
    y.close()
            
def word():
        print(b)
        word=input('word to be searched')
        if word in c:
            d=c.count(word)
            print(d,word)
            re=input('replaceable word')
            ye=input('replace or 1.replace all')
            if ye=='1' or ye=='replace all':
                rep(re,ye,word)
            elif ye=='2' or ye=='replace':
                repl(re,ye,word)
global a
global b
global c
a=input('file name without format')
b=open(a,"r").read()
c=b.split(' ')
word()

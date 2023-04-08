п=['****',
   '*  *',
   '*  *',
   '*  *']
р=['****',
   '*  *',
   '****',
   '*   ']
abc=[п,р]
alf=['п','р']

a='прпрррппп'

ch=[alf.index(z) for z in a]

for i in range (len(abc[0])):
    for y in range(len(ch)):
        print(abc[ch[y]][i],end=' ')
    print()
    


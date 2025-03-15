from  gauss_jordan import gauss

# a = [[1,1,1,9] , [2,-3,4,13] , [3,4,5,40]]
# gauss(3 , a)

d = {'A' : 0}

for i in range(25):
    d[chr(65+i)] = i

d['0'] = 26
d['1'] = 27
d['2'] = 28
d['3'] = 29
d['4'] = 30
d['5'] = 31
inv_d = {v: k for k, v in d.items()}
# header = input('enter header(enter d for WPI)')
# if header == 'd':
#     header = 'WPI'
# massage = input('enter massage(enter d for j5a0edj2b)')
# if massage == 'd':
#     massage = 'j5a0edj2b'
massage = 'j5a0edj2b'
header = 'WPI'
massage = massage.upper()
print('\n\nheader:', header ,'to binary')
for i in header:
    print(format(d[i] , '05b') ,end=' ')

print('\n\nmassage:', massage ,'to binary')
for i in massage:
    print(format(d[i] , '05b') , end=' ')

m = [1,1,1]
print('\n\nwe XOR firts 3 letters:')
for i in range(3):
    m[i] = d[massage[i]] ^ d[header[i]]
    print(format(int(d[header[i]]) , '05b') ,' XOR ',format(int(d[massage[i]]) , '05b') ,' = ',format(m[i] , '05b'), end='\n')
s = list()
for i in range(5):
    s.append(format(m[0] , '05b')[i])
for i in range(5):
    s.append(format(m[1] , '05b')[i])
for i in range(5):
    s.append(format(m[2] , '05b')[i])
a = list()
print('so first 15 key in keystream is' ,''.join([str(elem) for elem in s]))
print('\n\nnow we make a matrix from arguments of equations and try to solve it with Gauss Jordan method')
for i in range(6):
    if i == 0:
        a.append(s[i+5::-1])
        a[i].append(s[i+6])
    else:
        a.append(s[i+5:i-1:-1])
        a[i].append(s[i+6])

for i in range(6):
    print(a[i])

p= gauss(6 , a)
for i in range(6):
    p[i] = abs(p[i])

for i in range(6):
    print('\np',5-i , ':' , p[i] , end='\t')
j = list(p)
print(type(j[1]))
for i in range(30):
    s.append( (int(s[len(s)-6])*int(j[5])) ^ (int(s[len(s)-5])*int(j[4])) ^ (int(s[len(s)-4])*int(j[3])) ^ (int(s[len(s)-3])*int(j[2])) ^ (int(s[len(s)-2])*int(j[1])) ^ (int(s[len(s)-1])*int(j[0])) )

#listToStr = ''.join([str(elem) for elem in s[0:5]])
j=0
w=0
y=''
print('\n\nnow we have the answers and we\'re able to calculate the rest of keystream:')
print(''.join([str(elem) for elem in s]))
print('we have all the keystream, the rest is simple, we XOR encrypted data with keystream and exract relevant letter\n')
for i in massage:
    r = j*5
    w=0
    for z in range(5):
        #print('w=' , w , 'z=' , z , 's[r]=' ,s[r] ,'int(s[r])=',int(s[r]),'int(s[r])*2^(4-z)=' , int(s[r])*2**(4-z) )
        w += int(s[r])*2**(4-z)
        r += 1
    t = format(d[i] , '05b')
    listToStr = ''.join([str(elem) for elem in s[j*5:(j+1)*5]])
    #print(bin(w))
    print(listToStr ,' XOR ' , t , ' = ' , w ^ int(d[i]) , ' ----> ' ,inv_d[w ^ int(d[i])])
    y = y+inv_d[w ^ int(d[i])]
    # print(t)
    # print(inv_d[w ^ int(d[i])])
    j += 1
print('\nso the data is:   ' , y)

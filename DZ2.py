#Задание 1:
s = '<trsfgFDG&89<<<<//...0989g**fwekiYY'
print(s)
s = s[0:5] + '_' + s[5:10] + '_' + s[10:15] + '_' + s[15:20] + '_' + s[20:25] + '_' + s[25:30] + '_' + s[30:37] + s[-1]
print(s)
z = s.split('_')
#print(type(z))
print(z)
for e in z:
    for i in e:
        if (i == 'F') or (i == 'D') or (i == 'G') or (i == 'Y'):
            print(e)
            break
#Задание 2 (автоматизировать генерацию строки и внос разделителя):
s = 'Y65o*^Rfvw'
s = s*4
print(s)
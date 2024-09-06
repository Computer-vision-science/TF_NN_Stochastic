import sys
'''
#d = [line.strip() for line in sys.stdin]
#d = sys.stdin.read()
#sys.stdout.write('123')
#sys.stdout.write('asd')
t = sys.stdout
sys.stdout = open('log.txt', 'w')
print('111')
print('222')
sys.stdout.close()
sys.stdout = t
print('333')
'''
import sys, datetime

d = [datetime.datetime.strptime(i, '%d.%m.%Y') for i in list(map(str.strip, sys.stdin))]

if d == sorted(d):
    print('ASC')
elif d == sorted(d, reverse=True):
    print('DESC')
else:
    print('MIX')










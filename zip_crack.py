import zipfile
import time
import sys
import itertools

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print bcolors.WARNING + '***************************************************************'
print bcolors.WARNING + '*'+bcolors.ENDC + '                      Author: @Franc15'+bcolors.WARNING+'                       *'
print bcolors.WARNING + '*'+bcolors.ENDC  +bcolors.OKGREEN+ '                       Year: 2017'+bcolors.WARNING+'                            *'
print bcolors.WARNING + '*                                                             *'
print bcolors.WARNING + '*'+bcolors.ENDC + bcolors.FAIL + '                       Crack Cat v1.1'+bcolors.WARNING+'                        *'
print bcolors.WARNING + '***************************************************************' +bcolors.ENDC
z_file = str(raw_input('Enter the zip file to crack : '))
min_n = int(input('Enter minimum password length : '))
max_n = int(input('Enter maximum password length : '))
z=zipfile.ZipFile(z_file, 'r')

a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,./\'[]<>?"{}\|+=)(*&^%$#@!~`'
al=list(a)

print bcolors.OKBLUE + '\n[i] Starting time : %s' % time.strftime('%H:%M:%S')
print u"\u001b[31mCracking..."
def crack():
  for n in range(min_n,max_n+1):
      for xs in itertools.product(al,repeat=n):
           passwd=''.join(xs)
           try:
               sys.stdout.write('\rTrying : %s' % passwd)
               sys.stdout.flush()
               #print "Trying password : %s" %passwd
               z.extractall(pwd=passwd)
               print bcolors.WARNING + "\n[*] Password crack successful!\n"
               print bcolors.WARNING + "[*] Password : %s\n" % passwd
               print bcolors.OKBLUE + '\n[i] Finish time : %s' % time.strftime('%H:%M:%S')

               return 1
           except:
               pass

if(crack()==1):
    sys.exit(0)
else:
    print bcolors.OKBLUE + "Sorry...Password not found!"

from __future__ import division
import random
import time
#for AWS
import boto3
from botocore.errorfactory import ClientError

LAMBDA = 4 #security parameter
N = LAMBDA
P = LAMBDA ** 2
Q = LAMBDA ** 5

#for rounding the number
def quot(z, p):
        return (z + p // 2) // p
        
def mod(z, p):
        return z - quot(z,p) * p

def keygen():
    key = random.getrandbits(P)
    while(key % 2 == 0):	
        key = random.getrandbits(P)
    return key

def encrypt(key, aBit):
    q = random.getrandbits(Q)
    m_a = 2 * random.getrandbits(N - 1)
    c = key * q + m_a + int(aBit)
    return c

#after reading input from user file
def mod(z, p):
        return z - quot(z,p) * p

def decrypt(key, cipherText):
	return mod(cipherText, key) % 2


#Generating the key
key = keygen()
#print(key)
f= open("test.txt","w+")
#functions taking user input
def conv_bin(a):
    b="{0:08b}".format(a)
    enc=[0,0,0,0,0,0,0,0]
    for i in range(len(b)):
        enc[i]=int(b[i])
        #f.write(str(enc[i])+ '\n')
    return enc

#take as input    
a=int(input("Total Cholestrol:"))
b=200
bin_a = conv_bin(a)
bin_b = conv_bin(b)

#now encrypting all bits
enc_a=[0,0,0,0,0,0,0,0]
enc_b=[0,0,0,0,0,0,0,0]
for i in range(8):
    enc_a[i]=encrypt(key,bin_a[i])
    f.write(str(enc_a[i])+ ',')
    enc_b[i]=encrypt(key,bin_b[i])
    f.write(str(enc_b[i]))
    if(i != 7):
        f.write(str(enc_b[i])+ '\n')
f.close()

#now Uploading file

s3=boto3.client('s3')
s3.upload_file('/Users/satyavratgaur/Desktop/MS - Information technology/Semester 2/Advanced Network Security Analysis/Project/projectcode/test.txt','amanibucket','encrypted.txt')


"""
Final part of code - User Machine
"""

def mod(z, p):
        return z - quot(z,p) * p

def decrypt(key, cipherText):
	return mod(cipherText, key) % 2

def quot(z, p):
        return (z + p // 2) // p

#AWS details
s3 = boto3.client('s3', aws_access_key_id='AKIATZ5Q2TITTOQMZCN6', aws_secret_access_key='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')

time_to_wait = 10
time_counter = 0
while (time_counter < time_to_wait):
    time.sleep(1)
    time_counter += 1

client = boto3.client('s3')
content = client.head_object(Bucket='amanibucket',Key='result.txt')
time_to_wait = 10
time_counter = 0
while(content.get('ResponseMetadata',None) is None):
    time.sleep(1)
    time_counter += 1
    if(time_counter > time_to_wait and content.get('ResponseMetadata',None) is None):
        print("file not found")
        break
    else:
        content = client.head_object('amanibucket','result.txt')

s3.download_file('amanibucket','result.txt','/Users/satyavratgaur/Desktop/MS - Information technology/Semester 2/Advanced Network Security Analysis/Project/projectcode/result_1.txt')

with open('/Users/satyavratgaur/Desktop/MS - Information technology/Semester 2/Advanced Network Security Analysis/Project/projectcode/result_1.txt') as f:
        data_dict = f.read()
        p=data_dict.split('\n')
f.close()

def comp_final_out(a):
        arr=a.split(',')
        if(decrypt(key,int(arr[0]))==1):
                return("High risk")
        elif(decrypt(key,int(arr[1])) == 0):
                return("At risk")
        else:
                return("Safe")

def comp_user(arr_comp):
        for i in range(len(arr_comp)):
                res = comp_final_out(arr_comp[i])
                if(res != "equal"):
                        return res
        return res


print(comp_user(p))
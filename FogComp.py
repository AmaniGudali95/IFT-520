from __future__ import division
import json
import boto3
import botocore

s3 = boto3.client('s3', aws_access_key_id='AKIATZ5Q2TITTOQMZCN6', aws_secret_access_key='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')
s3.download_file('amanibucket','encrypted.txt','/Users/satyavratgaur/Desktop/MS - Information technology/Semester 2/Advanced Network Security Analysis/Project/projectcode/computation_res.txt')

#Code at VM (for comparison):
with open('/Users/satyavratgaur/Desktop/MS - Information technology/Semester 2/Advanced Network Security Analysis/Project/projectcode/computation_res.txt') as f:
        data_dict = f.read()
        p=data_dict.split('\n')
f.close()    

f= open("result.txt","w+")
def add(cipherText1, cipherText2):
	return cipherText1 + cipherText2

def mult(cipherText1, cipherText2):
	return cipherText1 * cipherText2

def comparison(c1,c2):
#        print("first",add(mult(c1,c2),c1),"\nsecond",add(c1,c2),"\nthird",add(mult(c1,c2),c1))
        return add(mult(c1,c2),c1),add(c1,c2),add(mult(c1,c2),c1)

def comp_array(arr1,arr2):
        arr_comp=[0 for j in range(8)]
        for i in range(8):
                arr_comp[i] = comparison(arr1[i],arr2[i])
#        print(arr_comp,"LALALLALLALAALAL")
        return arr_comp

enc_a=[0,0,0,0,0,0,0,0]
enc_b=[0,0,0,0,0,0,0,0]

for i in range(len(p)):
    d = p[i].split(',')
    enc_a[i] = int(d[0])
    enc_b[i] = int(d[1])

final_computation = comp_array(enc_a,enc_b)
#print(len(final_computation))

for i in range(len(p)):
    for j in range(3):
        if(j!=2):
                f.write(str(final_computation[i][j]) + ',')
        elif(i!=7):
                f.write(str(final_computation[i][j]) + '\n')
        else:
                f.write(str(final_computation[i][j]))

f.close()
s3=boto3.client('s3')
s3.upload_file('/Users/satyavratgaur/Desktop/MS - Information technology/Semester 2/Advanced Network Security Analysis/Project/projectcode/result.txt','amanibucket','result.txt')
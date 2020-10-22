#basic method
# f = open('C:\\Users\\HP\\Desktop\\test.txt','r')
# #f = open('test.txt','a')
# g = open('test1.txt','w')
# #f = open('test.txt','r+')#read in python
# print(f.read())
# f.close()
# g.close()

#context manager
with open('test1.txt','r+') as f:
    f.write('hello')
    print(f.readline())
    # print(f.readline())
    #for i in f:
     #   print(i)
#print(f.read())
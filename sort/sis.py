#!/usr/bin/python
#encoding:utf-8
#基本思想:

#将一个记录插入到已排序好的有序表中，从而得到一个新，记录数增1的有序表。即：先将序列的第1个记录看成是一个有序的子序列，然后从第2个记录逐个进行插入，直至整个序列有序为止。


def sis(alist):
	length=len(alist)
	for i in range(1,length):
		for j in range(0,i):
			if alist[j]>alist[i]:
				tmp=alist[j]
				alist[j]=alist[i]
				alist[i]=tmp
				break
	return alist


a=[23,16]
b=[34,89,-34,12,34,3434,234.19]

print sis(a)
print sis(b)

				
			

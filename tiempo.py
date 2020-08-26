


import time

print('the time is  : ' , time.ctime())
later =  time.time() + 15 
print ('the time is : ' , time.ctime(later))



print()
print ('-------------------time analizador -----------------')
print()

def show_structu(s):
	print(' year : ' , s.tm_year)
	print(' mon : ' , s.tm_mon)
	print(' moday : '  , s.tm_mday)
	print(' hour : ' , s.tm_hour)
	print(' min : ' , s.tm_min)
	print(' sec : ' , s.tm_sec)
	print(' tm_wday :' , s.tm_wday)
    print(' tm_yday :' , s.tm_yday)
    print(' tm_isdst:' , s.tm_isdst)


# now
now = time.ctime(1483391847.433716)
print('now : ' , now)

#parsed
parsed = time.strptime(now)
print('\nParsed	:')
show_structu(parsed)

#formateado
print('\nformatted : ' ,
	time.strftime("%a %b %d %H:%M:%S %Y", parsed))

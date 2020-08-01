import MySQLdb
    
while (1):
	try:
	    db = MySQLdb.connect("127.0.0.1","iot","iot","iot")
	    cursor = db.cursor()
	    #print("[+] CONNECTED TO DB")
	except:
	    print("[+] UNABLE TO CONNECT TO DB")
	
	sql="select count(*) from acc;"
	try:
	    cursor.execute(sql)
	    r = cursor.fetchone()
	    #print("[+] FETCHED NO OF ROWS")
	except:
	    print("[+]UNABLE TO FETCH ROWS")
	else:
		#print(r)
		s=str(r)
		row=int(s[1])
		print(row)
	        print(pre_count)
	        #time.sleep(5)
		if pre_count < row :
                        a_row = pre_count + 1
			print("[+]ACCIDENT DETECTED" )
			cmd1="select * from acc where s_no="+str(a_row)+";"
                        
			try:
				cursor.execute(cmd1)
				values = cursor.fetchall()
				
			except:
		        	print("[+] UNABLE TO FETCH DATA")
			else:
                pre_count=pre_count+1;
                

import MySQLdb
import datetime
import base64
#import tkinter
from tkinter import messagebox
import time
import os
pre_count=0;
while (1):
	try:
	    db = MySQLdb.connect("127.0.0.1","test","test","iot")
	    cursor = db.cursor()
	    print("[+] CONNECTED TO DB")
	except:
	    print("[+] UNABLE TO CONNECT TO DB")
	
	sql="select count(*) from acc_picam;"
	#r=""
	try:
	    cursor.execute(sql)
	    r = cursor.fetchone()
	    print("[+] FETCHED NO OF ROWS")
	    #db.commit()
	except:
	    print("[+]UNABLE TO FETCH ROWS")
	    #db.rollback()
	else:
		#print(r)
		s=str(r)
		row=int(s[1])
		print(row)
	        print(pre_count)
	        #time.sleep(5)
		if pre_count < row :
			print("[+]ACCIDENT DETECTED" )
			cmd1="select * from acc_picam where sno="+str(row)+";"
			try:
				cursor.execute(cmd1)
				values = cursor.fetchall()
				for i in values:
					date = i[1]
					time1 = i[2]
					c_name1 = i[3]
					c_loc = i[4]
					f_name = i[5]
			except:
		        	print("[+] UNABLE TO FETCH DATA")
			else:
				num = str(c_name1)
				x=int(num[3])+1
				c_name2 = "cam" + str(x)
				#print(date)
				#print(time1)
				#print(c_name1)
				#print(c_name2)
				#print(c_loc)
				#print(f_name)
				txt="ACCIDENT HAPPENED AT : \n"+c_loc+"\n\nACCIDENT DETECTED ON : \n"+time1+"\n\nACCIDENT DETECTED BY : \n"+c_name1+"\t"+c_name2+"\n\nVIDEO IS SAVED BY NAME : \n"+f_name
				messagebox.showerror("ACCIDENT DETECTED ",txt);
				name1=f_name+".mp4"
				name2=f_name+".mp4"
				name2=name2.replace(c_name1,c_name2)
				print(name1+"\n"+name2)
				time.sleep(60)
				print("[+] DELAY COMPLETED")
				cmd2="""sshpass -p "pipipi" scp pi@192.168.43.63:/home/pi/Desktop/files/cam1/acc/merges/%s /root/Desktop/hackathon/a_project/%s"""%(name1,name1)
				#cmd2="""sshpass -p "pipipi" scp pi@10.10.191.39:/home/pi/Desktop/files/cam1/acc/merges/mergerd_cam1_2_8_2019__10:24.mp4 /root/Desktop/hackathon/a_project/%s"""%name1
				#"""sshpass -p "pipipi" scp pi@demo.com:/file/ /root/Desktop/hackathon/a_project/"""	
				cmd3="""sshpass -p "pipipi" scp pi@192.168.43.63:/home/pi/Desktop/files/cam2/acc/merges/%s /root/Desktop/hackathon/a_project/%s"""%(name2,name2)
				#cmd3="""sshpass -p "pipipi" scp pi@10.10.191.39:/home/pi/Desktop/files/cam1/acc/merges/mergerd_cam1_2_8_2019__10:24.mp4 /root/Desktop/hackathon/a_project/%s"""%name2
				#"""sshpass -p "pipipi" scp pi@demo.com:/file/ /root/Desktop/hackathon/a_project/"""
				x=os.system(cmd2)
				os.system(cmd3)
				if x==0:
				    print("[+] FILE COPIED TO THE LOCALHOST AND SAVE AT a_project DIRECTORY")
				else:
				    print("[+] FAILED TO COPY THE FILES")
				name3="merged_"+c_name1+"_"+c_name2+"_"+date+"_"+time1+"_.mp4"
				os.system("ffmpeg -i /root/Desktop/hackathon/a_project/%s -i /root/Desktop/hackathon/a_project/%s  -filter_complex hstack /root/Desktop/hackathon/a_project/merges/%s"%(name1,name2,name3))
				os.system("totem /root/Desktop/hackathon/a_project/merges/%s"%name3)
				pre_count=pre_count+1;

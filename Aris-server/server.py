import MySQLdb
from datetime import *
import base64
#import tkinter
from tkinter import messagebox
import time
import os
import requests
import subprocess

pre_count=0;

def send_sms(date_time,loc,light_no,acc_type,name,car_no,ph_no1,ph_no2):
	try:
		url = "https://www.fast2sms.com/dev/bulk"
		message = name +"'S VECHICLE " + car_no + "\nMIGHT GOT "+acc_type+"\nON LOCATION "+ loc + "\nNEAR THE LIGHT NUMBER "+light_no
		payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+ph_no1+","+ph_no2
		headers = {'authorization': "jG6FRZkW9h0DoqUdAcsaIumEyBgbNlwTYrCMvHK3izP1x4V5JXGCNMdmAPV2le1QI03BjgUFOESviqHn",'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",}
		response = requests.request("POST", url, data=payload, headers=headers)
		print(response.text)
	except:
		print("\n[+]UNABLE TO SEND SMS, TRY SEND IT MANUALLY\n")
    
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
				for i in values:

					sno = str(i[0])
					date_time = str(i[1])
					loc = str(i[2])
					light_no = str(i[3])
					light_seq = str(i[4])
                                        cam_no = str(i[5])
                                        acc_type = str(i[6])
                                        name = str(i[7])
                                        car_no = str(i[8])
                                        ph_no1= str(i[9])
                                        ph_no2= str(i[10])
                                        aadhar= str(i[11])

			except:
		        	print("[+] UNABLE TO FETCH DATA")
			else:
				#print(sno)
				#print(date_time)
                                txt="ACCIDENT HAPPENED AT : \n"+loc+"\n\nACCIDENT DETECTED ON : \n"+date_time+"\n\nACCIDENT DETECTED BY : \n cam \t"+cam_no+"\n\nLIGHT NUMBER : \n"+light_no+"\n\nACCIDENT TYPE : \n"+acc_type+"\n\nNAME OF THE CAR OWNER : \n"+name+"\n\nCAR NUMBER : \n"+car_no+"\n\nPHONE NUMBER 1 : \n"+ph_no1+"\n\nPHONE NUMBER 2 : \n"+ph_no2+"\n\nAADHAR NUMBER : \n"+aadhar+"\n\nVIDEO IS SAVED BY NAME : \n"
				messagebox.showwarning("ACCIDENT DETECTED ",txt);
                            
                                send_sms(date_time,loc,light_no,acc_type,name,car_no,ph_no1,ph_no2)
                                no1,no2,no3,no4 = cam_no.split(',')
                                cam1 = "cam"+str(no1)
                                cam2 = "cam"+str(no2)
                                cam3 = "cam"+str(no3)
                                cam4 = "cam"+str(no4)
                                #print(cam1,cam2,cam3,cam4)
                                dt1 = datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S")
                                dt2 = dt1 - timedelta(seconds=60)
                                dt5 = dt1 + timedelta(seconds=60)
                                dt3 = str(dt1)[:-3]
                                dt6 = str(dt5)[:-3]
                                dt4 = str(dt2)[:-3]
                                #print(dt3)
                                #print(dt2)
				time.sleep(120)
				print("[+] DELAY COMPLETED")
                                i = 0
                                while i<4:
                                    if i==0:
                                        a = "ls /home/iot/cam/%s/*'"%cam1 + dt4 + "'*.mp4"
                                        b = "ls /home/iot/cam/%s/*'"%cam1 + dt3 + "'*.mp4"
                                        c = "ls /home/iot/cam/%s/*'"%cam1 + dt6 + "'*.mp4"
                                        print(a,b)
                                        x = (subprocess.check_output(a,shell=True))[:-1]
                                        y = (subprocess.check_output(b,shell=True))[:-1]   
                                        xx= (subprocess.check_output(c,shell=True))[:-1]
                                        #print(x,y)
                                        os.system("""echo "file '%s'\nfile '%s'\nfile '%s'"> /root/Desktop/acc/videos/concat1/concat.txt"""%(x,y,xx))
                                        i = i+1
                                    if i==1:
                                        a = "ls /home/iot/cam/%s/*'"%cam2 + dt4 + "'*.mp4"
                                        b = "ls /home/iot/cam/%s/*'"%cam2 + dt3 + "'*.mp4"
                                        c = "ls /home/iot/cam/%s/*'"%cam2 + dt6 + "'*.mp4"
                                        #print(a,b)
                                        m = (subprocess.check_output(a,shell=True))[:-1]
                                        n = (subprocess.check_output(b,shell=True))[:-1]
                                        mm= (subprocess.check_output(c,shell=True))[:-1]
                                        os.system("""echo "file '%s'\nfile '%s'\nfile '%s'"> /root/Desktop/acc/videos/concat2/concat.txt"""%(m,n,mm))                                                
                                        i = i+1
				    if i==2:
                                        a = "ls /home/iot/cam/%s/*'"%cam3 + dt4 + "'*.mp4"
                                        b = "ls /home/iot/cam/%s/*'"%cam3 + dt3 + "'*.mp4"
                                        c = "ls /home/iot/cam/%s/*'"%cam3 + dt6 + "'*.mp4"
                                        #print(a,b)
                                        o = (subprocess.check_output(a,shell=True))[:-1]
                                        p = (subprocess.check_output(b,shell=True))[:-1]
                                        oo= (subprocess.check_output(c,shell=True))[:-1]
                                        os.system("""echo "file '%s'\nfile '%s'\nfile '%s'"> /root/Desktop/acc/videos/concat3/concat.txt"""%(o,p,oo))                                                
                                        i = i+1
				    if i==3:
                                        a = "ls /home/iot/cam/%s/*'"%cam4 + dt4 + "'*.mp4"
                                        b = "ls /home/iot/cam/%s/*'"%cam4 + dt3 + "'*.mp4"
                                        c = "ls /home/iot/cam/%s/*'"%cam4 + dt6 + "'*.mp4"
                                        #print(a,b)
                                        q = (subprocess.check_output(a,shell=True))[:-1]
                                        r = (subprocess.check_output(b,shell=True))[:-1]
                                        qq= (subprocess.check_output(c,shell=True))[:-1]
                                        os.system("""echo "file '%s'\nfile '%s'\nfile '%s'"> /root/Desktop/acc/videos/concat4/concat.txt"""%(q,r,qq))                                                
                                        i = i+1
                                #concat1 = """ffmpeg -i /home/iot/cam/"""+cam1+"/*'"+dt4+"""'*.mp4 -i /home/iot/cam/"""+cam1+"/*'"+dt3+"""'*.mp4 -filter_complex concat=n=2:v=1:a=1 -f MOV -vn -y /root/Desktop/acc/videos/concat1/'"""+cam1+"_concat_"+dt3+".mp4'"
				os.system("""chmod 777 '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s'"""%(x,y,m,n,o,p,q,r,xx,mm,oo,qq))
				concat1 = """ffmpeg -f concat -safe 0 -i /root/Desktop/acc/videos/concat1/concat.txt -c copy /root/Desktop/acc/videos/concat1/'"""+cam1+"_concat_"+dt3+".mp4'"
				concat2 = """ffmpeg -f concat -safe 0 -i /root/Desktop/acc/videos/concat2/concat.txt -c copy /root/Desktop/acc/videos/concat2/'"""+cam2+"_concat_"+dt3+".mp4'"
				concat3 = """ffmpeg -f concat -safe 0 -i /root/Desktop/acc/videos/concat3/concat.txt -c copy /root/Desktop/acc/videos/concat3/'"""+cam3+"_concat_"+dt3+".mp4'"
				concat4 = """ffmpeg -f concat -safe 0 -i /root/Desktop/acc/videos/concat4/concat.txt -c copy /root/Desktop/acc/videos/concat4/'"""+cam4+"_concat_"+dt3+".mp4'"
                                #print(concat1)
                                #print(concat2)
                                #print(concat3)
                                #print(concat4)
				#merge the one minute video
				os.system(concat1)
				os.system(concat2)
				os.system(concat3)
				os.system(concat4)

                                #4 video merge
				out_name = "merged_"+cam1+"_"+cam2+"_"+cam3+"_"+cam4+"_"+dt3+".mp4"
				name1 = cam1+"_concat_"+dt3+".mp4"
				name2 = cam2+"_concat_"+dt3+".mp4"
				name3 = cam3+"_concat_"+dt3+".mp4"
				name4 = cam4+"_concat_"+dt3+".mp4"
				render4 = """ffmpeg -i '/root/Desktop/acc/videos/concat1/%s' -i '/root/Desktop/acc/videos/concat2/%s' -i '/root/Desktop/acc/videos/concat3/%s' -i '/root/Desktop/acc/videos/concat4/%s' -f lavfi -t 0.1 -i anullsrc -filter_complex "[0:v][1:v]hstack[top]; [2:v][3:v]hstack[bottom]; [top][bottom]vstack,format=yuv420p[v]; [4:a][4:a][4:a][4:a]amerge=inputs=4[a]" -map "[v]" -map "[a]" -ac 2 '/root/Desktop/acc/videos/merges/%s'"""%(name1,name2,name3,name4,out_name)
				os.system(render4)
				print(render4)
                                os.system("totem '/root/Desktop/acc/videos/merges/%s'"%out_name)

                                pre_count=pre_count+1;
                else:
                    print("[+] EVERYTHING IS FINE")

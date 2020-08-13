#!/bin/bash
source /home/hduser/.bashrc

/usr/local/sqoop/bin/sqoop import --bindir /usr/local/sqoop/lib --connect jdbc:mysql://localhost/student --username root --password redhat --table student --incremental append --check-column sid --last-value $last_value --target-dir /user/hduser/data_new --m 1

x=`/usr/local/sqoop/bin/sqoop eval --connect jdbc:mysql://localhost/student --username root --password redhat --query "select sid from student order by sid desc limit 1"  | tail -n 2 | head -n 1 | awk '{print $2}'`

sed -i s'/last_value=[0-9]*/last_value='$x'/g' /home/hduser/.bashrc


#put this file into /home/hduser location
#--> chmod a+x /home/hduser/sqoop_backup.sh
#first schedule your job using crontab -e as 
#-->00	02	*	*	*	/home/hduser/sqoop_backup.sh
#vim /home/hduser/.bashrc
#-->export last_value=1010 #last value of particular column 
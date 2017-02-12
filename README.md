# Vault---Test-Automation
A Test Suite for the Vault Project - Used as an accessory for PolyPassword Hasher Project


Output Sample: (Update as per the current stage)

------> WEB

-----------  Vault Automation Test  -----------
This program executes some test cases to evaluate VAULT
Enter the IP Address of the host: 192.168.1.151
Enter the Username of the host: ubuntu
Enter the Password of the host: ubuntu
Enter the choice of connectivity (SSH/WEB)? web
Enter the port number of the request: 9200
Connecting to host 192.168.1.151...

{"initialized":true,"sealed":false,"standby":false,"server_time_utc":1486930139,"version":"0.6.5","cluster_name":"vault-cluster-25da058a","cluster_id":"509aee2f-98d7-42b3-d9a7-7357cd2bb325"}

Request to http://192.168.1.151:9200/v1/sys/seal-status
{"sealed":false,"t":1,"n":1,"progress":0,"nonce":"","version":"0.6.5","cluster_name":"vault-cluster-25da058a","cluster_id":"509aee2f-98d7-42b3-d9a7-7357cd2bb325"}

None

BEGIN: Test Case Execution ---->

Basic TestCase: 


------> SSH

/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 /Users/darkknight/PycharmProjects/PPH-Vault/main.py
-----------  Vault Automation Test  -----------
This program executes some test cases to evaluate VAULT
Enter the IP Address of the host: 192.168.1.151
Enter the Username of the host: ubuntu
Enter the Password of the host: ubuntu
Enter the choice of connectivity (SSH/WEB)? ssh
Connecting to host 192.168.1.151...

The Machine Details are Linux ubuntu 4.8.0-22-generic #24-Ubuntu SMP Sat Oct 8 09:15:00 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux


The Vault Status is [] 


BEGIN: Test Case Execution ---->

Basic TestCase:

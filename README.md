# oscp-scripts
Scripts created to use with the OSCP exercises

## snmp_user_discovery.py
Use this script to scan a list of ip addresess for a list of usernames
*use python2*

### Example usage
```
# ./snmp_user_discovery.py users.txt ips.txt
['root', 'admin', 'administrator', 'webadmin', 'sysadmin', 'netadmin', 'guest', 'user', 'web', 'test', 'jenny', 'joe45', 'john', 'marcus', 'ryuu']
['10.11.1.227', '10.11.1.72', '10.11.1.115', '10.11.1.217', '10.11.1.231', '10.11.1.241']
testing user root on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user root
testing user admin on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user admin
testing user administrator on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user administrator
testing user webadmin on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user webadmin
testing user sysadmin on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user sysadmin
testing user netadmin on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user netadmin
testing user guest on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user guest
testing user user on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user user
testing user web on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user web
testing user test on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user test
testing user jenny on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user jenny
testing user joe45 on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user joe45
testing user john on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user john
testing user marcus on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user marcus
testing user ryuu on ip 10.11.1.227
successful connection to ip 10.11.1.227 for user ryuu
```

### users.txt
```
root
admin
administrator
webadmin
sysadmin
netadmin
guest
user
web
test
jenny
joe45
john
marcus
ryuu
```

### ips.txt
```
10.11.1.72
10.11.1.115
10.11.1.217
10.11.1.227
10.11.1.231
10.11.1.241
```

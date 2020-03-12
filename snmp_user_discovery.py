#!/usr/bin/python
#snmp_user_discovery.py
import socket 
import sys
if len(sys.argv) != 3:
        print "Usage: snmp_user_discovery.py <username_list.txt> <ip_list.txt>"
        sys.exit(0)


def gen_user_list(users):
    users_list = []
    with open(users, "r") as file:
        for user in file:
            users_list.append(user.strip("\n"))
    return users_list

def gen_rhost_list(rhosts):
    rhosts_list = []
    with open(rhosts, "r") as file:
        for host in file:
            rhosts_list.append(host.strip("\n"))
    return rhosts_list

def send_verify(ip, user):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    print("testing user {} on ip {}".format(user, ip))
    try:
        connect=s.connect((ip,25))
        banner=s.recv(1024)
        data = b'VRFY ' + user.encode() + b'\r\n' 
        s.send(data)
        result = s.recv(1024)
        print("successful connection to ip {} for user {}".format(ip, user))
        return user
        s.close()
    except Exception:
        return False
def main():
    hostFile=sys.argv[2]
    ipFile=sys.argv[1]
    rhosts = gen_rhost_list(hostFile)
    users = gen_user_list(ipFile)
    print (users)
    print (rhosts)

    for ip in rhosts:
        for user in users:
                send_verify(ip, user)


if __name__ == "__main__":
    main()

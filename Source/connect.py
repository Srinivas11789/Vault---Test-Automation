#!/usr/bin/python

import socket
import sys
import time
import paramiko

def connect(host, username, password):
    handle = 0
    try:
        handle = paramiko.SSHClient()
        handle.load_system_host_keys()
        handle.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        handle.connect(host, port=22, username=username, password=password, timeout=10)
        sys.stdout.write("Connecting to host %s" % host)
        for i in range(3):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(1)
        print ("\n")
        handle.exec_command("\n")
        return handle

    except socket.timeout:
        print ("\nNo Connection to the Host: %s " % (host))
        sys.exit()
    except socket.error:
        print ("\nConnection attempt Failed. Please check your Connectivity")
        sys.exit()
    except EOFError:
        print ("ERROR: SSH Connection Closed")
        sys.exit()


def sendcmd(handle,command):
    stdin, stdout, stderr = handle.exec_command(command)
    return stdout,stderr
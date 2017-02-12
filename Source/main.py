import connect
import sys
import web

def main():
    print """-----------  Vault Automation Test  -----------"""
    print """This program executes some test cases to evaluate VAULT"""
    host = raw_input('Enter the IP Address of the host: ')
    user = raw_input("Enter the Username of the host: ")
    password = raw_input("Enter the Password of the host: ")
    ch = raw_input("Enter the choice of connectivity (SSH/WEB)? ")

    if (ch == "SSH" or ch == "ssh"):
        handle = connect.connect(host, user, password)
        out, err = connect.sendcmd(handle, "uname -a")
        print ("The Machine Details are %s \n" % out.readlines()[0])
        out, err = connect.sendcmd(handle, 'vault')
        print ("The Vault Status is %s \n" % out.readlines())
    elif (ch == "WEB" or ch == "web"):
        port = raw_input("Enter the port number of the request: ")
        handle = web.request(host,"sys/health",port)
        print web.url(handle + "sys/seal-status")
    else:
         print ("Enter the Right Choice ! \n")
         sys.exit()

    print "\nBEGIN: Test Case Execution ---->\n"
    print "Basic TestCase: "
    print """"""

main()









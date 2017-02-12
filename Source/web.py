import urllib2,socket
import sys,time
def request(host,url,port):
    get = "http://%s:%s/v1/" % (host,port)
    try:
        handle = urllib2.Request(get + url)
        result = urllib2.urlopen(handle)
        sys.stdout.write("Connecting to host %s" % host)
        for i in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1)
        print ("\n")
        print(result.read())
        return get
    except urllib2.HTTPError, e:
        print e
    except urllib2.URLError, e:
        print e.args
    except socket.timeout:
        print ("\nNo Connection to the Host: %s " % (host))
        sys.exit()


def url(url):
    print "Request to %s" % (url)
    try:
        result = urllib2.urlopen(url)
        print(result.read())
    except urllib2.HTTPError, e:
        print e
    except urllib2.URLError, e:
        print e.args
    except socket.timeout:
        print ("\nNo Connection to the Host %s!" % (url))
        sys.exit()
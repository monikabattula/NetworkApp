import sys
import subprocess

#Checking IP reachability
def ip_reach(list):

    for ip in list:
        ip = ip.rstrip("\n")
        #here using the call command ping to check the reachability of the IP address
        # we have ping then the string formate operator percent s and then we add in backslash n and two, which means the number of echo requests to be sent each device.

        ping_reply = subprocess.call('ping %s -n 2' % (ip,), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #if ping reply is 0 then the device is reachable and we print the message that the device is reachable.then using continue statement right here we move to evaluate the reachablility of the next ip address
        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue
        
        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()
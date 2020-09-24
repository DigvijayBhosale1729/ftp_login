#Made by FoxSinOfGreed
#Thanks to TJ O'Connor The author of Violent Python


import ftplib
import optparse
import socket

def anonlogin(hostname,password):
    try:
        ftp=ftplib.FTP(hostname)
        ftp.login('anonymous', str(password))
        print('\n')
        print('Anonymous login to '+hostname+' with password '+password+' succeeded')
        ftp.quit()
        return True
    except:
        print('Anonymous login failed')
        return False
def main():
    usage = "usage: python3 ftp_login [options] argument use -h for help"
    parser=optparse.OptionParser(usage=usage)
    parser.add_option('-H', dest='hostname', type='string', help='Specify hostname')
    parser.add_option('-p', dest='passwd', type='string', help='Specify password you want to provide')
    (options, args)=parser.parse_args()
    passwd=options.passwd
    hostname=options.hostname
    try:
        print("Resolving the hostname to IP address")
        hostname=socket.gethostbyname(hostname)
    except:
        print('Could not resolve the hostname')
        print('If you entered an ip address like 167.99.11.102 the program might still work, do you want to go ahead? (y/n)')
        f=input()
        if f=='N' or f=='n':
            exit(0)
        elif f=='Y' or f=='y':
            pass
        else:
            print('Incorrect input, exiting')
            exit(0)    
    f=anonlogin(hostname, passwd)
main()

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,subprocess
import pexpect
import pdb

"""
python作成の定型文
Usage :
"""

__author__  = 'SANCHU'
__version__ = '1.0.0'
__date__    = 'YYYY/MM/DD'

PASSWORD_PROMPTS=["パスワード:", "password:"]
ROOT_PROMPT='#'
ROOT_PASSWORD='yasuyuki'
USER_PROMPT='\$'
USER_PASSWORD='yasuyuki'
DEBUG_LOG = None

def testFunc():
    #sessTest = pexpect.spawn("/bin/bash")
    sessTest = pexpect.spawn("/usr/bin/ssh 192.169.0.151" , encoding='utf-8')
    sessTest.logfile_read = DEBUG_LOG
    #sessTest.logfile_send = DEBUG_LOG
    #sessTest.sendline("echo aaaaa")
    #sessTest = pexpect.spawn("ssh 192.169.0.151")
    #sessTest.expect("#")
    #sessTest.sendline("/usr/bin/ssh 192.169.0.151")
    sessTest.expect("password:")
    #sessTest.expect_exact(PASSWORD_PROMPTS, timeout=15)
    sessTest.sendline("yasuyuki")
    sessTest.expect("#")
    sessTest.sendline("ls -l")
    print("testFunc")

def sshTest():
    child = pexpect.spawn('ssh 192.169.0.151' , encoding='utf-8') 
    child.logfile_read = sys.stdout
    child.expect(PASSWORD_PROMPTS)
    child.sendline("yasuyuki")
    child.expect("\$")
    child.sendline("su -")
    child.expect(PASSWORD_PROMPTS)
    child.sendline("yasuyuki")
    #child.sendline("yasuyuki")
    child.sendline("ls -l")
    child.expect("\#")
    child.sendline("ps -efww")
    child.expect("\#")
    child.sendline("exit")
    child.expect("\$")
    child.close()    
    subprocess.call(["ls","-la"]) 

# Main
if __name__ == "__main__":
    #testFunc()
    sshTest()

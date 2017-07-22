import subprocess
import os
import shlex

def main():
    cmd = "ls -l"
    print cmd
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out = p.communicate()
    print out[0]
    #print out
    # if "LinkedList.py" in

    print "Using shlex:"
    arg = shlex.split(cmd)
    print "args: {}".format(arg)
    p1 = subprocess.call(arg)
    # print p1

if __name__ == '__main__':
    main()

import os
import time
import sys
import stat
import shutil
import platform
import time





# Using the os module to get information about a file
def dump(file):
    print("stat", file)
    st = os.stat(file)
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print("- size:", size, "bytes")
    print("- owner:", uid, gid)
    print("- created:", time.ctime(ctime))
    print("- last accessed:", time.ctime(atime))
    print("- last modified:", time.ctime(mtime))
    print("- mode:", oct(mode))
    print("- inode/dev:", ino, dev)

dump('minishell.py')

# change current directory
def chdir(directory):
    print("Current directory:")
    cwd = os.getcwd()
    print(cwd)
    os.chdir(directory)
    cwd = os.getcwd()
    print("Changed directory:")
    print(cwd)


# display current directory
def cudir():
    print("Current directory:")
    cwd = os.getcwd()
    print(cwd)


# Directory changed to parent directory
def pdir():
    print("Directory changed")
    os.chdir(os.pardir)
    print(os.getcwd())


# list elements of directory
def ldir(directory):
    print("Elements of directory:" + directory)
    for file in os.listdir(directory):
        print(file)


# used to list directory elements

def fc(directory):
    return os.chdir(directory)


# create directory
def mkd(directory):
    os.mkdir(directory)
    print(directory + " CREATED")


# delete directory
def dld(directory):
    os.rmdir(directory)
    print(directory + " deleted")


# Return the real group id of the current process.
def rgid():
    print(os.getgid())


# return the current process’s user id.
def uid():
    # id=os.getuid()
    print(os.getuid())


# Returns the real process ID of the current process.
def rpid():
    print(os.getpid())


# Return information identifying the current operating system.
def cos():
    # print(os.uname())
    platform.platform()
    print(platform.platform())

# delete file
def df(file):
    os.remove(file)
    print(file + " deleted")

# specifies OS type
def oname():
    print("OS name is " + os.name)


# used to nename text files
def rname(filename, newname):
    os.rename(filename, newname)
    print(filename + " renamed to " + newname)


def help():
    print(
        " dump(file) \n chdir(directory) \n cudir()  \n pdir()  \n ldir(directory) \n ldir() \n fc(directory) \n mkd(directory) \n dld(directory) \n rgid() \n uid(): \n rpid() \n cos() \n df(file) \n oname() \n rname(filename,newname)")



while True:
    input_str = input(os.getcwd()+">")
    if 'dump ' in input_str:
        final_input = input_str.replace('dump ', '')
        dump(final_input)
    elif 'chdir ' in input_str:
        final_input = input_str.replace('chdir ', '')
        chdir(final_input)
    elif 'cudir' in input_str or 'cudir ' in input_str:
        cudir()
    elif 'pdir' in input_str or 'pdir ' in input_str:
        pdir()
    elif 'ldir ' in input_str:
        final_input = input_str.replace('ldir ', '')
        ldir(final_input)
    elif 'fc' in input_str:
        final_input = input_str.replace('fc ', '')
        print(fc(final_input))
    elif 'mkd ' in input_str:
        final_input = input_str.replace('mkd ', '')
        mkd(final_input)
    elif 'dld ' in input_str:
        final_input = input_str.replace('dld ', '')
        dld(final_input)
    elif 'rgid' in input_str or 'pdir ' in input_str:
        rgid()
    elif 'uid' in input_str or 'uid ' in input_str:
        uid()
    elif 'rpid' in input_str or 'rpid ' in input_str:
        rpid()
    elif 'cos' in input_str or 'cos ' in input_str:
        cos()
    elif 'df ' in input_str:
        final_input = input_str.replace('df ', '')
        df(final_input)
    elif 'oname' in input_str or 'oname ' in input_str:
        oname()
    elif 'rname ' in input_str:
        final_input = input_str.replace('rname ', '')
        names = final_input.split(sep=' ')
        old_name = names[0]
        new_name = names[1]
        rname(old_name,new_name)
    elif 'help' in input_str or 'help ' in input_str:
        help()
    else:
        print('command not found..!')




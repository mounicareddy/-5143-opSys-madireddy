

import os
import sys
import shutil
import stat
import time
from os.path import expanduser
import os.path



class historyManager(object):
    def __init__(self):
        self.command_history = []

    
    def push_command(self,cmd):
        self.command_history.append(cmd)
        
    
    def get_commands(self):
        return self.command_history
        
    
    def number_commands(self):
        return len(self.command_history)


class parserManager(object):
    def __init__(self):
        self.parts = []
    
    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts
        

class commandManager(parserManager):
    def __init__(self):
        self.command = None

    
    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command
		
		

    
    def ls(self):
        for dirname, dirnames, filenames in os.walk('.'):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))
        for dirname, dirnames, filenames in os.walk('.'):
        # print path to all filenames.
            for filename in filenames:
                print(os.path.join(dirname, filename))
               
    def lsf(self,flag):
        files_info=[]
        if(flag=='-m' or flag=='-s' or flag=='-a'  or flag =='-c'):
            for file_name in os.listdir('.'):
                file_stats=os.stat(file_name)
                file_info = [
                file_name,
                file_stats [stat.ST_SIZE],
                oct(stat.S_IMODE(file_stats.st_mode))[2:],
                time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME])),
                time.strftime("%m/%d/%Y %I:%M:%S %P",time.localtime(file_stats[stat.ST_ATIME])),
                time.strftime("%m/%d/%Y &I:%M:%S %p",time.localtime(file_stats[stat.ST_CTIME]))
                ]
                files_info.append(file_info)
        
        else:
            print ("wrong arguement")       
        #checks whether the arguement is recognised or not
        if(flag=='-m'): 
            files_info.sort(key=lambda x:time.strftime((x[3])))#sorts files_info.sort based on 3 item in list(Mtime)
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t{}\t{}\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        elif(flag=='-s'):
            files_info.sort(key=lambda x:time.strftime((x[2])))#sorts files_info.sort based on 3 item in list(Size)
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t{}\t{}\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        elif(flag=='-a'):
            files_info.sort(key=lambda x:time.strftime((x[4])))#sorts files_info.sort based on 3 item in list(Atime)
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t{}\t{}\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        elif(flag=='-c'):
            files_info.sort(key=lambda x:time.strftime((x[5])))#sorts files_info.sort based on 3 item in list(Ctime)
            
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t{}\t{}\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        
            
    
#cat command
    
    def cat(self,file):
        if(os.path.isfile(file)): 
            #checks whether file exists or not if it exists it opens file. 
            f = open(file,'r')#open file in read mode
            print(f.read())
            
        else:
        #if file does not exist 
            print("file does not exist")
            
# remove command            
            
    def rm(self,file):
        if os.path.exists(file):
        #checks whether the file exists or not if not exists then throws an exception
            try:
                os.remove(file)
            except :
                print("Error: %s - %s" % (e.file, e.strerror))
        else:
            print("sorry, i cannot find %s file" %file)#if file not found
		
 #wordcount
			
    def wc(self,file):
        if os.path.isfile(file):#checks whether file exists or not
            
            f= open(file,'r')#if exists open file in read mode
            wordcount={}#dictionary which is used to store word and its word count
        
            for word in f.read().split():#for each word it split
                if word not in wordcount: #count each word
                    wordcount[word] = 1
                else:
                    wordcount[word] +=1
            for key in wordcount.keys():
                print (key , wordcount[key])#prints words and its occurence
            f.close();
        else:
            print("sorry file not found")#if file does not exists
        
        
 # linecount
    def wcf(self,flag,file):
        if os.path.isfile(file):#checks whether file exists or not 
            f=open(file,'r') #if file exists open file in read mode
            count=0 #initialize number of lines to 0
            with open(file,'r')as f:
                for line in f:  #for each line increment count by one
                    count+=1
            print (count)  #return number of lines
        else:
            print("sorry,file not found")        
                
		    
        
		
#move command	
    def mv(self,src,dest):
        if os.path.isfile(src):
        #checks whether source file exists or not
            if os.path.isfile(dest): #checks whether destination file exists or not       
                shutil.copyfile('src','dest')#if both files exists then copies source to destination file
            else:
                print("dest file not found")
        else:
            print("source file not found")
        
#changing permissions		
    def chmod(self,file):
        os.chmod(file,0o777 )
        print(" mode succesfully updated")	

#copying one file to another		
		
    def cp(self,src, dest):
        try:
        
            shutil.copy(src, dest)
    # eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
    # eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)	
      
# changing directory      
   
    def cd(self,directory):
        if (directory=='..'):#change directory to previous directory
            os.chdir('..')
            new=os.getcwd()
            print(new)
        if(directory=='~'):#change directory to homedirectory
            curdir=os.getcwd()
            print(curdir)
            home=expanduser("~")
            print(home)
        else:
            if os.path.isdir(directory):#checks whether given arguement is directory or not
                os.chdir(directory)
            else:        
                print("directory does not exist")
    
#history of commands    
    def history(self):
        count=0
        history=self.get_commands()#gets history of commands 
        for cmd in commandlist:#printing the commands in history
            count += 1
            ouput = str(count)+ " " +cmd
            print(output)
        
    
    
class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
        
    
    def runShell(self):
        number_commands = 0
        while True:
            self.input = input("parser-$ ")         # get command
            self.history.push_command(self.input)   # put in history
            parts = self.commands.run_command(self.input)
            print(parts)

            

            #print(parts[0])
			
            if parts[0] == 'cat':
                if(len(parts)==2):
                    self.commands.cat(parts[1])
                else:
                    print("wrong number of arguements")
            elif parts[0]=='ls':
                if(len(parts)==1):
                    self.commands.ls()
                elif(len(parts)==2 ):
                    self.commands.lsf(parts[1])
            elif parts[0]=='cp':
                self.commands.cp(parts[1],parts[2])
            elif parts[0]=='rm':
                if(len(parts)==2):
                    self.commands.rm(parts[1]) 
                else:
                    print(" wrong number of arguements")               
                            
            elif parts[0]=='wc':
                if(len(parts)==2):
                    self.commands.wc(parts[1])
                elif(len(parts)==3):
                    self.commands.wcf(parts[1],parts[2]) 
                else:
                    print(" wrong number of arguements")                
            elif parts[0]=='mv':
                if(len(parts)==3):
                    self.commands.mv(parts[1],parts[2])
                else:
                    print("wrong number of arguements")
            elif parts[0]=='cd':
                self.commands.cd(parts[1])
            elif parts[0]=='chmod':
                self.commands.chmod(parts[1])
            elif parts[0]=='history':
                history=self.history.get_commands()
               
                if(len(parts)==1):
                    for item in history:
                        print(item)
            else:
                print("bad command")
            	
				
             			
			
			

if __name__=="__main__":
    d = driver()    
    d.runShell()

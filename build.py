#!/usr/bin/env python3 

import os 
import sys 
import subprocess 

# set the stdout -> stderr 
sys.stdout = sys.stderr 

src_dir = os.path.join( os.path.dirname(os.path.realpath(__file__)) , 'src' ) 
print ( 'src_dir: ' + src_dir ) 

target = os.path.join( os.path.dirname(os.path.realpath(__file__)) , 'target' ) 
print ( 'target: ' + target ) 

all_src_files = [ os.path.join( src_dir , f ) for f in os.listdir( src_dir ) if os.path.isfile( os.path.join( src_dir , f ) ) ] 

dependencies = [
    os.path.join(os.path.expandvars('.'), 'src'), 
] 

# home directory 
home = os.path.expanduser( '~' ) 

javafx_module = os.path.join( home , 'Downloads', 'javafx-sdk-20' , 'lib' ) 
module_paths = [ javafx_module ]

modules = [ 'javafx.base', 'javafx.controls', 'javafx.fxml' ]

def main(): 
    for src_file in all_src_files: 
        print ( 'src_file: ' + src_file ) 
        # print ( 'javac -d ' + target + ' ' + src_file )
        runs = [ 'javac' , '-d' , target , src_file , '-cp' , str.join(':', dependencies), ] 
        if module_paths is not None: 
            runs += [ '--module-path' , str.join(':', module_paths) ] 
        if modules is not None: 
            runs += [ '--add-modules' , str.join(',', modules) ] 
        print ( str.join(' ', runs) ) 
        subprocess.run( runs ) 

if __name__ == '__main__': 
    main() 
    if len(sys.argv) > 1 and sys.argv[1] == 'run': 
        runs = [ 'java' , '-cp' , target , '--module-path' , str.join(':', module_paths) , '--add-modules' , str.join(',', modules) , *sys.argv[2:] ] 
        print ( str.join(' ', runs) ) 
        subprocess.run( runs )
import argparse
import os
import shutil
import glob
descStr = """ Copies all files in 'prgm_dir' to computer/turtle directorys in computercraft server directory  srv_dir
 \nEx) python puppet.py ..\..\useful_programs E:\Non-steam game installations\Minecraft\forge_server"""
parser = argparse.ArgumentParser(description=descStr)
parser.add_argument('--verbose', action='store_true', help='verbose flag' )
parser.add_argument("prgm_dir", help="computercraft program directory")
parser.add_argument("srv_dir", help="computercraft server directory")
args = parser.parse_args()


if args.verbose:
    print("Program_Directory: {}".format(args.prgm_dir))
    print("Computercraft_Directory: {}".format(args.srv_dir))

computercraft_turtle_dir = os.path.join(args.srv_dir, "world\computer")

for d in os.listdir(computercraft_turtle_dir):
    t_dir = os.path.join(computercraft_turtle_dir,d)
    if os.path.isdir(t_dir):
        t_prgm_dir = os.path.join(t_dir,"local")
        if not os.path.exists(t_prgm_dir ):
            os.makedirs(t_prgm_dir)
        
        for src_file in os.listdir(args.prgm_dir):
            full_file_name = os.path.join(args.prgm_dir, src_file)
            if (os.path.isfile(full_file_name)):
                if args.verbose:
                    print("{:50s} {:20s}".format(full_file_name,t_prgm_dir))
                shutil.copy(full_file_name, t_prgm_dir)

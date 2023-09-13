#!/usr/bin/python3
# pore-number
# prof. Marco Barbosa UnB-Brasilia
# 2020-08-14
import argparse 

parser = argparse.ArgumentParser(description="Calculate the number of pore in a 3D parallelepiped imersed in a cubic lattice, with edges of size X, Y, and Z, and with porosity LAMBDA.")
parser.add_argument("-x", help="integer size X of x-axis. By default X=10.", type=int, default=10)
parser.add_argument("-y", help="integer size Y of y-axis (optional).", type=int, default=None)
parser.add_argument("-z", help="integer size Z of z-axis (optional).", type=int, default=None)
parser.add_argument("-L", "--Lambda", help="porosity of the capsule (0,1]. (Optional) By default LAMBDA=1.0.",type=float, default=1.0)
args = parser.parse_args()

x = args.x
if args.y: 
    y = args.y
else:
    y = args.x
if args.z:
    z = args.z
else:
    z = args.x
l = args.Lambda

pore_number = int( 2*l*(x*y + y*z + x*z) )
print(pore_number)





# doom_example.py

import sys
import doom

if __name__ == '__main__':

    Tx = int(sys.argv[1])   # DM kinetic energy, MeV
    mx = int(sys.argv[2])   # DM mass, MeV
    vx = doom.vBDM(Tx,mx)   # BDM velocity
    
    print(vx)               # Print the BDM velocity
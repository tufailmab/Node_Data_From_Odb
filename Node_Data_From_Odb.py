# I built this script out of boredom to quickly extract node information
# from an Abaqus .odb file simple, but handy.
# Developer: Engr. Tufail Mabood
# WhatsApp: +923440907874

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

import os
import time
import win32com.client  # For controlling Excel
import subprocess  # For forcefully closing Excel

# Get the current working directory
current_dir = os.getcwd()

# Search for an .odb file in the current directory
odb_file = None
for file in os.listdir(current_dir):
    if file.lower().endswith(".odb"):  # Check if file is an ODB
        odb_file = os.path.join(current_dir, file)
        break  # Stop at the first found ODB file

if odb_file:
    # Open the found ODB file
    o1 = session.openOdb(name=odb_file)
    odb = session.odbs[odb_file]  # Assign the opened ODB file to odb
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)

    print "ODB file opened:", odb_file  # Python 2.7 compatible print
else:
    print "No ODB file found in:", current_dir
    exit()  # Exit script if no ODB is found

session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(CONTOURS_ON_UNDEF, ))

# Get the active model assembly
assembly = odb.rootAssembly

# File path for saving node data
node_data_path = os.path.join(current_dir, "node_data.txt")

# Open a file to save node data
with open(node_data_path, "w") as file:
    for instanceName in assembly.instances.keys():
        if instanceName.upper() == "ASSEMBLY":  # Skip the main assembly instance
            continue
        file.write("-" * 40 + "\n")  # Separator for readability
        instance = assembly.instances[instanceName]
        file.write("Instance Name: {}\n".format(instanceName))
        file.write("-" * 40 + "\n")  # Separator for readability
        file.write("Node Label\tX\tY\tZ\n")  # Header
        file.write("-" * 40 + "\n")  # Separator for readability
        
        # Loop through all nodes in the instance
        for node in instance.nodes:
            x, y, z = node.coordinates  # Get node coordinates
            file.write("{}\t{}\t{}\t{}\n".format(node.label, x, y, z))  # Save data
        
        file.write("-" * 40 + "\n")  # Separator for readability

print "Node data saved in:", node_data_path  # Python 2.7 print statement

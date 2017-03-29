# PRTG_Status_Overview
This script will allow you to get an overall status of a PRTG installation. The script returns the following informationabout the total count of sensors which are :  
- Up 
- Down
- Paused
- Undefined
- Unsual state
- Warning state
- Partially Down
- Down but acknowledged 

This script can be integrated in PRTG as a custom sensor. All you need is to use the PRTG's Python Script Advanced sensor (https://www.paessler.com/manuals/prtg/python_script_advanced_sensor). 

How to proceed ? 
- Copy this script to the folder "PRTG Network Monitor\Custom Sensors\python" of your PRTG installation
- In PRTG's web interface, go to the "Local probe" and add a Python Script Advanced sensor on the "Probe device", by clicking on "Add Sensor" button
- In the "Add Sensor" wizard you will need to choose the script from the drop-down menu
- Enter the following information in the "Additional Parameters" flied : [IP_OF_PRTG_Core_Server] [Username] [Passhash]

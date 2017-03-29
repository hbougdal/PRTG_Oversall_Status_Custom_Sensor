#********** PRTG Overall Status Custom Sensor **********#

-------------------------------------------------------------------------------------------------------------------------------
                                                    DESCRIPTION
-------------------------------------------------------------------------------------------------------------------------------

This script will allow you to get an overall status of a PRTG installation. The script returns the following information about the total count of sensors, which are in the following states :  
- Up 
- Down
- Warning
- Paused
- Partially Down
- Down but acknowledged 
- Undefined
- Unsual 

In addition to the information above, this script will also return which PRTG version are you running. 

This script can be integrated in PRTG as a custom sensor. All you need is to use the PRTG's Python Script Advanced sensor (https://www.paessler.com/manuals/prtg/python_script_advanced_sensor). 

-------------------------------------------------------------------------------------------------------------------------------
                                                   HOW TO PROCEED ? 
-------------------------------------------------------------------------------------------------------------------------------

- Copy this script to the folder "PRTG Network Monitor\Custom Sensors\python" of your PRTG installation
- In PRTG's web interface: add a Python Script Advanced sensor by clicking on "Add Sensor" button
- In the "Add Sensor" wizzard you will need to choose the script copied in (1) from the drop-down menu
- Enter the following information in the "Additional Parameters" flied : [IP_OF_PRTG_Core_Server] [Username] [Passhash]

That's it! 

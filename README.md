# ftps_protocol_files_sender

Simple script used to send files to a server via an FTPS connection. 

Use auto-py-to-exe to create a .exe file from "script.py".

The script includes an interesting file called "run.py" which, with the proper configuration, can run scripts in other versions of python using virtual environments as well.

The config.txt file contains the information for the connection and the script:

The log.txt file stores the execution logs and any errors that may arise.

The requirements.txt file contains the dependencies for the virtual environment.

The version of python used: 3.11.0

## Utils

```
py --list
py -<version>
py -3.11 pip install virtualenv
py -3.11 -m virtualenv .env
```


https://stackoverflow.com/questions/2812520/dealing-with-multiple-python-versions-and-pip

import os , traceback, platform, ftputil
from datetime import datetime
from base64 import b64decode

try:
    # Log file path
    log_file = "log.txt"

    # Log file path
    config_file = "config.txt"
    
    # Read config file
    with open(config_file, "r") as config:
        lines = config.readlines()
        host = b64decode(lines[0].strip()).decode("utf-8").split(":")[0]
        port = b64decode(lines[0].strip()).decode("utf-8").split(":")[1]
        username = b64decode(lines[1].strip()).decode("utf-8")
        password = b64decode(lines[2].strip()).decode("utf-8")
        file_pattern_01 = lines[3].strip()
        file_pattern_02 = lines[4].strip()
        folder_path = lines[5].strip()
    
    plataform_sys = platform.system()
    slash = "\\"
    if plataform_sys != "Windows":
        slash = "/"
    folder_path = folder_path.replace("\\", slash).replace("/", slash)

    # Get the list of files matching the pattern
    files = []
    
    for file in os.listdir():
        if file.startswith(file_pattern_01) and file.endswith(file_pattern_02):
            files.append(file)

    # Sort the files by date in descending order
    files.sort(reverse=True)

    # Get the most recent file
    most_recent_file = files[0] if len(files) > 0 else None

    if most_recent_file:
        # Get the date from the most recent file
        date_str = most_recent_file.split("_")[1].split(".")[0]
        date_recent = datetime.strptime(date_str, "%Y%m%d")

        # Create the FTP directory path
        ftp_directory = "{}/{}/".format(date_recent.strftime("%Y"), date_recent.strftime("%m"))

        # Establecer la conexión FTP utilizando ftputil
        with ftputil.FTPHost(host, username, password) as ftp:
            with open(log_file, "a") as log:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log.write("[{}] Loggin.\n".format(current_time))
            if not ftp.path.exists(ftp_directory):
                ftp_directory_list = ftp_directory.split("/")
                for folder in ftp_directory_list:
                    if folder:
                        ftp.mkdir(folder)
                        ftp.chdir(folder)
                ftp.chdir("..")
                ftp.chdir("..")
                with open(log_file, "a") as log:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log.write("[{}] Created directory '{}' on FTP server.\n".format(current_time, ftp_directory))
            
            # Upload the file to the FTP server
            with open(os.path.join(folder_path, most_recent_file), "rb") as file:
                ftp.upload(os.path.join(folder_path, most_recent_file), ftp.path.join(ftp_directory, most_recent_file))

        # Log critical actions to the log file
        with open(log_file, "a") as log:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write("[{}] File '{}' uploaded to '{}'.\n".format(current_time, most_recent_file, ftp_directory))

        # Delete obsolete files in the local folder
        for file in files[1:]:
            os.remove(os.path.join(folder_path, file))

        # Log critical actions to the log file
        with open(log_file, "a") as log:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write("[{}] Obsolete files deleted.\n".format(current_time))
    else:
        with open(log_file, "a") as log:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write("[{}] No file found to upload.\n".format(current_time))
except Exception as err:
    with open(log_file, "a") as log:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        traceback_text = traceback.format_exc()
        log.write("[{}] ERROR:\n\n{}\n".format(current_time, traceback_text))
    raise
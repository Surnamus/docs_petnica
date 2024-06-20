import ftplib
import time

def upload_to_ftp(filename, server, username, password, directory):
    try:
        ftp = ftplib.FTP(server, username, password)
        ftp.cwd(directory)
        with open(filename, 'rb') as file:
            ftp.storbinary(f'STOR {filename}', file)
        ftp.quit()
        print(f'Uploaded {filename} to FTP server successfully.')
    except ftplib.all_errors as e:
        print(f'FTP error: {e}')

if __name__ == '__main__':
    while True:
        filename = 'autosave.py'
        server = '192.168.0.137'
        username = 'Surnamus'
        password = 'SHA256:23/NSLNcXWFW6t3LA62iUAtv9e/2OKFBatms9OIVwf8'
        directory = 'docs_petnica'
        
        upload_to_ftp(filename, server, username, password, directory)
        time.sleep(60) 

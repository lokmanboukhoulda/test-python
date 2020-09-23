import subprocess
import os
import wget
import os.path
import smtplib, ssl

#Verify if Java exists
def check_java_exists():
    javaExists = subprocess.call(['which', 'java'])
    if javaExists == 0:
        return True
    else:
        return False

#Verify Java version
def check_java_version():
    whole_version = os.system('java -version 2>&1 | awk -F[\\\"_] \'NR==1{print $2}\'')
    print('version',whole_version)
    return whole_version

#Download Java
def download_java(url, destination):
    print('Trying to download Java...')
    wget.download(url, destination)

#Install Java
def install_java(filepath):
    if (os.path.isfile(filepath)):
        print('Installing Java...')
        subprocess.call(["sudo","dpkg", "-i", "home/lokman/Downloads/jdk-15_linux-x64_bin.deb"])
    else:
        print('Le fichier n\'existe pas')

#Send email
def send_email(): 
    status = ''
    if (check_java_version() == 0):
        status = 'Java installed'
    else:
        status = 'Java not installed'
    context = ssl.create_default_context()
    smtpGmail = 'smtp.gmail.com'
    frm = 'from@gmail.com'
    to = 'to@gmail.com'
    password = 'secret'
    message = 'Java status:',status
    server = smtplib.SMTP(smtpGmail,587)
    server.starttls()
    server.login(frm, password)
    server.sendmail(frm, to, message)
    server.quit()

if check_java_exists():
    print('Java exists')
    send_email()
else:
    check_java_version()
    url = 'https://download.oracle.com/otn-pub/java/jdk/15+36/779bf45e88a44cbd9ea6621d33e33db1/jdk-15_linux-x64_bin.deb?xd_co_f=2dd697c2605e57e2bce1595882452433'
    destination = '/home/lokman/Downloads'
    filepath = '/home/lokman/Downloads/jdk-15_linux-x64_bin.deb'
    download_java(url, destination)
    install_java(filepath)
    send_email()

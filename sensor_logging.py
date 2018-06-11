
# Author: Conan Veitch
#
# Syntax for using sensor logger:
#
# import sensor_logging as slog
# logg = slog.sensor_logger("file_name.csv")
# logg.log_values(row_array)




import csv
#import paramiko

class sensor_logger(object):

    def __init__(self, file_name):
        self.fil = file_name
        

    def log_values(self, row):
        f = open("csv_files/"+self.fil, 'a')
        self.writer = csv.writer(f, delimiter=',')
        self.writer.writerow(row)
        f.close()

    def ssh_login(self, login, password):
        #ssh = paramiko.SSHClient()
        v = 5

    def curl_values(self, data):
        y = 5

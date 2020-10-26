import os

os.system('df -k /')
Filesystem     K-blocks    Used Available Use% Mounted on
/dev/root       14846608 3247272  10945876  23% /

disk = os.statvfs('/')
(disk.f_bavail * disk.f_frsize) / 1024
10945876L

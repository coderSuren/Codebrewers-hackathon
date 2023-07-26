def convert_bytes(bytes):
   bytes = float(bytes)
   if bytes >= 1099511627776:
      terabytes = bytes / 1099511627776
      size = '%.2fTb' % terabytes
   elif bytes >= 1073741824:
      gigabytes = bytes / 1073741824
      size = '%.2fGb' % gigabytes
   elif bytes >= 1048576:
      megabytes = bytes / 1048576
      size = '%.2fMb' % megabytes
   elif bytes >= 1024:
      kilobytes = bytes / 1024
      size = '%.2fKb' % kilobytes
   else:
      size = '%.2fb' % bytes
   return size

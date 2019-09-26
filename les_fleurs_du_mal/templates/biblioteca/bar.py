import ftplib

from_ftp = ftplib.FTP("servidor1", "usuario1", "contraseña1")

to_ftp = ftplib.FTP("servidor2", "usuario2", "contraseña2")

to_ftp.cwd("/Respaldos")

to_ftp.retrlines('LIST')

from_Sock = from_ftp.transfercmd("RETR /ISEC/Paulina.zip")

to_Sock = to_ftp.transfercmd('STOR /Respaldos/ISEC/Paulina.zip')

state = 0



while 1:

   block = from_Sock.recv(4096)

   if len(block) == 0:

       break

   state += len(block)



   while len(block):

       print ("Transferidos:", state)

       sentlen = to_Sock.send(block)

       block = block[sentlen:]


from_Sock.close()

to_Sock.close()

from_ftp.quit()

to_ftp.quit()
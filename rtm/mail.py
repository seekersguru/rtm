import smtplib
fromaddr = 'info@moneymanagementindia.net'
toaddrs  = 'nishu.saxena@gmail.com'
msg = 'Hey'
username = 'moneymanagementindianet'
password = 'Adm@1234'
server = smtplib.SMTP('smtp.falconide.com:25')
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
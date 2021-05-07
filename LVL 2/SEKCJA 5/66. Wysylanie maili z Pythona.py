import smtplib

mailFrom = 'Your automation system'
mailTo = ['twojmail@gmail.com', 'twojmail2@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello

This mail confirms that processing has finished without problems,

Have a nice day!'''

message = ''' From: {}
Subject: {}

{}
'''.format(mailFrom,mailSubject,mailBody)

user = 'twojmail@gmail.com'
password = 'abcd1234'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user,mailTo,message)
    server.close()
    print('mail sent')
except:
    print('error sending mail')
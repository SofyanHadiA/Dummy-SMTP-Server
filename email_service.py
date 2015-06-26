"""Email Service"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from dummy_smtp import DummySMTP

EMAIL_SERVER = "localhost" 
EMAIL_SERVER_PORT = 25 
EMAIL_TEST_MODE = True


class EmailService(object):
    """
    Email service \n
    This service is used to handle things that related to email
    """
    def __init__(self, smtp_server=None):
        self.__smtp_server = smtp_server

    def send(self, entity_email):
        """
        This method is used to send email \n
        :param entity_email: object of EntityEmail \n
        :param is_test: True for testing mode, False for running app
        """
        msg = MIMEMultipart('alternative')
        msg['Subject'] = entity_email.subject
        msg['From'] = entity_email.sender
        msg['To'] = entity_email.receiver
        body = MIMEText(entity_email.body, 'html')
        msg.attach(body)

        s = self.__smtp_server
        if not self.__is_connected(s):
            s = smtplib.SMTP(EMAIL_SERVER, EMAIL_SERVER_PORT)
        try:
            s.sendmail(entity_email.sender, entity_email.receiver,\
                       msg.as_string())
        except smtplib.SMTPServerDisconnected:            
            raise Exception('The server unexpectedly disconnect')
        except smtplib.SMTPSenderRefused:            
            raise Exception('The sender address refused to send')
        except smtplib.SMTPRecipientsRefused:            
            raise Exception('All the recipients addresses refused')
        except smtplib.SMTPDataError:            
            raise Exception('The SMTP server refused to accept\
                    the message data')
        except Exception, err:
            raise Exception('Failed to send email. Error: {0}'
                            .format(err))
        finally:
            s.quit()

    def __is_connected(self, conn):
        """
        Check if smtp server is connected
        :param conn: SMTP connection
        :return: True if connected
        """
        try:
            status = conn.noop()[0]
        except:  # smtplib.SMTPServerDisconnected
            status = -1
        return True if status == 250 else False


class EntityEmail():
    pass

# Test Send Email
email_service = EmailService(DummySMTP())

entity_email = EntityEmail()
entity_email.subject = "Test Email"
entity_email.sender  = "me@me.com"
entity_email.receiver = "you@you.com"
entity_email.body = "The message body"

email_service.send(entity_email)
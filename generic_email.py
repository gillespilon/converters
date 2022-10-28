#! /usr/bin/env python3
"""
Generic email to multiple receivers with multiple attachments
"""

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from pathlib import Path
from os import chdir
import smtplib


def main():
    chdir(Path(__file__).parent.resolve())  # required for cron
    # Each line in the external file is the name of an attachment
    attachments_file = Path("generic_email_attachments.txt")
    # each line in the external file is an email address
    receiver_file = Path("generic_email_receivers.txt")
    # There is only one line in the external file for the subject
    subject_file = Path("generic_mail_subject.txt")
    # The file contains the email body as plain text
    body_file = Path("generic_email_body.txt")
    sender_string = "yourgmailaddress"
    password = "yourgmailpassword"
    host = "smtp.gmail.com"
    port = 465
    # Read external files
    with (
        open(
            file=receiver_file,
            mode="r"
        ) as to,
        open(
            file=subject_file,
            mode="r"
        ) as subject,
        open(
            file=attachments_file,
            mode="r"
        ) as attachments,
    ):
        receiver_list = [x.rstrip() for x in to]
        subject_string = subject.read()
        attachments_list = [x.rstrip() for x in attachments]
    # HTML body message
    email_html = body_file.open()
    email_body = email_html.read()
    email_html.close()
    msg = MIMEMultipart()
    receiver_string = ",".join(receiver_list)
    msg["To"] = receiver_string
    msg["From"] = sender_string
    msg["Subject"] = subject_string
    msg.attach(payload=MIMEText(
        _text=email_body,
        _subtype="html"
        )
    )
    # Attachments
    for attachment_file in attachments_list:
        part = MIMEBase(
            _maintype="application",
            _subtype="octet-stream"
        )
        part.set_payload(
            payload=open(
                file=attachment_file,
                mode="rb"
            ).read()
        )
        encoders.encode_base64(msg=part)
        part.add_header(
            _name="Content-Disposition",
            _value=f"attachment; filename={attachment_file}",
        )
        msg.attach(payload=part)
    # Send the email
    server = smtplib.SMTP_SSL(
        host=host,
        port=port
    )
    server.login(
        user=sender_string,
        password=password
    )
    server.sendmail(
        from_addr=sender_string,
        to_addrs=receiver_list,
        msg=msg.as_string()
    )


if __name__ == "__main__":
    main()

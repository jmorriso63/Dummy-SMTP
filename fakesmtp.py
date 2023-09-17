#!/usr/bin/env python3
"""Fake SMTP server for WebFocus"""

import asyncio
from aiosmtpd.controller import Controller

class CustomHandler:
  async def handle_DATA(self, server, session, envelope):
    peer = session.peer
    mail = open("mails/"+str(time.time())+"eml",w)
    print("New mail from " + envelope.mail_from)
    mail.write(envelope.mail_from)
    mail.write(envelope.rcpts_tos)
    mail.write(envelope.content)
    mail.close()
    if error_occured:
      return '500 Could not process your message'
    return '250 OK'

if __name__ == '__main__':
  handler = CustomHandler()
  controller = Controller(handler, hostname='127.0.0.1', port=10025)
  controller.start()
  input('SMTP server running. Press Return to stop server and exit.')
  controller.stop()

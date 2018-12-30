import re


class EmailHandler(object):
    """an interface for handling mails"""

    def __init__(self, successor=None):
        self._successor = successor

    def handle_mail(self, subject, mail):
        print('HANDLE_REQUEST IN BASE CLASS ')
        pass


class SpamHandler(EmailHandler):
    """Handle spam, otherwise forward it to the successor."""

    def handle_mail(self, subject, mail):
        print("SpamHandler handle_mail")
        if re.search('buy', subject, re.IGNORECASE):
            print('move mail to spam folder')
        elif self._successor is not None:
            print("pass to other handler")
            self._successor.handle_mail(subject, mail)


class ForumHandler(EmailHandler):
    """Handles emails from forum"""

    def handle_mail(self, subject, mail):
        if re.search('forum', subject, re.IGNORECASE):
            print('move mail to forum folder')
        elif self._successor is not None:
            print("pass to other handler")
            self._successor.handle_mail(subject, mail)


class CustomerHandler(EmailHandler):
    """Handles emails from customers"""

    def handle_mail(self, subject, mail):
        if re.search('customer', subject, re.IGNORECASE):
            print('CustomersHandler handle_mail')
        elif self._successor is not None:
            print("pass to other handler")
            self._successor.handle_mail(subject, mail)


def main():
    forum_handler = ForumHandler()
    spam_handler = SpamHandler(forum_handler)
    customer_handler = CustomerHandler(spam_handler)

    customer_handler.handle_mail('Problem on production server', 'Customer has issue with...')


if __name__ == "__main__":
    main()

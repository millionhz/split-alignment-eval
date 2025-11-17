from sendmail import sendmail
import json
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send test emails to recipients.')
    parser.add_argument('cat', type=str, help='Key to select email configuration (e.g., dmarc-passing)')
    parser.add_argument('service', type=str, help='Email service to send to (e.g., gmail) (you need to configure these in code first)')
    parser.add_argument('type', type=str, help='Type of email (e.g., apex, subdomain)')
    args = parser.parse_args()

    # read config
    with open('email-configs.json', 'r') as file:
        email_configs = json.load(file)

    # email services
    services  = {
        "gmail": "address@gmail.com",
        "outlook": "address@outlook.com",
        "protonmail": "address@proton.me",
        "yandex": "address@yandex.com",
        "yahoo": "address@yahoo.com",
        "aol": "address@aol.com",
        "naver": "address@naver.com",
        "tutamail": "address@tutamail.com",
        "op.pl": "address@op.pl",
        "mailo": "address@mailo.com",
        "mail.com": "address@mail.com",
        "inbox.lv": "address@inbox.lv",
        "sapo.pt": "address@sapo.pt",
        "seznam.cz": "address@seznam.cz",
        "zohomail": "address@zohomail.com",
    }

    config = email_configs[args.cat][args.type]

    recipient = services[args.service]

    if config['dkim']:
        with open(config['dkim']['private_key'], 'r') as file:
            privkey = file.read()

        dkim_conf = {
            'privkey': privkey,
            'selector': config['dkim']['selector'],
            'domain': config['dkim']['domain']
        }
    else:
        dkim_conf = None

    mail_from = config['mailfrom']
    subject = config['subject']
    from_ = config['from']

    body = config['body']

    tls = True
    if '@aol.com' in recipient or '@yahoo.com' in recipient or '@zohomail.com' in recipient:
            tls = False

    sendmail(sender=from_,
             recipient=recipient,
             tls=tls,
             mail_from=mail_from,
             subject=subject,
             body=body,
             dkim_conf=dkim_conf
    )

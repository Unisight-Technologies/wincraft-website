from django.core.mail import send_mail


def sendMailToUser(name, send_to):
    subject = "Regarding query sent on Wincraft Buildmat's Website"
    message = "Hello "+name+"! \n\nWe have successfully received your query.\nWe are glad that you tried to connect with us.\n\nWe will get back to you as soon as possible.\n\nRegards\n-Team Wincraft Buildmat"
    send_mail(
        subject,
        message,
        'teamurbaninsight@gmail.com',
        [send_to],
        fail_silently = False,
    )

def sendMailToWincraft(name, email, phone, query):
    message = "The following query has been received on our website:\n\nName: "+name+"\nEmail Id: "+email+"\nPhone Number: "+phone+"\nQuery: "+query+"\n\nRegards"
    subject = "A query has been received on Wincraft Buildmat"
    send_mail(
        subject,
        message,
        'teamurbaninsight@gmail.com',
        ['wincraftbuildmat@gmail.com'],
        fail_silently = False,

    )

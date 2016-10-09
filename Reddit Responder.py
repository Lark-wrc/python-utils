import re
import time
import urllib
import sys

recenturl = ""
oldrecenturl = ""
recenttime = 0

def checkAndGet():
    global recenturl
    global recenttime
    global oldrecenturl
    grab = 0
    store = 1
    updates = 0

    urllib.urlretrieve(recenturl, "test.html")
    f = open("test.html", 'r')

    for x in range(0,4): f.readline()
    if f.readline() == "    <title>Too Many Requests</title>\n":
        print "Too many Requests error, holding."
        f.close()
        time.sleep(3)
        return checkAndGet()
    f.seek(0,0)


    # <div class="md"><p>.*</p> # message text.
    for line in f:
        if grab:
            if store:
                oldrecenturl = recenturl
                store = 0

            post_url = re.search("""a href="(.*?)" """, line)
            if post_url and re.search("""reddit.com/r/""", post_url.string):
                grab = 0
                post_url = post_url.group(1)
                # print post_url
                recenturl = post_url

        post_string = re.search("""<time title="(.*?)" """, line)
        if post_string:
            post_time = post_string.group(1)
            # print post_time
            raw_time = time.mktime(time.strptime(post_time, "%a %b %d %X %Y %Z"))

            content_string = re.search("""<div class="md"><p>(.*)</p>""", line)
            if content_string:
                # print content_string.group(1)
                comment = content_string.group(1)[0] == '(' and content_string.group(1)[-1] == ')'

            if raw_time > recenttime and not comment:
                grab = 1 # Take the url of this comment on the next line of the html (weird formatting)
                updates += 1
                recenttime = raw_time
    return recenturl, updates


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail\n'
    except:
        print "failed to send mail\n"


def display(url, updates):
    print "Run Complete."
    if updates == 0:
        print "No changes."
    else:
        print "There were", updates, "updates. New url:"
        print url


def notify(result):
    if result[1] > 0:
        send_email('pawkun14', 'wheretheresawilltheresaway', 'willowlark@outlook.com',
                'Reddit Updater', 'There are %s updates at \n %s!' % (result[1], oldrecenturl))


def loop(thread):
    global recenturl
    recenturl = thread
    while(1):
        result = checkAndGet()
        display(*result)
        notify(result)
        time.sleep(60*5)

if __name__ == "__main__":
    # result = checkAndGet(recenturl, recenttime)
    # display(*result)
    # send_email('pawkun14', 'wheretheresawilltheresaway', 'willowlark@outlook.com',
    #         'Reddit Updater', 'There are %s updates at \n %s!' % (result[1], result[0]))
    loop(sys.argv[1])
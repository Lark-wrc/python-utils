#! /usr/bin/python

import cgi
import shorthand_bb
import markdown_BB

form = cgi.FieldStorage()

if "text" in form: text = form.getvalue("text")
else: text = None

print "Content-type:text/html"
print ""
print """
<head><link rel="shortcut icon" href="BBfavi.jpg" /></head>
<body style="background-color:black;">
<div style="margin: auto; width: 60%;text-align:center">
<h1 style="color:white;">BBcode from Custom Markdown<h1>

<textarea wrap="soft" form="input" name="text" rows="15" cols="80"
placeholder="Template:
How to do things:
**Bold**
_underline_
*italics*
&&c centered &&c
--- Horizontal rule
&_ Colored text& Where _ is one of these letters:
c,s,r,v,a,w & b, p, u, n
"></textarea>

<br /><br />

<form action="./BBcode.cgi" method="post" id="input">
<input type="submit" value="Submit" />
</form>

</div>

<div style="background-color:lightgrey;margin: auto; width:
50%;text-align:center;">
<a href="bbify.txt">Text file source</a><pre>"""


if text:
    lines = text.split("\r\n")
    #print lines
    try:
        exit = markdown_BB.convert(lines)
        if exit == 0: print """<iframe src="bbify.txt" width="400px"
height="470px"></iframe>"""
    except:
        print """<h1>Error Occurred. Check syntax?</p>"""
else: print """<h1>Put in some text...?</p>"""


print "<br /><br /></pre></div></body>"

#! /usr/bin/python

import cgi
import shorthand_bb

form = cgi.FieldStorage()

if "text" in form: text = form.getvalue("text")
else: text = None

print "Content-type:text/html"
print ""
print """
<body style="background-color:black;">
<div style="margin: auto; width: 60%;text-align:center">

<textarea wrap="hard" form="input" name="text" rows="15" cols="80"
placeholder="Template:
*bold text*
_underlined text_
^italic text^
*^_this can be combined, though keep them in order_^*
#sPrints Sona's text color.# <- note that it's only a single # to close!
#cPrints Sherwood,# #aPrints ASPN,# #vPrints VLPS,# and #wPrints white#
    indents with tabs
        are
    preserved.
            useful for
    1. lists
    2. more lists
"></textarea>

<br /><br />

<form action="./BBcode.cgi" method="post" id="input">
<input type="submit" value="Submit" />
</form>

</div>

<br />

<div style="background-color:lightgrey;margin: auto; width: 50%;text-align:center;">
<a href="bbify.txt">Text file source</a><pre>"""


lines = text.split("\r\n")
print lines
shorthand_bb.convert(lines)
print """<iframe src="bbify.txt" width="400px" height="500px">
    </iframe>"""

"""if text:
    lines = text.split('\n')
    shorthand_bb.convert(lines)
    f = open('bbify.txt')
    for line in f:
        print line
        #print "<br />"
"""

print "<br /><br /></pre></div></body>"

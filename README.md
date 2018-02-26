# Utilities

A bunch of scripts I used/use here or there.

## File Namers

I use these scripts to clean up file names from funky looking downloads. The kind that have [download.com]A file(thanks for {everything} 0x1).txt as a format.

* **Subfixer** is the first implementation of it. Subtitled files is where the name comes from. I... don't use this one anymore. I have no idea if it still/ever worked.

* **Renamer** I use frequently. Cute little batch script to run it on new downloads in a particular folder. Stable.

## MDasBB

I play by post on a forum that used BBcode. Typing BBcode is infernally annoying. Further, if I draft something offline I either have to A) format it twice, once for rich text and once for the BBcode; or B) look at raw BBcode in my editor. These are both dumb. I started writing in Markdown offline, and the scripts here are for converting that markdown into BBcode. It's not 100% compatible with markdown or BBcode, but it does what I need it to.

+ **word_scan** was the first draft. Cannot explain why I decided to parse each word in the string for markdown tags individually as opposed to regex. It was 3am and I was hopped up on a pot of coffee. Worked fine with a pseudo markdown format, but I retired it because it's implementation was just *bad*.

+ **regex_scan** is based on word_scan's control structure (which makes it less than perfect, but who needs snowflake code anyway) but uses Regex. Easier to expand on. Also adheres to github markdown, cause it's glorious.

+ **BBcode.cgi** is a cgi that takes input on a browser, runs it through regex_scan, and displays the result. Simple utility to /use/ the prior script.

## Simple Crypto

Exactly what it says on the tin. Very old testing scripts I did that encode or decode strings using some basic crypto. Shift cipher stuff.

+ **Encoder** can do either a ceasar cipher or entean, which is a fictional alternate alphabet.

+ **Decoder** only takes entean script and converts it back to english.

+ **Team Gen** doesn't actually encrypt anything. It's a permutation generator from RWBY team names, taking custom initials and spitting out team names to try. Unfortunately it can't do the work to figure out what the name can stand form. 

## search

Contains utilities for searching things. Includes a recursive glob file system search that returns file paths relative to calling folder.
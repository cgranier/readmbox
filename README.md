# readmbox #

readmbox exists simply so I can import emails from an mbox file into a csv file.

## Why? ##

Because YouTube sends emails regarding copyright claims and blocked videos against our content. These emails are very hard to interact with and keep track of which claims we have disputed, etc.

I tried several services that claim to parse emails and process them but Zapier was unable to manage attachments (and I had to deal with 3,000 previously received messages) and Mailparser has a bug where it will ignore a few attachments (between two and five in our tests) but will not let you know which attachments were ignored. It would probably take me a few days to properly forward, process and double-check all the messages.

## How did I solve it? ##

Python and Regular Expressions.

Using Google Takeout, I downloaded a copy of all the _claim_ emails and all the _blocked_ emails (labeled using a filter in GMail). The download comes in a standar mbox file, which you can read with Python's mailbox library.

A few visits to [Stack Overflow](https://stackoverflow.com/a/31489271/469449) and [RegExr](https://regexr.com/) later and I had a working prototype in a Jupyter Notebook.

## How long did it take me? ##

About an afternoon.

## Libraries used: ###

```python
import mailbox
import re
import csv
```

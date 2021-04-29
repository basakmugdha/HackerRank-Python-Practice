# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

n = int(input())
html = ""
for _ in range(n):
    html = html + input()

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for att in attrs:
            print ("-> "+att[0]+" > "+att[1])
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for att in attrs:
            print ("-> "+att[0]+" > "+att[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(html)

from twython import Twython

##connect to twitter
from auth import(
                 consumer_key,
                 consumer_secret,
                 access_token,
                 access_token_secret
                 )
twitter = Twython(
                  consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret
                  )


from lxml import html
import requests


page = requests.get('https://www.poetryfoundation.org/poems/poem-of-the-day')
tree = html.fromstring(page.content)

#This will create a list of buyers:
#poem = tree.xpath('//id[@text=""]/text()')
#poem = tree.xpath('//div[@class="o-poem"]/text()')
#line1 = tree.xpath('//div[@style="text-indent: -1em; padding-left: 1em;"]/text()[1]')


line1 = tree.xpath('//div[1][@style=\"text-indent: -1em; padding-left: 1em;"]/text()')
#line2 = tree.xpath('//div[2][@style=\"text-indent: -1em; padding-left: 1em;"]/text()')
#line3 = tree.xpath('//div[3][@style=\"text-indent: -1em; padding-left: 1em;"]/text()')

#author = tree.xpath('//span[@class="c-txt c-txt_attribution"]/text()')

authorPath = tree.xpath('//a[starts-with(@href, "https://www.poetryfoundation.org/poets/")]/text()')
author = authorPath[0]
##message = line1.append(" -".format(''.join(author)))

message = line1;

#print(line1)
#print(author)
twitter.update_status(status=message)
print("Tweeted: %s" % message)





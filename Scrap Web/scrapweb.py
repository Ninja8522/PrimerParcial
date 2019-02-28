#!/usr/bin/env python

import requests
import lxml.html

html = requests.get ("https://store.steampowered.com/explore/new/")

doc = lxml.html.fromstring(html.content)

newReleases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

print(newReleases)

titles = newReleases.xpath('.//div[@class="tab_item_name"]/text()')

print(titles)

prices = newReleases.xpath('.//div[@class="discount_final_price"]/text()')

print(prices)

tags = newReleases.xpath('.//div[@class="tab_item_top_tags"]')

totalTags = []

for tag in tags:
    totalTags.append(tag.text_content())

print(totalTags)

totalTags = [tag.split(', ') for tag in totalTags]

print(totalTags)

platformsdiv = newReleases.xpath('.//div[@class="tab_item_details"]')

totalPlatforms = []

for game in platformsdiv:
    namePlatform = game.xpath('//span[Contains(@class="platform_img")]')
    platforms = [t.get("class").split(' ')[-1] for t in namePlatform]
    if "had_separator" in platforms:
        platforms.remove('had_separator')
    totalPlatforms.append(platforms)

print(totalPlatforms)
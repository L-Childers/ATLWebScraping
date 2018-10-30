from scrapy import Spider, Request
from abovethelaw.items import AbovethelawItem
import re

class AbovetheLawSpider(Spider):
    name = "abovethelaw_spider"
    allowed_urls = ['https://abovethelaw.com/']
    start_urls = ['https://abovethelaw.com/biglaw/']

    def parse(self, response):
        # Number of pages to scrape (chose 200 initially)
        num_pages=200
        # Creating URLs for set number of pages to scrape
        result_urls = ['https://abovethelaw.com/biglaw/page/{}/?rf=1'.format(i) for i in range(1, num_pages)]

        for url in result_urls:
            yield Request(url=url,callback=self.parse_topic_page)

    def parse_topic_page(self, response):
        # Extract URLs for individual articles
        article_urls=response.xpath('//ul[@class="newslist"]//p[@class="title"]/a/@href').extract()

        for url in article_urls:
            yield Request(url=url, callback=self.parse_article_page)

    def parse_article_page(self, response):
        # Extract data for anlysis
        # Extract Title
        title=response.xpath('//h1[@class="post-title"]/a/text()').extract_first().strip()
        # Extract Subtitle (text beneath title)
        sub_title=response.xpath('//h2[@class="post-sub-title"]/text()').extract_first().strip()
        # Extract author name
        author=response.xpath('//p[@class="postAuthor byline"]/a/text()').extract_first().strip()
        # Extract date articlew as published
        publish_date=response.xpath('//div[@class="meta"]/text()').extract_first()
        publish_date=''.join(c for c in publish_date if c not in '\t\n')
        publish_date=re.findall('\w+\s\d+\,\s\d{4}', publish_date)
        # Extract article content (body)
        summary=response.xpath('//div[@class="entry"]/div[@class="content"]/p/text()').extract()
        summary=''.join(c for c in summary if c not in '\r\t\n')
        # Extract tags (theme of article)
        tags=response.xpath('//div[@class="postTags meta"]/p/a/text()').extract()

        item = AbovethelawItem()
        item['title']=title
        item['sub_title']=sub_title
        item['author']=author
        item['publish_date']=publish_date
        item['summary']=summary
        item['tags']=tags

        yield item

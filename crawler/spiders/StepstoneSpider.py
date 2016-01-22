from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from crawler.items import VacancyItem
from scrapy.http import Request

class StepstoneSpider(BaseSpider):
    name = "stepstone_crawler"
    allowed_domains = ["www.stepstone.se"]
    url = "http://www.stepstone.se/lediga-jobb-i-hela-sverige/data-it/sida{0}/"

    def start_requests(self):
        first_url = self.url.format(1)

        req = Request(url=first_url, callback=self.parse)
        req.meta['numberOfPage'] = 1
        return [req]

    def parse(self, response):
        num = response.meta['numberOfPage']
        articles_html = response.css('article')

        print(articles_html)
        for vacancy in articles_html:
            item = VacancyItem()

            item['image_path'] = vacancy.xpath('.//div[@class="logo"]//img/@src').extract()[0]
            item['title'] = vacancy.xpath('.//div[@class="description"]/h5/a/text()').extract()[0]
            item['place'] = vacancy.xpath('.//div[@class="description"]//span[@class="subtitle"]/span[2]/text()').extract()[0]
            item['company_name'] = vacancy.xpath('.//div[@class="description"]/span/a/text()').extract()[0]
            yield item

        if len(articles_html) == 0:
            yield None
        else:
            req = Request(url=self.url.format(num+1), callback=self.parse)
            req.meta['numberOfPage'] = num+1
            yield req
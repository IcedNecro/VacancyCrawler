from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from crawler.items import VacancyItem
from scrapy.http import Request

class MonsterSpider(BaseSpider):
    name = "monster_crawler"
    allowed_domains = ["jobb.monster.se"]
    url = "http://jobb.monster.se/browse/Data-IT_4?pg={0}&sf=15.660"

    def start_requests(self):
        first_url = self.url.format(1)

        req = Request(url=first_url, callback=self.parse)
        req.meta['numberOfPage'] = 1
        return [req]

    def parse(self, response):
        num = response.meta['numberOfPage']
        articles_html = response.xpath('//table[@class="listingsTable"]//tr[contains(@class,"odd") or contains(@class,"even")]')
        
        def check_for_existence(v):
            return '' if len(v)==0 else v.extract()[0]

        for vacancy in articles_html:
            item = VacancyItem()

            item['image_path'] = check_for_existence(vacancy.xpath('.//td[3]//a[@class="companyLogo"]/img/@src'))
            item['place'] = check_for_existence(vacancy.xpath('.//td[3]//*[@class="jobLocationSingleLine"]/a/text()'))
            item['title'] = check_for_existence(vacancy.xpath('.//td[2]//*[@class="jobTitleContainer"]/a/text()'))
            item['company_name'] =  check_for_existence(vacancy.xpath('.//td[2]//*[@class="companyContainer"]/div/a[2]/text()'))

            yield item

        next_button =  response.xpath('//div[@class="navigationBar"]/a[contains(@class, "nextLink")]')

        if len(next_button) == 0:
            yield None
        else:
            req = Request(url=self.url.format(num+1), callback=self.parse)
            req.meta['numberOfPage'] = num+1
            yield req

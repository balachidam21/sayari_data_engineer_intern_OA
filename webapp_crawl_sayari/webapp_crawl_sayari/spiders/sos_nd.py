import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request, FormRequest
import json


class SosNdSpider(CrawlSpider):
    name = 'sos_nd'
    allowed_domains = ['firststop.sos.nd.gov']
    

    def start_requests(self):
        url = 'https://firststop.sos.nd.gov/api/Records/businesssearch'
        searchData = {"SEARCH_VALUE":"X","STARTS_WITH_YN":"true","ACTIVE_ONLY_YN":"true"}
        yield scrapy.Request(url,  callback=self.parse_item,
                      method='POST',
                      body=json.dumps(searchData),
                      headers={'Content-Type':'application/json'} )

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        res = json.loads(response.body)
        rows = res.get("rows")
        for key, value in rows.items():
            source_id = int(key)
            business_url = 'https://firststop.sos.nd.gov/api/FilingDetail/business/{}/false'.format(source_id)
            yield scrapy.Request(business_url, callback=self.parse_business,
                                 meta = {'source_id': key},
                                 method='GET',
                                 headers={'accept':'*/*','authorization':'undefined'})
        yield {
            "template" : res.get("template"),
            "rows" : res.get("rows")
        }
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
    def parse_business(self, response):
        source_id = response.meta.get('source_id')
        # print(source_id)
        res = json.loads(response.body)
        yield {
            source_id: res.get("DRAWER_DETAIL_LIST")
        }

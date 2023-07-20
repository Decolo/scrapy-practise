from pathlib import Path

import scrapy

class XueqiuSpider(scrapy.Spider):
    name = "xueqiu"

    def start_requests(self):
        urls = [
          "https://xueqiu.com/hq",
        ]

        for url in urls:
          yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       page = response.url.split("/")[-2]
       filename = f"xueqiu-${page}.html"
      #  filename = f"quotes-${page}.html"
       Path(filename).write_bytes(response.body)

       self.log(f"file saved: {filename}")
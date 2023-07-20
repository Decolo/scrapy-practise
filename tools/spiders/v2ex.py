from pathlib import Path

import scrapy

class V2exSpider(scrapy.Spider):
    name="v2ex"
    
    start_urls = [
        "https://www.v2ex.com/?tab=tech",
        "https://www.v2ex.com/?tab=creative",
        "https://www.v2ex.com/?tab=jobs"
    ]
    
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
    
    def parse(self, response):
        # domain = response.url.split("/")[-2]
        
        # sub_hrefs = []
        
        info = {
            "title": "",
            "count_livid": ""
        }
        
        for info in response.css("div.cell.item"):
            _item = info.css(".topic-link")
            _href = _item.css("::attr(href)").get()
            
            
            title = _item.css("::text").get()
            count_livid = info.css(".count_livid::text").get()
            # info["title"] = title
            # info["count_livid"] = count_livid
            
            if (_href):
                print(f"**${_href}**")
                yield response.follow(_href, self.parse_content, cb_kwargs={
                    "title": title,
                    "count_livid": count_livid
                })
            
            
            
        
        
            
    def parse_content(self, response, title, count_livid):
        content = response.css(".topic_content")
        links = content.css("a::text").getall()
        texts = content.css("p::text").getall()
        
        print({
            "title": title,
            "count_livid": count_livid,
            "content": ",".join(links + texts)
        })
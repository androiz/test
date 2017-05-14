import scrapy
import itertools

import knowledge


class SinonimosSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://www.diccionariodesinonimos.es/']

    def parse(self, response):
        blocks = []
        letters = response.xpath('/html/body/div[1]/table/tr//a')
        for letter in letters:
            url = letter.css('::attr(href)').extract_first()
            blocks.append(url)

        for block in blocks:
            request = scrapy.Request(response.urljoin(block), callback=self.get_word)
            yield request

    def get_word(self, response):
        links = []
        words = response.xpath('/html/body/table[1]/tr/td/a')
        for word in words:
            w = {
                'word': word.css('::text').extract_first(),
                'url': word.css('::attr(href)').extract_first()
            }
            links.append(w)

        for link in links:
            request = scrapy.Request(response.urljoin(link['url']), callback=self.get_sinonimo)
            request.meta['word'] = link['word']
            request.meta['font'] = response.url
            yield request

    def get_sinonimo(self, response):
        if response.url not in self.start_urls:
            keyword = response.xpath('/html/body/table[2]/tr[3]/td[2]/strong')
            if keyword:
                word = keyword.css('::text').extract_first()
                sinonimos_path = response.xpath('/html/body/table[2]/tr/td[2]/strong')
                sinonimos = sinonimos_path.css('::text').extract()
            else:
                word = response.meta['word']
                sinonimos_path = response.xpath('/html/body/ul/li')
                sinonimos_list = sinonimos_path.css('::text').extract()
                sinonimos = list(itertools.chain.from_iterable(
                    [sinonimo
                         .replace("\t", "")
                         .replace("\n", "")
                         .replace("\r", "")
                         .replace(" ", "")
                         .split(",") for sinonimo in sinonimos_list])
                )
                sinonimos = [sinonimo for sinonimo in sinonimos if sinonimo]

            word_dict = {
                'word': word,
                'url': response.url,
                'font': response.meta['font'],
                'sinonimos': ','.join(sinonimos)
            }

            knowledge.Knowledge().insert_synonymous(word_dict)

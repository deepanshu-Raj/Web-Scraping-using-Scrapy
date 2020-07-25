import scrapy

class AlgoScrape(scrapy.Spider):
    
    name = "algo_spider"
    
    def start_requests(self):
        urls = ["https://cp-algorithms.com/data_structures/segment_tree.html"]
        
        for url in urls:
            yield scrapy.Request(url = url,callback = self.parse)
            
    def parse(self,response):
        
        for head1 in response.css('h1'):
            yield {
                "head1" : head1.get()
    	       }
        	
        for head2 in response.css('h2'):
            yield {
    		  "head2" : head2.get()
    	   }
     	    
        for head3 in response.css('h3'):
            yield {
                "head3" : head3.get()
            }

        	
        for para in response.css('p::text'):

         		yield {
     			"Paragraph" : para.get()
            	}
        	
        self.log("Success!!")


        
        
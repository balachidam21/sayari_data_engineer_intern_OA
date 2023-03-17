# Sayari Data Task


### Task
The Secretary of State of North Dakota provides a business search [web app](https://firststop.sos.nd.gov/search/business) that allows users to search for businesses by name. 
Your task:
1. Play around with the site and figure out how to query companies by name.
    - Hint: Your browser's dev tools are good for this.
2. Download information for all active companies whose names start with the letter **"X"** (e.g., **X**treme Xteriors LLC) including their **Commercial Registered Agent**, **Registered Agent**, and/or **Owners**. Save the crawled data in the file format of your choice.
   - Hint: [scrapy](https://github.com/scrapy/scrapy) is a suitable web-crawling framework.
3. Create and plot a [graph](https://en.wikipedia.org/wiki/Graph_theory) of the companies, registered agents, and owners.
   - Hint: [NetworkX](https://networkx.github.io/documentation/stable/index.html) is a suitable graph library that plays nice with [matplotlib](https://matplotlib.org/).
   - Hint: You may consider names as sufficiently unique to identify each node in the graph.
   - Hint: An example plot output is included below.


### Work Done
1. The APIs that were used by the website was found using Network tab in Browser's Dev Tools. Two APIs are being used for business search and business details respectively.
2. The respective APIs were crawled using a spider from Scrapy Library. The crawled data is stored at [businesssearch.json](./webapp_crawl_sayari/businesssearch.json).
3. Based on the crawled data obtained from 2, 
    * We were able to construct a graph with Entity Linking which connects company names with their entities Commercial Registered Agent, Registered Agent, Owners respectively.
    * The Network is a Connected Components SubGraph which visualizes companies with common entities. The graph can be found [here](connected.png).
    
    **Note:** The Node labels have been removed from the graph for the sake of good visualization. The labels can be added by changing the `with_labels` parameter in `networkx.draw()` function.





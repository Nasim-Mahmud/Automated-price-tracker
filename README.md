# Automated-price-tracker
A simplistic price tracker program that will monitor a certain product's price on ex: Amazon.com in order to find the best time to a purchase. This project is an outcome of Angela Yu's <a href="https://www.udemy.com/course/100-days-of-code/">100 Days of Code</a>.

Find the url of the product you want to purchase. Get the headers of your browser from the <a href="http://myhttpheader.com/">My Headers </a> website, it is necessary because when your browser search a product online, it also passes some info about your browser. We also have to pass those info via headers.

Now, we need to make soup using BeautifulSoup module and for that, we need to use <b>"lxml"</b> parser instead of <b>"html.parser"</b>. Find the price using soup and the rest logic is simple as that.

:)

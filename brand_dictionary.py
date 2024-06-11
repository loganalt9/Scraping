#Use this for key words so we can have a universal scraper
#Not sure if there is a better method but writing this while searching for other possible implementations
#Also not sure that Nike is correct yet need to write the 'universal scraper' in order to test fuctionality

parsing_keywords = {
    'Nike': {
        'dynamic': True,
        'url': 'https://www.nike.com/w/mens-clothing-6ymx6znik1',
        'finder': 'product-card__body',
        'name': 'product-card__title',
        'price': 'product-price',
        'image': 'product-card__hero-image'
    },
    'H&M': {
        'dynamic': False,
        'url': 'https://www2.hm.com/men/products/view-all.html?productTypes=Vest,Top,T-shirt,Shorts,Shirt,Jeans,Jacket',
        'finder': 'article',
        'name': 'link',
        'price': 'price regular',
        'image': 'item-image',
    }
} 

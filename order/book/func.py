"""This fille is function file """
def get_asin_isbn(url):
    """It is a function to get ASIN or ISBN from Amazon URL
       Returns: ASIN or ISBN
    """
    asin_index = url.find('/dp/')
    isbn_index = url.find('/product/')
    if asin_index > 0:
        asin = url[asin_index+4:asin_index+14]

        return asin

    elif isbn_index > 0:
        isbn = url[isbn_index+9:isbn_index+19]
        return isbn
    else:
        raise Exception('This url can\'t use')

def get_image_url(asin_or_isbn):
    """It is a function to obtain the URL of image of product from asin or isbn.
       Returns: ImageUrl
    """
    return 'http://images-jp.amazon.com/images/P/{}.09.LZZZZZZZ.jpg'.format(asin_or_isbn)

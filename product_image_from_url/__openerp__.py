# -*- coding: utf-8 -*-
{
    'name': "Import Product Images From URL",
    'summary': """
        Get product images from url""",
    'description': """
        This module offers a way to import product images from urls.
		Simply import the url of the product image in the Image Url field.
        Then select the images and download images. This supports batch processing.
    """,
    'author': "Explore Data Systems",
    'website': "http://www.exploredatasystems.com",
    'category': 'Extra Tools',
    #Change the version every release for apps.
    'version': '0.1',
	#the cost of the module in EUR
	'price' : 20,
	'currency': 'EUR',
    # any module necessary for this one to work correctly
    'depends': [
        'product',
    ],
    # always loaded
    'data': [
        'views/product_view.xml',
		'views/product_actions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    # only loaded in test
    'test': [
    ],
}

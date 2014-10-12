WTF_CSRF_ENABLED = True #activates cross-site request forgery prevention
SECRET_KEY = 'something-goes-here' #needed when csrf is enabled, token that is used to validate form

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/08/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

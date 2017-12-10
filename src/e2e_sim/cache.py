"""
    Web Cache
"""


import pickle
import sys


class Site:
    def __init__(self, sitename, content, latency):
        """
            Create a site instance
        """
        self.sitename = sitename
        self.content = content
        self.latency = latency

class Cache:
    def __init__(self, cachefile=None):
        """
            Initialize the internal cache dictionary
        """
        self.cache = dict()
        if cachefile:
            try:
                with open(cachefile, 'rb') as cf:
                    saved_sites = pickle.load(cf)
                    for sitename, popularity, latency, content  in saved_sites:
                        if content is None: continue
                        self.cache_site(sitename, content, latency)
            except Exception as e:
                print('Failed to open cachefile "{}": {}'.format(cachefile, e), file=sys.stderr)

    def get_site(self, sitename):
        """
            If site is cached return the cached sitem otherwise return None
        """
        return self.cache.get(sitename)

    def cache_site(self, sitename, content, latency):
        """
            Cache a site in the internal cache dictionary
        """
        
        site = Site(sitename, content, latency)
        self.cache[sitename] = site
        return site
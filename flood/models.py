from __future__ import division
__author__ = 'Daan Debie'


class Torrent(object):

    def __init(self, name=None, magnet_link=None, torrent_link=None, seeders=0, leechers=0):
        self.name = name
        self.magnet_link = magnet_link
        self.torrent_link = torrent_link
        self.seeders = seeders
        self.leechers = leechers

    @property
    def ratio(self):
        return self.seeders / self.leechers if self.leechers != 0 else float('inf')

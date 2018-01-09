# -*- coding:utf-8 -*-
class AnotherMiddleware(object):
    def process_response(self, request):
        print "Another middleware executed"
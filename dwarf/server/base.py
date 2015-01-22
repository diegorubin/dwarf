# coding: utf-8

import sys
import cyclone.web
import ast

from os.path import join, abspath, dirname
apipath = abspath(join(dirname(__file__), ".."))
sys.path.append(apipath)

from dwarf.link.base import *


class SpaHandler(cyclone.web.RequestHandler):
    def get(self):

        static_path = abspath(join(dirname(__file__), "..", "..", "webresources"))
        f = open(static_path + "/index.html")

        self.write(f.read())

class AllLinksHandler(cyclone.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")

        try:
            documents = all_documents()
            arr_documents = []

            for doc in documents:
                arr_documents.append(doc.to_json())

            self.write({'status' : '200',
                        'documents' : str(arr_documents)})

        except:
            self.write({'status':'500',
                        'documents':[]})

    def post(self):
        self.set_header("Content-Type", "application/json")

        try:
            document = ast.literal_eval(self.request.body)

            d = Document()
            d.__dict__ = document
            d.save()

            self.write({'status' : '200',
                        'id' : str(d._id)})

        except:
            self.write({'status': '500',
                        'erro' : 'documento não pode ser salvo'})

class Application(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/", SpaHandler),
            (r"/links", AllLinksHandler)
        ]

        static_path = os.path.join(os.path.dirname(__file__), "static")
        settings = dict(
            static_path = os.path.join(os.path.dirname(__file__), "static")
        )

        print static_path
        print settings

        cyclone.web.Application.__init__(self, handlers, **settings)



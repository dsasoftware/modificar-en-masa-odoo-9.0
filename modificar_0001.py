import os
import csv
import xmlrpclib
import re


HOST='190.114.253.252'
PORT=8069
DB='db'
USER='falconsoft.3d@gmail.com'
PASS='1234567890'
url ='http://%s:%d/xmlrpc/' % (HOST,PORT)

common_proxy = xmlrpclib.ServerProxy(url+'common')
object_proxy = xmlrpclib.ServerProxy(url+'object')
uid = common_proxy.login(DB,USER,PASS)

def _update_mass(estado):
    if estado is True:
        cont = 1

        product = object_proxy.execute(DB,uid,PASS,'product.template','search',[('active','=',True)])


        for id in product:
            do_write = object_proxy.execute(DB,uid,PASS,'product.template', 'write',id, {'default_code':cont})
            do_write2 = object_proxy.execute(DB,uid,PASS,'product.template', 'write',id, {'warranty':10})
            if do_write:
                print "OK:",cont
            cont = cont + 1
            print "Contador:",cont


def __main__():
    print 'Ha comenzado el proceso'
    _update_mass(True)
    print 'Ha finalizado la carga tabla'
__main__()
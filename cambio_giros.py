# -*- coding: utf-8 -*-
import os
import csv
import xmlrpclib
import re


HOST='100.239.86.110'
PORT=8069
DB='db'
USER='admin'
PASS='mipass'
url ='http://%s:%d/xmlrpc/' % (HOST,PORT)

common_proxy = xmlrpclib.ServerProxy(url+'common')
object_proxy = xmlrpclib.ServerProxy(url+'object')
uid = common_proxy.login(DB,USER,PASS)


print "Logeado como  %s (uid:%d)" % (USER,uid)

def _update_mass(estado):
    if estado is True:
        cont = 1

        # Filtramos lo que son compañia y tienen rut
        partner = object_proxy.execute(DB,uid,PASS,'res.partner','search',[('is_company','=',True),('document_number','!=',"")])

        for id in partner:
            print '==partner_id==',id
            act =  object_proxy.execute(DB,uid,PASS,'res.partner','read', id, ['partner_activities_ids'])
            activities = act[0]['partner_activities_ids'] #Campo 1 a n: vienen 1 o mas ids
            giro = activities and activities[0] or False
            if giro:
                eco_act = object_proxy.execute(DB,uid,PASS,'economical.activities','read', giro, ['name'])
                full_name = eco_act[0]['name']
                name_40 = full_name[0:40]
                do_write = object_proxy.execute(DB,uid,PASS,'res.partner', 'write', id, {'giro': name_40 })
                print '==eco_act==',name_40
            #if do_write:
            print "OK:",cont
            cont = cont + 1
            # print "Contador:",cont


def __main__():
    print 'Ha comenzado el proceso'
    _update_mass(True)
    print 'Ha finalizado la carga tabla'
__main__()

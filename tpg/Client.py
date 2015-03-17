#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=W0613

import json
import requests

class Client:

    def __init__(self, token):
        self.token = token
        self.baseUrl = "http://rtpi.data.tpg.ch/v1/"

    def getStops(self, stopCode=None, stopName=None,
                 line=None, latitude=None, longitude=None):
        url = "GetStops%s" % self.__get_url_params(locals().copy())
        return json.loads(self.__do_request(url))

    def getPhysicalStops(self, stopCode=None, stopName=None):
        url = "GetPhysicalStops%s" % self.__get_url_params(locals().copy())
        return json.loads(self.__do_request(url))

    def getNextDepartures(self, stopCode, departureCode=None,
                          linesCode=None, destinationsCode=None):
        url = "GetNextDepartures%s" % self.__get_url_params(locals().copy())
        return json.loads(self.__do_request(url))

    def getAllNextDepartures(self, stopCode, lineCode, destinationCode):
        url = "GetAllNextDepartures%s" % self.__get_url_params(locals().copy())
        return json.loads(self.__do_request(url))

    def getThermometer(self, departureCode):
        url = "GetThermometer%s" % self.__get_url_params(locals().copy())
        return json.loads(self.__do_request(url))

    def getThermometerPhysicalStops(self, departureCode):
        url = "GetThermometerPhysicalStops%s" % self.__get_url_params(locals().copy())
        return json.loads(self.__do_request(url))
        
    def getLinesColors(self):
        url = "GetLinesColors"
        return json.loads(self.__do_request(url))

    def getDisruptions(self):
        url = "GetDisruptions"
        return json.loads(self.__do_request(url))

    def __get_url_params(self, argDict):
        arguments = "?key=%s" % self.token
        for arg in argDict:
            if not argDict[arg] or arg == "self": continue
            arguments += "&%s=%s" % (arg, argDict[arg])
        return arguments

    def __do_request(self, url):
        reqUrl = self.baseUrl + url
        response = requests.get(reqUrl)
        body = response.text
        response.close()
        return body

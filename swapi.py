#!/usr/bin/env python3

""" A simple script to use the Star Wars API."""

import urllib.request
import json

from math import pi

base_url = "https://swapi.co/api/"

url = base_url + 'planets/1'

def print_planet(json_planet):
    print("Name:", json_planet["name"])
    print("Surface:", 4*(int(json_planet["diameter"])/2)**2*pi)
    print("Population:", json_planet["population"])
    print("Famous inhabitants:")
    for race in json_planet['residents']:
        jrace = get_api_json(race)
        print(" *", jrace['name'])

def get_api_json(url):
    request = urllib.request.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')
    with urllib.request.urlopen(request) as response:
        data = response.read()
        encoding = response.info().get_content_charset('utf-8')
        json_object = json.loads(data.decode(encoding))
        return json_object

planet = get_api_json(url)
print_planet(planet)

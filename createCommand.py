# -*- coding: utf-8 -*-
import json

with open('dict.json','r', encoding="utf-8") as f:
    data = json.load(f)

def translate(thing):

    return data[thing]
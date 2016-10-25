#!/bin/env python
# -*- coding: utf-8 -*-
"""
A number of functions to rename and modify edXml video tags in order to make them mobile ready.

.. note:: This assumes that the csv file is ordered youtube_id, edx_id
"""

import sys

import xml.etree.ElementTree as ET
import csv


def print_help():
    print('''usage: edx_id_vid -h
      edx_id_vid -a csv_filename xml_filename
      edx_id_vid -d xml_filename
      edx_id_vid -r xml_filename attribute''')



def load_csv(csv_fn):
    '''Load a csv document.'''
    edx_id_file = open(csv_fn, 'r')
    edx_id_csv = csv.reader(edx_id_file)
    edx_id_dict = {}

    for line in edx_id_csv:
        if line[0] != '':
            edx_id_dict[line[0]] = line[1]

    return edx_id_dict


def load_xml(xml_fn):
    '''Load an xml document.'''
    video_xml = ET.parse(xml_fn)
    return video_xml


def remove_edx_ids(xml_fn):
    '''
    Check an xml file for video tags, if any edx_video_ids exist, delete them.
    '''
    video_xml = load_xml(xml_fn)
    root = video_xml.getroot()
    for video in root.iter('video'):
        if 'edx_video_id' in video.keys():
            del video.attrib['edx_video_id']
            print('edx_video_id removed in {}'.format(xml_fn))
    video_xml.write(xml_fn)
    print ('Wrote {}'.format(xml_fn))


def add_edx_ids(csv_fn, xml_fn):
    '''
    Compare any youtube_x_x... or youtube attributes and gather youtube IDs.
    If any youtube ids exist that are in the csv, add an edx_video_id attribute.
    '''

    video_xml = load_xml(xml_fn)
    edx_id_dict = load_csv(csv_fn)
    root = video_xml.getroot()
    attribs = ['youtube_id_0_75',
               'youtube_id_1_0',
               'youtube_id_1_25',
               'youtube_id_1_5',
               ]
    for video in root.iter('video'):
        youtube_ids = []
        yt_ids = video.attrib['youtube'].split(',')
        for yt_id in yt_ids:
            youtube_ids.append(yt_id.split(':')[1])

        for attrib in attribs:
            if attrib in video.attrib.keys():
                youtube_ids.append(video.attrib[attrib])

        for youtube_id in youtube_ids:
            if youtube_id in edx_id_dict.keys():
                video.set('edx_video_id', edx_id_dict[youtube_id])
                video_xml.write(xml_fn)
                print ('Wrote {}'.format(xml_fn))
                break

def remove_attribute(xml_fn, attribute):
    xml_file = load_xml(xml_fn)
    root = xml_file.getroot()
    root.attrib.pop(attribute)
    xml_file.write(xml_fn)
    print ('Wrote {}'.format(xml_fn))


if __name__ == '__main__':
    if ('-h' in sys.argv[1]):
        print_help()
    elif ('-a' in sys.argv[1]):
        add_edx_ids(sys.argv[2], sys.argv[3])
    elif ('-d' in sys.argv[1]):
        remove_edx_ids(sys.argv[2])
    elif ('-r' in sys.argv[1]):
        remove_attribute(sys.argv[2], sys.argv[3])

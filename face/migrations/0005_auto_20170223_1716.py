# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
import html2text
from dateutil import parser

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def parse_html(html, data, face):
    h = html2text.HTML2Text()
    h.ignore_links = True
    text = h.handle(html.decode('utf-8'))
    rows = text.split('\n')
    for row in rows:
        if ':' in row:
            key, value = row.replace('*', ' ').strip().split(':', 1)
            if value != '':
                data[key.lower()] = value.strip()
                setattr(face, key.lower(), value.strip())


def description_parser(apps, schema_editor):
    Face = apps.get_model('face.face')
    Image = apps.get_model('core.AffixImage')
    location_objects = apps.get_model('location.location')
    author = apps.get_model('author.author')
    for face in Face.objects.all():
        html = face.description
        data = {}
        parse_html(html, data, face)
        image = Image.objects.get(id=face.image_id)
        location = update_location_model(location_objects, data, face, image)
        update_image_model(data, image, author, face)
        # export_parsed_data(data)
        # location.save()
        export_parsed_data(html, data)
        image.save()
        face.save()


def export_parsed_data(html, data):
    f = open('parsedData.txt', 'a')
    f.write(html)
    f.write('\n \n')
    for key, value in data.items():
        f.write('%s:%s\n' % (key, value))
    f.write('\n \n')
    f.close()


def export_inconsistent_data(image, face, data):
    f = open('InconsistentDate.txt', 'a')
    f.write('\nFace Title:' + str(face.title))
    f.write('Image id:' + str(image.id))
    f.write('\nDescription Date:' + str(data['date']))
    f.write('\n \n')
    f.close()


def update_image_model(data, image, author, face):
    if 'camera' in data.keys():
        image.camera = data.get('camera', '')
    if 'date' in data.keys():
        print data['date']
        try:
            image.date = parser.parse(data['date'].encode('utf-8'))
        except:
            export_inconsistent_data(image, face, data)
    if 'photographer' in data.keys():
        photographer_name = data.get('photographer', '').encode('utf-8')
        if author.objects.filter(name=photographer_name).exists():
            photographer = author.objects.get(name=photographer_name)
            image.photographers.add(photographer)

        else:
            photographer = author(name=photographer_name, slug=photographer_name.replace(' ', '-').lower())
            photographer.save()
            image.photographers.add(photographer)


class Migration(migrations.Migration):
    dependencies = [
        ('face', '0004_auto_20170223_1622'),
        ('core', '0008_auto_20170220_1223'),
        ('location', '0002_auto_20170217_1544'),
        ('author', '0005_auto_20170124_1609'),
    ]

    operations = [
        migrations.RunPython(description_parser),
    ]


def parse_contridicting_locations(face, location, data):
    f = open('ConflictingLocations.txt', 'a')

    f.write('Face title: ' + str(face.title))
    f.write('\nDescription location; '+'Image location:\n')
    f.write('State:' + str(data.get('state', '')+ ';' + str(location.state)))
    f.write('\nDistrict:' + str(data.get('district', ''))+';'+str(location.district))
    f.write('\nVillage name:' + str(data.get('village', ''))+';'+str(location.name))
    f.write('\n \n')
    f.close()


def update_location_model(location_objects, data, face, image):

    # location = location_objects.objects.get(id=face.location_id)

    locations = image.locations.all()

    for location in locations:
        print location.name
        image_location = [location.state.strip(), location.district.strip(), location.name.strip()]
        parsed_location = [data.get('state', '').strip(), data.get('district', '').strip(), data.get('village', '').strip()]
        if cmp(image_location, parsed_location) != 0:
            parse_contridicting_locations(face, location, data)
    # if location_objects.filter(state=data.get('state', ''), district=data.get('district', ''),
    #                            name=data.get('village', ''), block=data.get('block',''),
    #                            tehsil=data.get('tehsil',''), taluka=data.get('taluka','')).exists():
    #     location = location_objects.object.get(state=data.get('state', ''), district=data.get('district', ''),
    #                            name=data.get('village', ''), block=data.get('block',''),
    #                            tehsil=data.get('tehsil',''), taluka=data.get('taluka',''))
    #     image.locations.clear()
    #     image.locations.add(location)
    # for location in location_objects.all():
    #     location_values = [location.name, location.state, location.district]
    #     parsed_values = [data.get('village'], , '')ata.get('state'], , '')ata.get('district']], '')    #     if parsed_values == location_values

    # if 'block' in data.keys():
    #     location.block = data.get('block', '')
    # if 'tehsil' in data.keys():
    #     location.tehsil = data.get('tehsil', '')
    # if 'taluka' in data.keys():
    #     location.taluka = data.get('taluka', '')
    # if 'state' in data.keys():
    #     location.state = data.get('state', '')
    # if 'district' in data.keys():
    #     location.district = data.get('district', '')
    # if 'village' in data.keys() and location.name != data.get('village', ''):
    #     print location.name
    #     print data.get('village', '')
    #     location.name = data.get('village', '')
    # image.locations.add(location)

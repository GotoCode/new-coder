'''
Part III of the DataViz Tutorial

Plot the SFPD crime data on a map

New Ideas:
    - enumerate
    - dict.setdefault
    - with ... as ...
'''

from geojson import dumps

import parse as p


def create_map(parsed_data):

    # specify type of geoJSON map to create
    geo_map = {'type' : 'FeatureCollection'}
    
    item_list = []
    
    for index, line in enumerate(parsed_data):
        
        # skip over weird data points
        if line['X'] == '0' or line['Y'] == '0':
            continue
        
        data = {}
        
        # specify properties of single data point
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {
                                'title':line['Category'],
                                'description':line['Descript'],
                                'date':line['Date']
                             }
        data['geometry'] = {'type':'Point',
                            'coordinates':(line['X'], line['Y'])}
        
        item_list.append(data)
    
    # add each point to the map    
    for point in item_list:
        geo_map.setdefault('features', []).append(point)
    
    # write geoJSON data to output file for mapping
    with open('file_sf.geojson', 'w') as f:
        f.write(dumps(geo_map))
    

def main():
    data = p.parse(p.MY_FILE, ',')
    
    return create_map(data)


if __name__ == '__main__':
    main()


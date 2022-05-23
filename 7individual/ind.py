from lxml import etree as et


PATH = '3.osm'


def main():
    with open(PATH, 'r', encoding='utf-8') as file:
        data = file.readlines()
    root = et.fromstringlist(data)
    ways = []
    nodes = {}
    for appt in root.getchildren():
        if appt.tag == 'node':
            nodes[appt.get('id')] = (appt.get('lat'), appt.get('lon'))
    for appt in root.getchildren():
        if appt.tag == 'way':
            way_nodes = []
            flag = False
            for elem in appt.getchildren():
                if elem.tag == 'nd':
                    way_nodes.append(elem.get('ref'))
                elif elem.get('k') == 'building':
                    flag = True
            if way_nodes[0] == way_nodes[-1] and flag:
                ways.append({
                    'id': appt.get('id'),
                    'nodes': way_nodes
                })
    answers = {}
    for way in ways:
        answers |= {
            way['id']: []
        }
        for node in way['nodes']:
            answers[way['id']].append(nodes[node])

    for way_id in answers.keys():
        print(way_id)
        print(answers[way_id])


if __name__ == '__main__':
    main()

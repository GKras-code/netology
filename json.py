import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding='Utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
items = root.findall('channel/item')
word_list = []
for item in items:
        description = item.find('description').text        
        word_list.extend(description.split())


count_word = {}


for word in word_list:
    if len(word) < 7:
        continue

    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1
sorted_dict = dict(sorted(count_word.items(), key=lambda item: item[1], reverse=True)[:10])


pass
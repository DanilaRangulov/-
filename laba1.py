import json
max_length = 0
max_probel = 0
max_name = 0
length_no_signs = 0
text_length = 0
with open('pokemon_full.json','r') as f:
    text = json.load(f)
    for txt in text: 
        list_abilities = txt['abilities']
        description = txt['description']
        name = txt['name']
        for i in range(0,len(list_abilities)):
            s = list_abilities[i]
            count=s.count(" ")
            if count > max_probel:
                max_probel = count
            if max_probel == 2:
                max_ability = s
        max_probel=0
        length_description = len(description)
        if length_description > max_length:
            max_length = length_description
        if length_description == 171:
            max_name=name
with open('pokemon_full.json','r') as f:
    for line in f:
        text_length += len(line)
        for i in range(len(line)):
            if line[i].isalpha() != 0:
                length_no_signs += 1
print("Общее количество символов в файле:"," ", text_length)
print("Общее кол-во символов без пробелов и знаков:"," ", length_no_signs)
print("Покемон с самым длинными описанием:"," ", max_name)
print("Название умения,содержащее больше всего слов:"," ",max_ability)

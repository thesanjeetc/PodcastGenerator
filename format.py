import re

with open('transcriptsOriginal.txt', 'r', encoding="utf8") as file:
    data = file.read()
    file.close()

pattern = '\(.*\)\n|\[.*]|\(.*\)|PART.*]|…|Jamie:.*(.|\?)|[\?]|--|\.\.\.\s|Jaime(\n|.)*?\].'

result = re.sub(pattern, ' ', data)
result = result.replace('Elon Musk:  ', 'ELON MUSK:\n')
result = result.replace('Joe Rogan:  ', 'JOE ROGAN:\n')
result = result.replace('  Joe Rogan', '\nJOE ROGAN:')
result = result.replace('  Elon Musk', '\nELON MUSK:')
result = result.replace('--', '-')

wr = open('transcriptsFormatted.txt', 'w', encoding="utf8")
wr.write(result)

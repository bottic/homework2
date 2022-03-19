def unite(files):
    count = 0
    for file in files:
        with open(file, encoding = 'utf-8') as content_file:
            content = content_file.read()
            line = content.count('\n')+1
            if count == 0:
                min = line
                count = 1
                unite_content_max = f'{file}\n {line}\n {content}'
                unite_content_min = f'{file}\n {line}\n {content}'
                unite_content_mean = f'{file}\n {line}\n {content}'
            if min > line:
                min = line
                unite_content_min = f'{file}\n {line}\n {content}'
            else:
                unite_content_max = f'{file}\n {line}\n {content}'
    unite_content = f'{unite_content_min}\n {unite_content_mean}\n {unite_content_max}'
    with open('unite_content','w', encoding='utf-8') as content_file:
        content_file.write(unite_content)
# я не разобрался, как сделать для неопределённого кол-ва файлов,
# поэтому сделал основываясь на условии т.з.
unite(['1.txt','2.txt', '3.txt'])
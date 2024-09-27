import json

if __name__ == "__main__":
    files = ['train', 'dev', 'test']
    ch_path = 'corpus.ch'  # 中文
    en_path = 'corpus.en'  # 英语
    ch_lines = []
    en_lines = []

    for file in files:
        corpus = json.load(open('./json/' + file + '.json', 'r'))
        for item in corpus:
            ch_lines.append(item[1] + '\n')
            en_lines.append(item[0] + '\n')

    # with open(ch_path, "w") as fch:  # 默认gbk 编码，会报错
    #     fch.writelines(ch_lines)

    with open(ch_path, "w", encoding="utf-8") as fch:
        fch.writelines(ch_lines)

    # with open(en_path, "w") as fen:
    with open(en_path, "w", encoding="utf-8") as fen:
        fen.writelines(en_lines)

    # lines of Chinese: 252777
    print("lines of Chinese: ", len(ch_lines))
    # lines of English: 252777
    print("lines of English: ", len(en_lines))
    print("-------- Get Corpus ! --------")

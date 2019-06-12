def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)":"🙂",
        ":(":"☹",
        ";)":"😉",
        ":D":"😃",
        ":X":"🤐",
        ":o":"😯",
        "XD":"😆",
        ":p":"😋",
        ":P":"😋",
        ":/":"😕",
        ":'(":"😢"
    }
    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
    return output


message = input("Hey there send me a message with an emoji:")
print(emoji_converter(message))
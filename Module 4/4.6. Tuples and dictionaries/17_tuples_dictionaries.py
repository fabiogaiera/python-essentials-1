colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = {}
for color in colors:
    colors_dictionary.update({color[0]: color[1]})

print(colors_dictionary)

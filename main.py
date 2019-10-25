import re

def main (file_name):

    file_content_as_string = " "

    try:
        file_handle = open(file_name, "r")
        file_content_as_string = file_content_as_string.join(file_handle.readlines())
        file_handle.close ()
        return (file_content_as_string)
    except IndexError:
        print ("No file name to read")



if __name__ == '__main__':
    feelings_name = "feelings_marriott.txt"
    temp = main(feelings_name)
    feelings_source = temp.split('#')
    feelings_source.pop(0)
    #print(feelings_source) #['JW Marriott Aerocity Delhi India ', 'Oct 10 2019 -
    length = len(feelings_source)
    # print(length)

    template_name = "template.txt"
    template_source = main(template_name).split(" ")
    #print(template_source) # ['I', 'chose', '<property_name>', 'because', '<reasons>
    count=0
    pos = []
    for i in template_source:
        if (i[0]=="<"):
            index = template_source.index(i)
            template_source[index]=feelings_source[count]
            #print(template_source)
            count = count+1

    full_sentence = " ".join(template_source)
    print(full_sentence)
    #return template_source



    # positions = [];
    # sentence = template_source;
    # regex_search = '<[^>]+>'
    # regex_replace = " "
    #print(re.sub(regex_search,regex_replace,template_source))

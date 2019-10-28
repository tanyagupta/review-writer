import sys
import collections

def writefile(filename,review):
    myfile = open  (filename, 'w')
    myfile.writelines (review)
    myfile.close ()
    print ("successfully written "+filename)

def fileopen (file_name):
    file_content_as_string = " "
    try:
        file_handle = open(file_name, "r")
        file_content_as_string = file_content_as_string.join(file_handle.readlines())
        file_handle.close ()
        return (file_content_as_string)
    except IndexError:
        print ("No file name to read")

def parse_data(feelings,template):
    feelings_source = feelings.split('#')
    feelings_source.pop(0)
    print(feelings_source)
    template = template.split("#")
    if "property_name" in feelings_source and "dates" in feelings_source:
        feeling_tags = dict(zip(feelings_source[::2], feelings_source[1::2]))
        template_tags = dict(zip(template[::2], template[1::2]))
        template_tags = dict((v,k) for k,v in template_tags.items())
        print(feeling_tags.keys())
        #print(template_tags.keys())
        review = ""
        for item in feeling_tags:
            if item in template_tags:
               #print(item)
                temp = template_tags.get(item,"")
                feel = feeling_tags.get(item,"")
                review = review + temp+ feel
                #print (review)
                #print("eol")
        review = review.replace('\r', '').replace('\n', '')
        filename = (feelings_source[1]).strip().replace(' ','_')
        filename = filename +".txt"
        #print(review)
        writefile(filename,review)
    else:
        print("error")


        #print(template)
        #{'property_name': '\n JW Marriott\n ', 'dates': '\n Oct
    #     template = template.split(" ")
    #     review=""
    #
    #
    #     for item in template:
    #
    #
    #         if (not item.startswith("<")):
    #             review = review +" "+ item
    #
    #         elif (item.startswith("<")):  #if item.startswith("<") and (item.endswith(">.\n") or item.endswith(">.")or item.endswith(">")):
    #
    #             item = item.strip('>.')
    #             item = item.strip('>')
    #             item = item.strip('>.\n')
    #             item = item.strip('<')
    #
    #             if item in tags:
    #                 review = review +tags[item]
    #
    #     review = review.replace('\r', '').replace('\n', '')
    #     filename = (feelings_source[1]).strip().replace(' ','_')
    #     filename = filename +".txt"
    #     print(review)
    #     #writefile(filename,review)
    # else:
    #     print("error")


def main():
    filepath1 = sys.argv[1]
    filepath2 = sys.argv[2]
    feelings = fileopen(filepath1)
    template = fileopen(filepath2)
    parse_data(feelings,template)

if __name__ == '__main__':
    main()

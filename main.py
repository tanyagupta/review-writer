import sys

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
    #feelings_source = [i.replace('\n','') for i in feelings_source] # use this if you want to get rid of the \n
    tags = dict(zip(feelings_source[::2], feelings_source[1::2]))
    template = template.split(" ")
    #print(template) # ['I', 'chose', '<property_name>', 'because', '<reasons>
    review=""
    for item in template:
        if (not item.startswith("<")):
            review = review +" "+ item
            #print(review)
        else: #if item.startswith("<") and (item.endswith(">.\n") or item.endswith(">.")or item.endswith(">")):
            item = item.strip('>.')
            item = item.strip('>')
            item = item.strip('>.\n')
            item = item.strip('<')
            review = review +tags[item]

    review = review.replace('\r', '').replace('\n', '')
    print(review)


def main():
    filepath1 = sys.argv[1]
    filepath2 = sys.argv[2]
    feelings = fileopen(filepath1)
    template = fileopen(filepath2)
    parse_data(feelings,template)

if __name__ == '__main__':
    main()

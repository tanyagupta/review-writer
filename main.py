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
    if "property_name" in feelings_source and "dates" in feelings_source:
        #print(feelings_source)
        #feelings_source = [i.replace('\n','') for i in feelings_source] # use this if you want to get rid of the \n
        #tags = dict(zip(feelings_source[::2], feelings_source[1::2]))
        #tags = collections.defaultdict(lambda : 'Key Not found')
        tags = dict(zip(feelings_source[::2], feelings_source[1::2]))
        template = template.split(" ")
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
                if item in tags:
                    review = review +tags[item]
                else:
                    review = review + ""

        review = review.replace('\r', '').replace('\n', '')
        filename = (feelings_source[1]).strip().replace(' ','_')
        filename = filename +".txt"
        writefile(filename,review)
    else:
        print("error")


def main():
    filepath1 = sys.argv[1]
    filepath2 = sys.argv[2]
    feelings = fileopen(filepath1)
    template = fileopen(filepath2)
    parse_data(feelings,template)

if __name__ == '__main__':
    main()

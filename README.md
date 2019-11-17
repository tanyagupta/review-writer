# review-writer
## Objective
Using natural language processing for smart review writing

## Phase 1: Use a supervised classifier to automatically tag new reviews with the following category labels

```#reason#
#dates#
#duration#
#expectation#
#hotel_location#
#staff_experience#
#staff_name#
#room_size#
#room_location#
#room_decor#
#breakfast#
#local_info#
#early_check_in#
#food#
#minibar#
#value_for_money#
#conclusion#
```

### Data description

The data at the first level is a Dictionary with two keys, reviews, and HotelInfo.

The value of the key reviews is an array of reviews where each array element is a dictionary. Each dictionary has keys Ratings, AuthorLocation, Title, Author, ReviewID, Content and Date.

The Ratings key has a dictionary as a value. The dictionary contains service, cleanliness, Overall, Value, Sleep Quality, Rooms and Location. The other keys have string values.

There are 12,774 hotels in this data set.

#### Sample data
```
{
   "Reviews":[
      {
         "Ratings":{
            "Service":"1",
            "Cleanliness":"2",
            "Overall":"1.0",
            "Value":"1",
            "Sleep Quality":"2",
            "Rooms":"2",
            "Location":"3"
         },
         "AuthorLocation":"Coffs Harbour, Australia",
         "Title":"\u201cWorst Sydney stay ever\u201d",
         "Author":"hazza55",
         "ReviewID":"UR126310463",
         "Content":"...blah..",
         "Date":"March 19, 2012"
      },
      "HotelInfo":{
    "Name":"Criterion Hotel",
    "HotelURL":"/ShowUserReviews-g255060-d645391-Reviews-Criterion_Hotel-Sydney_New_South_Wales.html",
    "Price":"0",
    "Address":"<address class=\"addressReset\"><span rel=\"v:address\"><span dir=\"ltr\"><span class=\"street-address\" property=\"v:street-address\">Pitt and Park Streets</span>, <span class=\"locality\"><span property=\"v:locality\">Sydney</span>, <span property=\"v:region\">New South Wales</span></span>, <span class=\"country-name\" property=\"v:country-name\">Australia</span> </span></span></address>",
    "HotelID":"645391",
    "ImgURL":""
 }.....

}
```

### Task details and tool selection :
* We will need to thus identify the selection of the tool (PyTorch, NLTK etc.) and then decide how to tag the data while keeping in mind the tool we will use
* We will need to build a feature set (from category labels) with feature names similar to [NPS chat corpus](https://catalog.ldc.upenn.edu/desc/addenda/LDC2010T05.xml)

* NPS Chat corpus example:
```
<Post class="whQuestion" user="11-09-20sUser101">
11-09-20sUser31 why arent you employed?
<terminals>
<t pos="NNP" word="11-09-20sUser31"/>
<t pos="WRB" word="why"/>
<t pos="VBP" word="arent"/>
<t pos="PRP" word="you"/>
<t pos="JJ" word="employed"/>
<t pos="." word="?"/>
</terminals>
</Post>
```
* Our example:
```
[{tag="food",sentence="The buffet breakfast was amazing!"},{tag="conclusion",sentence="The hotel was terrible"}]
```
* Once this is done, we construct the training and testing data by applying the feature extractor to each review text

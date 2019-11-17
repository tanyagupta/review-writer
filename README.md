# review-writer
## Objective
Using natural language processing for smart review writing

### Phase 1: Use a supervised classifier to automatically tag new reviews with the following category labels

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

### Details:
* Build a feature set (from category labels) with feature names e.g. a feature name could be "conclusion" and the corresponding value "The hotel was terrible". Similar to [NPS chat corpus](https://catalog.ldc.upenn.edu/desc/addenda/LDC2010T05.xml)
* An example using the above:
```[({'contains(the)': True, 'contains(hotel)': True, 'contains(was)': True, 'contains(terrible)': True}, 'Conclusion')] ```
* Construct the training and testing data by applying the feature extractor to each review text

### Data descriptions
The data at the first level is a Dictionary with two keys, reviews, and HotelInfo.
The value of reviews is an array of reviews. Each array element is a dictionary. Keys are Ratings, AuthorLocation, Title, Author, ReviewID, Content and Date.

The Ratings key has a dictionary as a value. The dictionary contains service, cleanliness, Overall, Value, Sleep Quality, Rooms and Location. 

There are 12,774 hotels in this data.

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

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

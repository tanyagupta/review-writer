# review-writer
## Objective
Using natural language processing for smart review writing

### Step 1
* Decide what features of the reviews are relevant
* Build a feature set with feature names e.g. a feature name could be "conclusion" and the corresponding value "The hotel was terrible". Similar to [NPS chat corpus](https://catalog.ldc.upenn.edu/desc/addenda/LDC2010T05.xml)
* An example using the above:
```[({'contains(the)': True, 'contains(hotel)': True, 'contains(was)': True, 'contains(terrible)': True}, 'Conclusion')] ```
* Construct the training and testing data by applying the feature extractor to each review text

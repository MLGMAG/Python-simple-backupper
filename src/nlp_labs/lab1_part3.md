# Lab 1. Part 3

## Author
[Roman Kyslyi](https://www.linkedin.com/in/romankyslyi/)

## Description

There is a [dataset](https://huggingface.co/datasets/yelp_review_full).  

You can work with a subset of the dataset, but the whole statistics should be calculated for at least 10,000 documents (or more). Also, it is possible to take a test split (50_000 reviews).  

Tasks:  
 - Write a function that selects spans (non-empty paragraphs in the document).
 - Explore paragraphs that do not begin with a letter. Make a list of the most frequent tokens.
 - Write patterns that look for words in the text with letters `a`, longer than 2 letters; `t`, longer than 3 letters. Count their number per 10,000 documents.
 - Change the pattern to only search for non-stop words on `a` and `t`, with no length limit. Count their number per 10_000, compare.
 - Measure the processing time per 1 document using: `pipe`, `en_core_web_md`, `en_core_web_sm`, `regexp` (compare not only the time but also the results, is it possible to detect without spaCy?)
 - Find phrases containing `very/`, `much/`, `so/`, `good/`, `bad/` and their forms, find their most frequent occurrences, taking into account the number of stars in the review (label).
 - Write a pipeline element that, from the obtained characteristics, draws a conclusion about the level of emotionality of the text.

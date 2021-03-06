# Semantic Nutrition
This repo demonstrates how our semantic nutrition API works. We submitted this process as a clinical abtract to MLHC 2020 ([poster](Poster_Semantic_Nutrition.pdf), [abstract](Abstract_Semantic_Nutrition.pdf)). 

**This is a base implementation of what was presented at the MLHC**, and operates on a limited dataset. The dataset we used for training and publication is not ours to share. If you're interested in using your own nutrition dataset with this API, you can designate a different (local or hosted) csv when you initialize the class. The USDA provides an excellent [starting point](https://fdc.nal.usda.gov) to build a dataset.

## Installation
#### Requires Python >= 3.6
```
pip install food2vec
```

## Usage

```
from food2vec.semantic_nutrition import Estimator

estimator = Estimator() 

# Search database for nutrition estimates
match = estimator.natural_search("I ate an apple") 

# Embed words or phrases with food content (limited to our food-related vocabulary)
# Here, embedding1 will be equal to embedding2
embedding1 = estimator.embed('apple')
embedding2 = estimator.embed('I ate an apple')

# See the relationship between embeddings
embedding1 = estimator.embed('orange')
embedding2 = estimator.embed('apple')
relationship = estimator.cosine(embedding1, embedding2)

# Use your own nutrition dataset
my_estimator = Estimator(food_data_filepath = 'my_nutrition_data.csv')

# Use your own embeddings
my_estimator = Estimator(food_embeddings_filepath = 'my_embeddings.csv')
```

## Connecting to mobile assistants, placing the API in an online server, and managing a database

For testing purposes, we used [Siri Shortcuts](https://support.apple.com/en-us/HT209055) (iOS) and [Google Assistant / IFTTT webhooks](https://ifttt.com/google_assistant) (Android) to send voice transcriptions to [Google Firebase](https://firebase.google.com/docs/storage/web/start). Once received, the incoming data would trigger a [Firebase Cloud Function](https://firebase.google.com/docs/functions). The Firebase Function relayed the voice transcription to our [Semantic Nutrition API](semantic.py)(hosted online with [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) and [Google App Engine](https://cloud.google.com/appengine/docs/standard/python3/building-app)), which responded with estimates for nutrition data. The nutrition data was then logged in Google Firebase.

While useful for testing and demonstrations, this method has been depecrated in favor of a native mobile application and private server / database. Please stay tuned for future developments, and feel free to use our API locally in the meantime!

*updated on 7/27/2020*

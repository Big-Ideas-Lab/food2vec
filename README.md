# Semantic Nutrition
This repo demonstrates how our basic semantic nutrition API works. We submitted this process as a clinical abtract to MLHC 2020 [poster, abstract].

## API (Local)

```
pip install semantic-nutrition
```

## Connecting to mobile assistants, placing the API in an online server, and managing a database
We're currently in the process of developing native applications for iOS (Siri) and Android (Google Assistant) to leverage their local voice command capabilities. 

For testing purposes, we used Siri Shortcuts (iOS) and Google Assistant / IFTTT (Android) to send voice transcriptions to Google Firebase. Once received, the incoming data triggered an online Firebase Function. The Firebase Function sent the voice transcription to our Semantic Nutrition API (hosted with Flask and Google App Engine), which responds with estimates for nutrition data. The nutrition data was then logged in Google Firebase. We do not recommend this method for handling sensitive data / protected patient information. 

While useful for testing and demonstrations, this method has been depecrated in favor of a native mobile application and private server / database. Please stay tuned for future developments, and feel free to use our API locally in the meantime!
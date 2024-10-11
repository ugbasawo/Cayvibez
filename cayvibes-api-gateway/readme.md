# Consuming social authentication
    Facebook
    curl -X POST -d "grant_type=convert_token&client_id=<client_id>&client_secret=<client_secret>&backend=facebook&token=<facebook_token>" http://localhost:8000/auth/convert-token
    
    Google
    curl -X POST -d "grant_type=convert_token&client_id=<django-oauth-generated-client_id>&client_secret=<django-oauth-generated-client_secret>&backend=google-oauth2&token=<google_token>" http://localhost:8000/auth/convert-token

    Instagram
    curl -X POST -d "grant_type=convert_token&client_id=<django-oauth-generated-client_id>&client_secret=<django-oauth-generated-client_secret>&backend=github&token=<access_token>" http://localhost:8000/auth/convert-token

    Twitter
    

### Console to retrieve client ID and secret
###### Facebook
You can obtain the ID (SOCIAL_AUTH_FACEBOOK_KEY) and secret (SOCIAL_AUTH_FACEBOOK_SECRET) of your app from [Facebook](https://developers.facebook.com/apps/)
###### Google
To obtain your app’s ID (SOCIAL_AUTH_GOOGLE_OAUTH2_KEY) and secret (SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET), visit [Google](https://console.developers.google.com/apis/credentials)
###### Instagram
Follow these [guidelines](https://developers.facebook.com/docs/instagram-basic-display-api/getting-started) in order to create and configure your application
###### Twitter
Twitter offers per application keys named Client ID and Client Secret. To enable Twitter these two keys are needed. Further documentation at [Twitter development resources](https://developer.x.com/en/docs/authentication/oauth-2-0/authorization-code)
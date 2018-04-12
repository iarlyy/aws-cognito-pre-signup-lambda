# aws-cognito-pre-signup-lambda


### Setup

#### 1 - AWS Web Console > Lambda > Create Function (Use python 3.6 as runtime)

#### 2 - Paste content of cognito_pre_signup_parser.py into Function code

#### 3 - Set the env var

```
ALLOWED_DOMAINS_REGEX = ^[A-Za-z0-9\.\+_-]+@(domain1.com$|domain2.com$)
```

#### 4 - Cognito > User pools > ###Your_user_Pool## > Triggers > Select the lambda function on the drop down menu for "Pre sign-up"

#### 5 - Test

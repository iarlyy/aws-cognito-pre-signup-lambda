import os
import re


def lambda_handler(event, context):
    email = event["request"]["userAttributes"]["email"]
    allowed_domains_regex = os.environ.get("ALLOWED_DOMAINS_REGEX")

    if event["triggerSource"] == "PreSignUp_ExternalProvider" and re.match(allowed_domains_regex, email):
        event["response"]["autoConfirmUser"] = True
        event["response"]["autoVerifyEmail"] = True
        event["response"]["autoVerifyPhone"] = True
        return event

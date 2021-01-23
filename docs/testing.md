
# Manual testing

1. `cd` into a new directory and create `wev.yml`:

```yaml
[AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN]:
  plugin:
    id: wev-awsmfa
```

1. Create an IAM user named _x_ and attach this inline policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "iam:GetUser",
                "iam:ListMFADevices"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:iam::*:user/${aws:username}"
            ]
        },
        {
            "Action": "s3:ListAllMyBuckets",
            "Condition": {
                "Bool": {
                    "aws:MultiFactorAuthPresent": "true"
                }
            },
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

1. Use `aws configure` to set the user's credentials into a new profile named _y_.
1. Temporarily set this new profile as the default:

```bash
export AWS_DEFAULT_PROFILE=<Y>
```

1. Confirm that you do not have permission to list your S3 buckets:

```bash
aws s3 ls
```

```text
An error occurred (AccessDenied) when calling the ListBuckets operation: Access Denied
```

1. Install `wev` and `wev-awsmfa`:

```bash
pipenv install wev wev-awsmfa
```

1. Use `wev` to list your S3 buckets:

```bash
wev --log-level debug aws s3 ls
```

You should be prompted for a token, then your S3 buckets should be listed.

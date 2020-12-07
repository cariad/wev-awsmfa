# wev-awsmfa: A `wev` plugin to support Amazon Web Services multi-factor authentication on the command line

**This is pre-release software. Use at your own peril!**

[wev](https://github.com/cariad/wev) (**w**ith **e**nvironment **v**ariables)is a command line tool for resolving environment variables and running shell commands.

The `wev-awsmfa` plugin allows you to verify your Amazon Web Services via multi-factor authentication without needing to modify your credentials file.

## Example

Say your IAM user policy requires you to verify your identity via multi-factor authentication. If you try to use the `aws` command line…

```bash
aws s3 ls
```

…your request is denied, because you didn't multi-factor authenticate:

```text
An error occurred (AccessDenied) when calling the ListBuckets operation: Access Denied
```

With an appropriate `.wev.yml` configuration (see below), you can run the `aws` command line via `wev`:

```bash
wev aws s3 ls
```

```text
Resolving AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and AWS_SESSION_TOKEN...
We need your token.

Token:
```

Enter your one-time token, then `wev-awsmfa` will create a temporary session, set the environment variables, then run the command:

```text
2019-10-13 11:42:03 bucket-one-87yiuhhguy98ouo
2019-10-13 11:42:27 bucket-two-kjhu65564ewtrgd
2020-07-03 15:38:22 bucket-thr-08uytgftryjh766
```

## Installation

Install [wev](https://github.com/cariad/wev), then:

```bash
pip3 install wev-awsmfa
```

## Configuration

The _key_ must be a list of three strings, describing the environment variables to set for:

1. The access key ID. You probably want this to be `AWS_ACCESS_KEY_ID`.
1. The secret access key. You probably want this to be `AWS_SECRET_ACCESS_KEY`.
1. The session token. You probably want this to be `AWS_SESSION_TOKEN`.

Your minimal configuration is likely to look like this:

```yaml
[AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN]:
  plugin:
    id: wev-awsmfa
    mfa_device: choo choo
```

There are two optional properties:

- `mfa_device` describes the ARN of the MFA device to use. `wev-awsmfa` will attempt to discover this automatically if omitted.
- `duration` describes the duration of the temporary session, in seconds. Default is 900 seconds.

```yaml
[AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN]:
  plugin:
    id: wev-awsmfa
    duration: 1800
    mfa_device: arn:aws:iam::123456789012:mfa/foo
```

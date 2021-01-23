# wev-awsmfa<br />A wev plugin to support Amazon Web Services multi-factor authentication on the command line

[![codecov](https://codecov.io/gh/cariad/wev-awsmfa/branch/main/graph/badge.svg?token=TS995LZMW1)](https://codecov.io/gh/cariad/wev-awsmfa)

- ⚙️ Plugin for **[wev](https://github.com/cariad/wev)**.
- 👮 Takes your **one-time token** and creates a **temporary multi-factor authenticated session**.
- 📋 **Caches** your temporary session to **minimise prompts**.

[![asciicast](https://asciinema.org/a/386493.svg)](https://asciinema.org/a/386493)

## 🔥 The Problem

Say your IAM user policy requires you to verify your identity via multi-factor authentication.

This limits your ability to use the `aws` CLI because you can't provide MFA tokens with your requests.

`wev-awsmfa` extends [wev](https://github.com/cariad/wev) to prompt for your one-time tokens and authenticate you automatically.

## 🎁 Installation

`wev-awsmfa` requires Python 3.8 or later and `wev`.

```bash
python -m pip install wev
python -m pip install wev-awsmfa
```

## ⚙️ Configuration

### Filename and location

See [wevcli.app/configuration](https://wevcli.app/configuration) for a detailed guide to `wev` configuration files.

If in doubt, create your configuration file as `wev.yml` in your project directory.

### Keys

`wev-awsmfa` must be configured to resolve three environment variables:

| Index | Description       | Suggested name          |
|------:|-------------------|-------------------------|
| 0     | AWS access key ID | `AWS_ACCESS_KEY_ID`     |
| 1     | AWS secret key    | `AWS_SECRET_ACCESS_KEY` |
| 2     | AWS session token | `AWS_SESSION_TOKEN`     |

### Properties

`wev-awsmfa` supports two optional properties:

| Property   | Description                                  | Default                                   |
|------------|----------------------------------------------|-------------------------------------------|
| duration   | Duration of the temporary session in seconds | 900                                       |
| mfa_device | ARN of the multi-factor device to use        | _Attempt to discover automatically._ |

### Examples

#### Minimal configuration

```yaml
[AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN]:
  plugin:
    id: wev-awsmfa
```

#### 30-second sessions

```yaml
[AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN]:
  plugin:
    id: wev-awsmfa
    duration: 1800
    mfa_device: arn:aws:iam::123456789012:mfa/foo
```

## 💻 Usage

Run `wev` with any command that requires a multi-factor authenticated session.

For example, to run `aws s3 ls` in a multi-factor authenticated session:

```bash
wev aws s3 ls
```

You'll be prompted to enter your one-time token, then `wev` will authenticate you and run the command.

More examples:

- [Amazon Web Services multi-factor authentication on the command line](https://wevcli.app/examples/aws-mfa-on-command-line/) on [wevcli.app](https://wevcli.app).


## FAQs 🙋‍♀️

### Will wev-awsmfa work with my scripts?

Yes! `wev-awsmfa` will work with _any_ command line application or script that requires a multi-factor authenticated session

## Thank you! 🎉

My name is **Cariad**, and I'm an [independent freelance DevOps engineer](https://cariad.me).

I'd love to spend more time working on projects like this, but--as a freelancer--my income is sporadic and I need to chase gigs that pay the rent.

If this project has value to you, please consider [☕️ sponsoring](https://github.com/sponsors/cariad) me. Sponsorships grant me time to work on _your_ wants rather than _someone else's_.

Thank you! ❤️

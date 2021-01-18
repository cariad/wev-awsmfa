# wev-awsmfa<br />A wev plugin to support Amazon Web Services multi-factor authentication on the command line

[![codecov](https://codecov.io/gh/cariad/wev-awsmfa/branch/main/graph/badge.svg?token=TS995LZMW1)](https://codecov.io/gh/cariad/wev-awsmfa)

- ⚙️ Plugin for **[wev](https://github.com/cariad/wev)** (**w**ith **e**nvironment **v**ariables).
- 👮 Handles your **one-time token** to create a **temporary authenticated session**.
- 📋 **Caches** your temporary session to **minimise prompts for your token**.

![](https://github.com/cariad/wev-awsmfa/blob/main/docs/demo.gif?raw=true)

## The Problem 🔥

Say your IAM user policy requires you to verify your identity via multi-factor authentication.

This limits your ability to use the `aws` CLI because you can't provide MFA tokens with your request:

```text
$ aws s3 ls

An error occurred (AccessDenied) when calling the ListBuckets operation: Access Denied
```

`wev-awsmfa` extends [wev](https://github.com/cariad/wev) to ask for your one-time tokens as-needed and authenticate you automatically.

## Installation 🎁

`wev-awsmfa` requires Python 3.8 or later.

```bash
pip3 install wev
pip3 install wev-awsmfa
```

## Configuration ⚙️

### Location

[wev](https://github.com/cariad/wev) configuration files apply to the _working_ and _child_ directories.

This gives you a few options for where to place your configuration:

- If you always need multi-factor authentication then place the configuration in your home directory (i.e. `~/.wev.yml`).
- If you're a contractor working on mutiple projects with a client (i.e. you have `~/client-foo/project-a` and `~/client-foo/project-b`) that requires multi-factor authentication then place the configuration in your client's project directory (i.e. `~/client-foo/.wev.yml`).
- If you have only one project that requires multi-factor authentication then place the configuration in that project's directory (i.e. `~/project-foo/.wev.yml`).

### Content

A minimal configuration would look like this:

```yaml
[AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN]:
  plugin:
    id: wev-awsmfa
```

Optional properties:

- `mfa_device`: ARN of the MFA device to use. `wev-awsmfa` will attempt to discover this automatically if omitted.
- `duration`: Duration of the temporary session, in seconds. Default is 900 seconds.

A configuration with these optional properties set would look like this:

```yaml
[AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN]:
  plugin:
    id: wev-awsmfa
    duration: 1800
    mfa_device: arn:aws:iam::123456789012:mfa/foo
```

## Usage ⌨️

With `wev` and `wev-awsmfa` installed and configured, you can run the `aws` CLI via `wev` in a multi-factor authenticated session:

```bash
wev aws s3 ls
```

You'll be prompted to enter your one-time token, then `wev` will authenticate you and run the command.

## FAQs 🙋‍♀️

### Will wev-awsmfa work with my scripts?

Yes! `wev-awsmfa` will work with _any_ command line application or script that requires a multi-factor authenticated session

## Thank you! 🎉

My name is **Cariad**, and I'm an [independent freelance DevOps engineer](https://cariad.me).

I'd love to spend more time working on projects like this, but--as a freelancer--my income is sporadic and I need to chase gigs that pay the rent.

If this project has value to you, please consider [☕️ sponsoring](https://github.com/sponsors/cariad) me. Sponsorships grant me time to work on _your_ wants rather than _someone else's_.

Thank you! ❤️

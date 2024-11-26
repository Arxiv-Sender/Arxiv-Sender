# Getting Started for Custom Arxiv Paper Email Sender
This page is for tutorial on Custom Arxiv Paper Email Sender. If you follow the guidelines below, it will run without problems. 

#### Step 1. Create Organization
Create an Organization. The reason for doing this is to receive an alarm. 

Fork `MUST` be done with the created organization.

#### Step 2. Fork this repository
Fork this repository. Just click the fork button in the top right corner.

Once the repository is created, you `MUST` turn on issues in the repository settings.

`Settings` -> `General` -> turn on `issues` at `Features`

#### Step 3. Set Github token
Set envorinment variable with github token.

1. Generate Personal Token

`Personal Profile` -> `Settings` -> `Developer settings` -> `Personal access tokens` -> `Tokens (classic)` -> `Generate new token` -> `Generate new token (classic)`

Then, you need to setup your token.

Note : Any name that you want.

Expiration : Any time, but it is good as long as possible.

Select scopes : You `MUST Check repo`.

Then, you can copy your token.

2. Set Secret Variables.

`Copy token` -> `Back to your repo` -> `Setting` -> `Secrets and variables` -> `Actions` -> `New repository secret`

Then, you need to enter your token.

Name* : The name `MUST` be set to `MY_GITHUB_TOKEN`.

Secret* : Paste your token.

#### Step 4. Custom Setting

1. set `.github/workflow/python-package.yaml` file.

    - cron : This is the argument for set sending period. You can refer to [https://crontab.guru](https://crontab.guru) and edit it there.

    - token : You MUST SET SECRET ENVIRONMENTS. Do NOT Change This.

    - organization: You MUST SET HERE to same as this organization.

    - repository: You MUST SET HERE to same as this repository.

    - search_limitation: This is the number of papers to search. Feel free to change it, but the larger the better. Default is `'9999'`.

    - send_limitation: This is the limit on the number of papers to upload per email. Default is `'100'`.

    - send_term: This will determine how up-to-date your paper should be sent. Default is `'1'`.

    - abstract: Type False for enable abstract in email. Default is `False`.

        - If you set abstract to True, be careful not to exceed the character limit (65536).


2. set `keywords.yaml` file.

    - You can assign your custom search keywords. Use `-` to remove or add.
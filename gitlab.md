How to download job artifacts from gitlab using curl
====================================================

Make a [personal access token][token] and save it to `$token`

Find the project and job id.   These are just decimal numbers and they are shown
in the UI and in the URL for the project and the job.   Save them in `$project`
and `$job`.  Then the command is:

```
curl -f --header "PRIVATE-TOKEN: $token" \
    -o artifacts.zip \
    "https://gitlab.example.com/api/v4/projects/$project/jobs/$job/artifacts" 
```

[token]: https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html
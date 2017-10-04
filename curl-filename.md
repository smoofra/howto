How to download a file with curl, and preserve the filename
===========================================================

How to download a file with curl, and preserve the filename.  Also follow
redirects and authenticate as a user.

    vm5: local$ curl -O  -J -L -u USERNAME https://bats.apple.com/api/v1/osxkit/download/9131285/
    Enter host password for user 'USERNAME:
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
    100 19.8M  100 19.8M    0     0  18.0M      0  0:00:01  0:00:01 --:--:-- 22.7M
    curl: Saved to filename 'OSXKit-9131285_SomeTrain99A1234_macOS_DSTROOT.tgz'
    

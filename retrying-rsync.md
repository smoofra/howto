How to auto-restart rsync when it's not making progress
==================

`--timeout=60` will cause a failure after a minute of no IO progress.


    while ! rsync --timeout=60  --partial --progress demogorgon:foo.tgz .  ; do echo doh; sleep 1; done

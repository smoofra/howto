How to copy only matching files with rsync but recurse into all directories
===========================================================================

Sometimes you want to recursively copy a directory tree, by only include files
from that tree that match a certain pattern.  This is tricky with rsync because
the filters apply to directories as well as files, so if you simple exclude
everything that doesn't match it will exclude directories that don't match and
not recurse into them.  The solution is to include all directories, then
include the patterns you want then, exclude anything that isn't a directory.


    rsync -rul --filter '+ **/' --include '*foobar*' --include 'lol*' --filter '-! **/' src/ dest/

How to trap retain and release with dtrace
=======================================

Warning: this generates a *lot* of data quite quickly.

    pid$target:libobjc:objc_retain:entry {
        printf("retain %x", arg0);
        ustack();
    }
    
    
    pid$target:libobjc:objc_release:entry {
        printf("release %x", arg0);
        ustack();
    }
    
    pid$target:CoreFoundation:CFRetain:entry {
        printf("retain %x", arg0);
        ustack();
    }


    pid$target:CoreFoundation:CFRelease:entry {
        printf("release %x", arg0);
        ustack();
    }


invoke with:

    dtrace -s retain-release.d -b 50M -p `pgrep ProcName`


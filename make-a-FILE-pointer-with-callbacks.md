How do you make a `FILE *` with callbacks?
=======================================

How do you make a `FILE *` that calls your callbacks on `fread()` and `fwrite()`
instead of writing to a file descriptor.

* On glibc, use [fopencookie(3)](http://man7.org/linux/man-pages/man3/fopencookie.3.html)

* On FreeBSD or Mac OS, use [funopen(3)](https://www.freebsd.org/cgi/man.cgi?query=funopen&sektion=3&apropos=0&manpath=freebsd)

CMAKE cheat sheet
=================


<a name="DSTROOT"></a>
### How to do the equivalent of `DSTROOT=... make install` with cmake/ninja

The goal here is to pass an installation prefix only to the install step.
It's not good enough to run cmake with `-DCMAKE_INSTALL_PREFIX=$prefix`,
that would reconfigure the project with a prefix, possibly influencing
where the project thinks it will be installed at runtime, ie this is like
`./configure --prefix=$prefix` in an autoconf based project.

However, If you look at the ninja rule for install, all it does
is call a cmake script.   So instead of saying `ninja install`, do this:

```
cmake -DCMAKE_INSTALL_PREFIX=$DSTROOT/$prefix -P cmake_install.cmake
```

Note that this is different than `DSTROOT` in that it entirely replaces the
old prefix, so you need to include both the DSTROOT and the runtime prefix
in `CMKAE_INSTALL_PREFIX` when you do this.

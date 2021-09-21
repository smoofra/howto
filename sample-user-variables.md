How to use dtrace to sample variables from a userspace program
==============================================================

For example, lets say we have a C function like this, running on arm64, 
and we'd like to know what `*(vars->outcount)` is at the end.


```
struct vars { 
    foo *a, *b;
    uint32_t *outcount;
}

void some_function(struct vars *vars) 
{ 
    do_some_stuff()
}

```

Then we could use a dtrace script like this to sample it:

```
pid$target:SomeProgram:some_function:entry { 
	self->varsp = uregs[R_X1];
}

pid$target:SomeProgram:some_function:return { 
	outcountp =  *(uintptr_t*) copyin(self->varsp + 0x10, 8);
	outcount =  *(uint32_t *) copyin(outcountp, 4);
	trace(outcount)
}
```

Invoke it as `dtrace -s foo.d -p $(pgrep SomeProgram)`
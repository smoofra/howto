LLDB cheat sheet
================

<a name="imaloo"></a>
### Look up a global address to find what it is


    (lldb) image lookup -a 0xffffff8000557749
          Address: kernel.development[0xffffff8000557749] (kernel.development.__TEXT.__text + 3204937)
          Summary: kernel.development`vfs_trace_paths_callback + 9 at vfs_subr.c
          

<a name="source"></a>
### Tell LLDB where your source code is

    (lldb) list  vfs_trace_paths_callback
    File: /src/./xnu/xnu-5106/bsd/vfs/vfs_subr.c
    (lldb) settings set target.source-map /src/./xnu/xnu-5106 /src/xnu
    (lldb) list  vfs_trace_paths_callback
    File: /src/./xnu/xnu-5106/bsd/vfs/vfs_subr.c
       9896		}
       9897	
       9898		return VNODE_RETURNED;
       9899	}
       9900	
       9901	static int vfs_trace_paths_callback(mount_t mp, void *arg) {
       9902		if (mp->mnt_flag & MNT_LOCAL)
       9903			vnode_iterate(mp, VNODE_ITERATE_ALL, vnode_trace_path_callback, arg);
       9904	
       9905		return VFS_RETURNED;
       9906	}
       9907	
       9908	static int sysctl_vfs_trace_paths SYSCTL_HANDLER_ARGS {
       9909		struct vnode_trace_paths_context ctx;
       9910	


Note: You can also use `source list -a` to find the full paths for the source at a particular address.

<a name="list-all-source"></a>
### List all the source files LLDB knows about

    (lldb) script print(*[unit.file.fullpath for module in lldb.target.modules for unit in module.compile_units], sep="\n")

or just for the main executable:

    (lldb) script print(*[unit.file.fullpath for unit in lldb.target.modules[0].compile_units], sep="\n")


<a name="registers-at-pc"></a>
### Find out what's in registers at a particular code address

        (lldb) disas -m  -s 0x1924 -e 0x1924+4

        179 	
        180 		for (int i = 1; i >= 0; i--) {
        181 			struct radix_edge *edge = &node->edges[i];
        ** 182 			if (!edge_valid(edge)) {

        MallocStackLogging`radix_tree_lookup_recursive:
        MallocStackLogging[0x1924] <+108>: ldur   w9, [x25, #0x6]


        (lldb) image lookup -v -a   0x1924
            Address: MallocStackLogging[0x0000000000001924] (MallocStackLogging.__TEXT.__text + 176)
            Summary: MallocStackLogging`radix_tree_lookup_recursive + 108 at radix_tree.c:182:8
            ...
            FuncType: id = {0x7fffffff0000039f}, byte-size = 0, decl = radix_tree.c:147, compiler_type = "struct answer (struct radix_tree *, struct interval, struct interval, struct radix_node *, int)"
            Blocks: id = {0x7fffffff0000039f}, range = [0x000018b8-0x00001ba8)
                    id = {0x7fffffff00000427}, ranges = [0x00001904-0x00001914)[0x00001924-0x000019f0)[0x00001a00-0x00001b7c)
                    id = {0x7fffffff0000043b}, ranges = [0x00001924-0x000019f0)[0x00001a00-0x00001b7c)
            Symbol: id = {0x00000063}, range = [0x00000000000018b8-0x0000000000001ba8), name="radix_tree_lookup_recursive"
            Variable: id = {0x7fffffff00000440}, name = "edge", type = "radix_edge *", location = , decl = radix_tree.c:181
            Variable: id = {0x7fffffff0000042c}, name = "i", type = "int", location = DW_OP_consts +1, DW_OP_stack_value, decl = radix_tree.c:180
            Variable: id = {0x7fffffff000003b8}, name = "tree", type = "radix_tree *", location = DW_OP_reg24 W24, decl = radix_tree.c:147
            Variable: id = {0x7fffffff000003c7}, name = "keys", type = "interval", location = DW_OP_reg22 W22, DW_OP_piece 0x8, DW_OP_reg21 W21, DW_OP_piece 0x8, decl = radix_tree.c:148
            Variable: id = {0x7fffffff000003d6}, name = "nodekeys", type = "interval", location = DW_OP_reg20 W20, DW_OP_piece 0x8, DW_OP_reg5 W5, DW_OP_piece 0x8, decl = radix_tree.c:149
            Variable: id = {0x7fffffff000003e5}, name = "node", type = "radix_node *", location = DW_OP_reg25 W25, decl = radix_tree.c:150
            Variable: id = {0x7fffffff000003f4}, name = "keyshift", type = "int", location = DW_OP_reg23 W23, decl = radix_tree.c:151

    
<a name="python-version"></a>
### Select what version of python LLDB will use (Mac OS)

    $ defaults write com.apple.dt.lldb DefaultPythonVersion 3
    $ lldb

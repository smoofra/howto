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
    
    

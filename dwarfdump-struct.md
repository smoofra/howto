How to use dwarfdump to read structure layouts by hand
=====================================================

`dwarfdump` can be used to dump out structure layouts from dsym bundles in a
somewhat human readable form.

* `-c` says to include children of the selected entries
* `-n isa_t` says to search for entries named isa_t
* `-arch arm64` selects the arm64 slice.  Don't forget this if you're working with fat binaries.

`$ dwarfdump -c -arch arm64  -n isa_t libobjc.A.dylib.dSYM/Contents/Resources/DWARF/libobjc.A.dylib | less`

There can be multiple matches because there are multiple compilation units that
use the same type.

The `TAG_member` entries give info about the fields of the union or structure.

Here we can see `isa_t` is a union.  The `cls` member is at location 0, as is
the `bits` member.  (They can both be at the same place because it's a union).

There is also a unnamed structure member at the same location, and we see it has
a number of bitfield members, because they have `AT_bit_size` and
`AT_bit_offset` attributes.

To read a bitfield, load the word (sized by `AT_byte_size`) located at
`AT_data_member_location`.  The `AT_bit_offset` is the number of bits to the
"left" of the field, that is the number of bits in the word which are more
significant than the field.   So to read it you calculate:

`(word >> (byte_size*8 - (bit_size + bit_offset))) & ((1 << (bit_size))-1)`

This is what the output of dwarfdump looks like:

    ----------------------------------------------------------------------
     File: libobjc.A.dylib.dSYM/Contents/Resources/DWARF/libobjc.A.dylib (arm64)
    ----------------------------------------------------------------------
    Searching .debug_info for 'isa_t'... 15 matches:

    0x00007e18: TAG_union_type [114] *
                 AT_name( "isa_t" )
                 AT_byte_size( 0x08 )
                 AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                 AT_decl_line( 68 )

    0x00007e20:     TAG_member [6]
                     AT_name( "cls" )
                     AT_type( {0x0000000000003bdb} ( Class ) )
                     AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                     AT_decl_line( 73 )
                     AT_data_member_location( +0 )

    0x00007e32:     TAG_member [6]
                     AT_name( "bits" )
                     AT_type( {0x00000000000000d5} ( uintptr_t ) )
                     AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                     AT_decl_line( 74 )
                     AT_data_member_location( +0 )

    0x00007e44:     TAG_member [115]
                     AT_type( {0x0000000000007e52} ( struct  ) )
                     AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                     AT_decl_line( 93 )
                     AT_data_member_location( +0 )

    0x00007e52:     TAG_structure_type [5] *
                     AT_byte_size( 0x08 )
                     AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                     AT_decl_line( 93 )

    0x00007e56:         TAG_member [116]
                         AT_name( "nonpointer" )
                         AT_type( {0x00000000000000d5} ( uintptr_t ) )
                         AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                         AT_decl_line( 94 )
                         AT_byte_size( 0x08 )
                         AT_bit_size( 0x01 )
                         AT_bit_offset( 0x3f )
                         AT_data_member_location( +0 )

    0x00007e6b:         TAG_member [116]
                         AT_name( "has_assoc" )
                         AT_type( {0x00000000000000d5} ( uintptr_t ) )
                         AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                         AT_decl_line( 95 )
                         AT_byte_size( 0x08 )
                         AT_bit_size( 0x01 )
                         AT_bit_offset( 0x3e )
                         AT_data_member_location( +0 )

    0x00007e80:         TAG_member [116]
                         AT_name( "has_cxx_dtor" )
                         AT_type( {0x00000000000000d5} ( uintptr_t ) )
                         AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                         AT_decl_line( 96 )
                         AT_byte_size( 0x08 )
                         AT_bit_size( 0x01 )
                         AT_bit_offset( 0x3d )
                         AT_data_member_location( +0 )

    0x00007e95:         TAG_member [116]
                         AT_name( "shiftcls" )
                         AT_type( {0x00000000000000d5} ( uintptr_t ) )
                         AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                         AT_decl_line( 97 )
                         AT_byte_size( 0x08 )
                         AT_bit_size( 0x21 )
                         AT_bit_offset( 0x1c )
                         AT_data_member_location( +0 )

    0x00007eaa:         TAG_member [116]
                         AT_name( "magic" )
                         AT_type( {0x00000000000000d5} ( uintptr_t ) )
                         AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                         AT_decl_line( 98 )
                         AT_byte_size( 0x08 )
                         AT_bit_size( 0x06 )
                         AT_bit_offset( 0x16 )
                         AT_data_member_location( +0 )

    0x00007ebf:         TAG_member [116]
                         AT_name( "weakly_referenced" )
                         AT_type( {0x00000000000000d5} ( uintptr_t ) )
                         AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                         AT_decl_line( 99 )
                         AT_byte_size( 0x08 )
                         AT_bit_size( 0x01 )
                         AT_bit_offset( 0x15 )
                         AT_data_member_location( +0 )

    0x00007ed4:         TAG_member [116]
                         AT_name( "deallocating" )
                         AT_type( {0x00000000000000d5} ( uintptr_t ) )
                         AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                         AT_decl_line( 100 )
                         AT_byte_size( 0x08 )
                         AT_bit_size( 0x01 )
                         AT_bit_offset( 0x14 )
                         AT_data_member_location( +0 )

    0x00007ee9:         TAG_member [116]
                         AT_name( "has_sidetable_rc" )
                         AT_type( {0x00000000000000d5} ( uintptr_t ) )
                         AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                         AT_decl_line( 101 )
                         AT_byte_size( 0x08 )
                         AT_bit_size( 0x01 )
                         AT_bit_offset( 0x13 )
                         AT_data_member_location( +0 )

    0x00007efe:         TAG_member [116]
                         AT_name( "extra_rc" )
                         AT_type( {0x00000000000000d5} ( uintptr_t ) )
                         AT_decl_file( "/BuildRoot/Library/Caches/com.apple.xbs/Sources/objc4/objc4-699/runtime/objc-private.h" )
                         AT_decl_line( 102 )
                         AT_byte_size( 0x08 )
                         AT_bit_size( 0x13 )
                         AT_bit_offset( 0x00 )
                         AT_data_member_location( +0 )

    0x00007f13:         NULL

    ...

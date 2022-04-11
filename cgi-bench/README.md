# CGI benchmark

## Overview

Assume that you are given a very underpowered CloudLinux (container) on a static web host.
Is has a very low allowance for CPU speed, memory and disk I/O - as low as 64kB/s.

Such limits do not apply to static assets directly over the web server or if a given file already resides within the disk cache.
However, as few other users run CGI scripts on such an underpowered static host, most of your data files and libraries will be evicted rapidly.

It can make CGI response quicker with less standard deviation and less timeouts caused by extremes if the program is as efficient as possible.

### Factors

The following efficiency metrics influence response time:

* the size of the CGI script or binary itself
* the size of any needed interpreter or dynamic linker
* the number of attempts and the size of each file, folder and library being accessed
* parsing, compiling and any other computation by the interpreter on startup
* runtime performance and memory overhead of the interpreter
* peak memory consumption: RSS and VMEM
* output buffering

### Tools

* `ldd a.out`
* `objdump -x a.out`
* `readelf -a a.out`
* `hd a.out`
* `strace ./a.out`
* `valgrind -v --tool=memcheck ./a.out`
* `gdb -ex "b _exit" -ex "run" ./a.out`, on another terminal: `pmap -x $(pidof a.out)`
* `gdb -ex "b _exit" -ex "run ./hi.py.cgi" $(which python)`
* `gdb -ex "catch syscall" -ex "run" ./hi.write.asm.c.cgi`
* `perf stat -e instructions:u ./a.out`

## Results

According to preliminary tests, in order of decreasing quality:

* statically linked C, ideally 4-8kB: not doing any I/O, it's response time is always spot on, though it could still take a few hundred ms if anything got swapped out (DNS, apache.conf, web root, .htaccess, ELF)
* C, dynamically linked only to libc
* C, dynamically linked to other libraries as well
* dash, bash, mawk, lua, gawk: hard to measure a difference
* PERL: still pretty fast, but a bit slower than lua
* PHP: the worst case peak and the standard deviation is better than Python, but on average not much faster
* Python: less than 100ms if warmed up, but could take many seconds first, complicated libraries might even time out (parsing through lots of sources)
* gcc: can time out at first even for a trivial program, but should cache itself after an attempt or two up to a usable level

## Notes

### C++

Small static compile via musl, cassandra, uv, pthread, protobuf, zlib, stdc++

https://uhlenheuer.net/posts/2016-08-23-cpp_build_static_executable.html

Explanation of the various ELF sections

https://oneraynyday.github.io/dev/2020/05/03/Analyzing-The-Simplest-C++-Program/

Confirmation:

* https://github.com/Jonimoose/libfxcg/issues/50
* https://blog.mozilla.org/nnethercote/2011/01/18/the-dangers-of-fno-exceptions/
* https://www.thecodeteacher.com/question/43440/c++---What-is-__gxx_personality_v0-for
* https://gcc.gcc.gnu.narkive.com/1eRNfvat/new-statement-and-fno-exceptions

* `void *__gxx_personality__v0;`
* `.cfi_personality`

Tips by elegant invention:

* -fno-exceptions
* -fno-rtti (for `dynamic_cast<>()` and `typeid()`)
* overload new and delete operators that don't throw `std::bad_alloc`
* extern "C" void __cxa_pure_virtual() { while(1); }
* __gnu_cxx::__verbose_terminate_handler()
* std::set_terminate()
* http://elegantinvention.com/blog/information/smaller-binary-size-with-c-on-baremetal-g/

### gcc man

* `-fnothrow-opt`
* `-fno-enforce-eh-specs`
* `-mno-fp-exceptions`
* `-fcheck-new`
* `-flto` instead of `-ffunction-sections -fdata-sections -Wl,--gc-sections`
* `-W -Wall -Wextra`
* `-fno-pie -no-pie` for static
* `-Wl,--no-ld-generated-unwind-info`
* https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags

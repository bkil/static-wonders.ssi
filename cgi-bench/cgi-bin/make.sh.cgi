#!/bin/sh

main() {
  printf "Content-type: text/plain\n\n"
  {
    mkdir -p "var" &&
    touch var/index.html &&
    compile
  } 2>&1
}

compile() {
  dynamic
  asm
  normal
  static

  ls -l *.c.cgi
}

asm() {
  O="hi.write.asm.c.cgi"
  [ -f "$O" ] && return
  MUSL="var/musl.o"

  if ! [ -f "$MUSL" ]; then
    MUSLC="var/musl.c"
    if ! [ -f "$MUSLC" ]; then
      MUSRC="\
        var/syscall_arch.h \
        var/syscall.h \
        var/syscall_ret.c \
        musl_kludge.c \
        var/write.c \
        var/_Exit.c"
      get https://github.com/bminor/musl/raw/master/src/internal/syscall.h &&
      get https://github.com/bminor/musl/raw/master/arch/x86_64/syscall_arch.h &&
      get https://github.com/bminor/musl/raw/master/src/internal/syscall_ret.c &&
      get https://github.com/bminor/musl/raw/master/src/unistd/write.c &&
      get https://github.com/bminor/musl/raw/master/src/exit/_Exit.c &&

      {
        grep -h ' *#include <' $MUSRC
        grep -vh '#include ' $MUSRC
      } > "$MUSLC" ||
      return
    fi

    gcc \
      -v \
      -Dhidden="__attribute__((visibility(\"hidden\")))" \
      -D_Noreturn="__attribute((__noreturn__))" \
      -Os \
      -c \
      -o "$MUSL" \
      "$MUSLC" ||
    {
      echo $?
      return
    }
  fi

  gcc \
    -v \
    -nostartfiles \
    -nostdlib \
    -static \
    -Os \
    -Wl,--nmagic,--build-id=none,--sort-section=alignment,--gc-sections,-z,noseparate-code \
    -o "$O" \
    hi.write.asm.c \
    "$MUSL" \
    -lgcc &&

  strip \
    -R .eh_frame \
    -R .comment \
    $O ||

  echo $?
}

get() {
  URL="$1"
  FILE="var/`basename "$URL"`"
  if ! [ -f "$FILE" ]; then
    wget -O "$FILE" -A- "$URL"
  fi
}

static() {
  O="hi.write.static.c.cgi"
  [ -f "$O" ] && return

# this needs `libc6-dev` installed
# -flto

  gcc \
    -v \
    -ffunction-sections -fdata-sections \
    -nostartfiles \
    -static \
    -Os \
    -Wl,--nmagic,--build-id=none,--sort-section=alignment,--gc-sections,-z,noseparate-code \
    -o "$O" \
    hi.write.static.c &&

  strip \
    -R .eh_frame \
    -R .comment \
    -R .tbss \
    -R .got.plt \
    "$O" ||

  echo $?
}

dynamic() {
  O="hi.write.dl.c.cgi"
  [ -f "$O" ] && return

  gcc \
    -v \
    -fno-unwind-tables \
    -fno-asynchronous-unwind-tables \
    -nostartfiles \
    -Os \
    -Wl,--build-id=none \
    -o "$O" \
    hi.write.dl.c &&

  strip \
    -R .eh_frame \
    -R .gnu.hash \
    -R .gnu.version \
    -R .comment \
    "$O" ||

  echo $?
}

normal() {
  O="hi.write.dl.c.cgi"
  [ -f "$O" ] && return

  gcc \
    -v \
    -Os \
    -s \
    -o "$O" \
    hi.printf.c ||

  echo $?
}

main "$@"

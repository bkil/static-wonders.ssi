#include <stdio.h> // STDOUT_FILENO
#include <unistd.h> // write _exit

#define HI "Content-type: text/plain\n\nhi\n"

//__attribute__((force_align_arg_pointer))
void _start(void) {
  write(STDOUT_FILENO, HI, sizeof(HI) - 1);
  _exit(0);
}

#include <stdio.h> // STDOUT_FILENO
#include <unistd.h> // write _Exit

#define HI "Content-type: text/plain\n\nhi\n"

void _start(void) {
  write(STDOUT_FILENO, HI, sizeof(HI) - 1);
  _Exit(0);
}

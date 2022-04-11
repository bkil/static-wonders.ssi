#include "var/syscall.h"

static int errno_val;

long (__syscall_cp)(syscall_arg_t nr,
                    syscall_arg_t u, syscall_arg_t v, syscall_arg_t w,
                    syscall_arg_t x, syscall_arg_t y, syscall_arg_t z)
{
  return __syscall(nr, u, v, w, x, y, z);
}

int *__errno_location(void)
{
  return &errno_val;
}

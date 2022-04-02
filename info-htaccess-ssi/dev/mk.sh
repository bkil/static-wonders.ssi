#!/bin/sh

main() {
  get_variables
}

get_variables() {
  cat << EOF
<table>
  <thead>
    <tr>
      <th>Variable
      <th>Value
  <tbody>
EOF

  cat << EOF |
Includes 1
DATE_GMT
DATE_LOCAL
DOCUMENT_ARGS
DOCUMENT_NAME
DOCUMENT_PATH_INFO
DOCUMENT_URI
LAST_MODIFIED
QUERY_STRING_UNESCAPED
USER_NAME
Advanced 1
API_VERSION
AUTH_TYPE
CONN_LOG_ID
CONN_REMOTE_ADDR
CONTENT_TYPE
CONTEXT_DOCUMENT_ROOT
CONTEXT_PREFIX
DOCUMENT_ROOT
HANDLER
HTTP2
HTTP_ACCEPT
HTTP_COOKIE
HTTP_FORWARDED
HTTP_HOST
HTTP_PROXY_CONNECTION
HTTP_REFERER
HTTPS
HTTP_USER_AGENT
IPV6
IS_SUBREQ
PATH_INFO
QUERY_STRING
REMOTE_ADDR
REMOTE_HOST
REMOTE_IDENT
REMOTE_PORT
REMOTE_USER
REQUEST_FILENAME
REQUEST_LOG_ID
REQUEST_METHOD
REQUEST_SCHEME
REQUEST_STATUS
REQUEST_URI
SCRIPT_FILENAME
SCRIPT_GROUP
SCRIPT_USER
SERVER_ADMIN
SERVER_NAME
SERVER_PORT
SERVER_PROTOCOL
SERVER_SOFTWARE
THE_REQUEST
TIME
TIME_DAY
TIME_HOUR
TIME_MIN
TIME_MON
TIME_SEC
TIME_WDAY
TIME_YEAR
Printenv 1
DATE_GMT
DATE_LOCAL
DOCUMENT_NAME
GATEWAY_INTERFACE
HTTP_ACCEPT_ENCODING
HTTP_ACCEPT_LANGUAGE
HTTP_CACHE_CONTROL
HTTP_CONNECTION
HTTP_DNT
HTTP_SAVE_DATA
HTTP_SEC_GPC
HTTP_UPGRADE_INSECURE_REQUESTS
PATH
SCRIPT_NAME
SERVER_ADDR
set 1
BASH
BASHOPTS
BASH_ALIASES
BASH_ARGC
BASH_ARGV
BASH_CMDS
BASH_EXECUTION_STRING
BASH_LINENO
BASH_SOURCE
BASH_VERSINFO
BASH_VERSION
DIRSTACK
EUID
GROUPS
HOSTNAME
HOSTTYPE
IFS
MACHTYPE
OPTERR
OPTIND
OSTYPE
POSIXLY_CORRECT
PPID
PS4
PWD
SHELL
SHELLOPTS
SHLVL
TERM
UID
Found 1
SERVER_SIGNATURE
EOF
  while read VAR HEAD; do
    if [ -n "$HEAD" ]; then
    cat << EOF
    <tr class=heading><th colspan=2>$VAR
EOF
    else
      cat << EOF
    <tr><th>$VAR<td><!--#echo var="$VAR" -->
EOF
    fi
  done

  echo "</table>"
}

main "$@"

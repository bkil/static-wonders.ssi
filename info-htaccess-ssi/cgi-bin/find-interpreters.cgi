#!/bin/sh
echo "Content-type: text/plain"
echo

if [ -f found-interpreters.txt ]; then
  cat found-interpreters.txt
else
{

bash --version |
head -n 2

echo

sed --version |
head -n 2

echo

awk --version |
head -n 2

echo

gawk -V |
head -n 2

echo

mawk -W version 2>&1 |
grep -v "^$"

echo

curl --version

echo

wget --version |
grep -E "^(GNU|[+])"

echo

perl --version 2>&1 |
grep -v "^$" |
head -n 3

# printf "l\nq\n" | instmodsh ; echo

cat << "EOF" |
use ExtUtils::Installed;
my $installed = ExtUtils::Installed->new();
my $x = $kakak;
foreach my $module ($installed->modules()) {
 my $version = $installed->version($module) || "?";
 print "$module $version\n";
}
exit;
EOF
perl

echo

python --version

echo

python2 --version
# python2 -c 'help("modules");exit();'

echo

python3 --version
# python3 -c 'help("modules");exit();'

pip list
ls /usr/lib/python*/*-packages
ls /usr/local/lib/python*/*-packages

echo

conda list

echo

lua -v

cat << EOF |
local seen={}
function dump(t,i)
  seen[t]=true
  local s={}
  local n=1
  for k in pairs(t) do
    s[n]=k
    n=n+1
  end
  table.sort(s)
  for k,v in ipairs(s) do
    print(i..v)
    v=t[v]
    if type(v)=="table" and not seen[v] then
      dump(v,i.."  ")
    end
  end
end
dump(_G," ")
EOF
lua -

echo

echo 'puts "tclsh [info patchlevel]"' |
tclsh

echo

ruby --version

echo

java -version

echo

gcc --version | head -n 2

echo

clang --version

echo

php --version

echo

go version

echo

mono --version

echo

echo "nodejs `nodejs --version 2>/dev/null || echo ": command not found"`"

} 2>&1 |
tee found-interpreters.txt
fi

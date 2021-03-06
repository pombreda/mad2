#/bin/bash -el
set -e
######################################################################
# colors

bold="\033[1m"
red="\033[38;5;197m"
green="\033[38;5;76m"
blue="\033[38;5;69m"
purple="\033[38;5;129m"
reset="\033[0m"

######################################################################
#catch errors
function on_error {
    echo -e "${bold}${red}Caught an error ${purple}:(${reset}"
    echo -e "in ${green}$2${reset}, line: ${red}$1${reset}"
    exit -1
}

trap 'on_error ${LINENO} ${test_script}' ERR


#create dummy data
function test_data {
    for x in $(seq -w 1 $1)
    do
	for y in $(seq -w 1 $x)
	do
	    echo $x $y >> a00$x.test
	done
    done
}

function skip_test {
    echo -e "${red}#### ${purple}Skipping${reset} ($test_script)"

}

function start_test {
    echo -e "${red}#### ${green}Test${purple}: ${blue}${*}${reset} ($test_script)"
}

if [ -z "$1" ]
then
    pattern='????.*.sh'
    verbose='+v'
else
    pattern="*${1}*"
    verbose='-v'
fi
for test_script in $(find scripts/ -name "${pattern}" | grep "\.sh$")
do
    rm -rf test
    mkdir test
    cd test
    set $verbose
    . ../$test_script
    set +v
    cd ..
    rm -rf test
done

######################################################################
#set +v
echo "Success."



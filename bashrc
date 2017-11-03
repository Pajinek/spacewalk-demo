# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

PS1="[\[\e[32m\]\u\[\e[0m\]@\h \W]\\$ "

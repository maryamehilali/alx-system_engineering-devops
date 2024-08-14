Debugging is fun only when you know how to do it
First find the pid of the apache2 process

ps a-e | grep apache2
use that in the following command

strace -p <pid> 
This will run run strace of that program, the problem will aprear when we curl for localhost in the other tmuw window the second time
we will get an error "no such file or directory" on a file with the extention phpp a wrong extension. And since this is found in the php settings file... just correct it and you are good to go.
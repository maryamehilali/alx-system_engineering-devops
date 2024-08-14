# Configures SSH for no password and specifying IdentityFile

$line_string = "Host 100.25.153.157\n\
    IdentityFile ~/.ssh/school\n\
    PasswordAuthentication no\n"

file {"/etc/ssh/ssh_config":
    ensure => file,
    content => $line_string
}
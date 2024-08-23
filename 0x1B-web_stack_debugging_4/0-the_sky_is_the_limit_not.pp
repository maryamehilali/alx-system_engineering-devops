Fix our stack so that we get to 0 errors

file { '/etc/default/nginx':
  ensure  => present,
  content => 'ULIMIT="-n 10000"\n',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
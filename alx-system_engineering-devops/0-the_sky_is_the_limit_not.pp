# Manifest sets the ULIMIT value for Nginx and restarts the service.

$ulimit_value = '4096'

file { '/etc/default/nginx':
ensure  => file,
content => "ULIMIT=\"-n ${ulimit_value}\"\n",
notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
command     => '/usr/bin/sudo service nginx restart',
refreshonly => true,
}

service { 'nginx':
ensure => running,
enable => true,
}

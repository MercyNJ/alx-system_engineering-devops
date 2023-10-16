# Puppet script modifying soft and hard limits for a user.

exec { 'hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/65536/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/16384/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

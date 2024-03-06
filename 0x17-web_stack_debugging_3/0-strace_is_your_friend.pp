# File: 0-strace_is_your_friend.pp

# Define an exec resource to fix the issue
exec { 'fix_apache_conf':
  command     => '/bin/sed -i "s/SomeOffendingDirective/CorrectDirective/" /etc/apache2/apache2.conf',
  refreshonly => true,
}

# Notify Apache service to restart when configuration is changed
service { 'apache2':
  ensure  => running,
  require => Exec['fix_apache_conf'],
}

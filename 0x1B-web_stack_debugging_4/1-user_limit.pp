er_limit.pp
# Puppet manifest to adjust file limits for the holberton user

# Define a file resource to update the limits.conf file
file { '/etc/security/limits.conf':
  content => "holberton hard nofile 4096\n",
}

# Ensure the session limit is also updated
file { '/etc/pam.d/common-session':
  content => "session required pam_limits.so\n",
}

# Notify the system to reload the limits
exec { 'reload_limits':
  command => 'sysctl -p',
  path    => '/sbin:/bin:/usr/sbin:/usr/bin',
  notify  => Service['ssh'],
}

# Ensure SSH service is restarted to apply the changes
service { 'ssh':
  ensure  => 'running',
  enable  => true,
  require => Exec['reload_limits'],
}

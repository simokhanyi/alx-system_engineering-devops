# Puppet class to manage Nginx configuration

class { 'nginx':
  # Ensure Nginx service is running and enabled
  ensure => 'running',
  enable => true,  # Corrected parameter name to 'enable'
}

# Define a Puppet resource to manage Nginx configuration file
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  # Owner and group for the configuration file
  owner   => 'root',
  group   => 'root',
  # Set appropriate permissions for the configuration file
  mode    => '0644',
  # Content of the Nginx configuration file
  content => template('nginx/nginx.conf.erb'),
  # Notify Nginx service to reload if the configuration file changes
  notify  => Service['nginx'],
}

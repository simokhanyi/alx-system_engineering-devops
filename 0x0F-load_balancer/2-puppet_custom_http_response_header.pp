# File: 2-puppet_custom_http_response_header.pp

# Include the nginx class from the jfryman/nginx module
include nginx

# Define a custom HTTP header in the Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Class['nginx'],
  notify  => Service['nginx'],
}

# Enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify => Service['nginx'],
}

# Custom template for Nginx configuration
file { '/etc/nginx/custom_header.conf':
  ensure  => file,
  content => "add_header X-Served-By $hostname always;",
  require => Class['nginx'],
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Class['nginx'],
}

# Notify about changes to the service
service { 'nginx':
  subscribe => File['/etc/nginx/sites-available/default'],
  subscribe => File['/etc/nginx/sites-enabled/default'],
  subscribe => File['/etc/nginx/custom_header.conf'],
}

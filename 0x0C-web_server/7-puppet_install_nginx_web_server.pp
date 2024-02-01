# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}

# Configure Nginx server block
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx_config/nginx.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable the redirect configuration
file { '/etc/nginx/sites-available/redirect_me':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Custom Nginx configuration template
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx_config/nginx_default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Hello World HTML page
file { '/usr/share/nginx/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

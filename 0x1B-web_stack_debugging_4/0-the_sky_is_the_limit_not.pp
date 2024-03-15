# Puppet class to manage Nginx installation and configuration

class nginx_traffic_increase {

  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Modify Nginx configuration for handling more traffic
  file { '/etc/nginx/nginx.conf':
    ensure  => present,
    replace => true,
    content => template('nginx/nginx.conf.erb'), # Corrected template path
    notify  => Service['nginx'],
    require => Package['nginx'], # Require nginx package before modifying the config
  }

  # Service definition for Nginx
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'], # Require nginx package before starting the service
  }
}

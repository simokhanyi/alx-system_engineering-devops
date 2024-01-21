# Puppet script to create ssh config file

file { '/root/.ssh/config':
  ensure  => present,
  content => '
Host 34.203.75.160
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
',
  mode    => '0600',
  owner   => 'root',
  group   => 'root',
}

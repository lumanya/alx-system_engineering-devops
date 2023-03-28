# client configuration file (w/Puppet)

file { '/root/.ssh/config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "
  Host ubuntu
     Hostname 100.25.41.182
     User ubuntu
     IdentityFile ~/.ssh/school
     PasswordAuthentication no
  ",
  }

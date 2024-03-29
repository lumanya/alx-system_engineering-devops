# Add custom HTTP header  with Puppet
exec { 'update':
     command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => 'add_header X-Served-By $http_header_value;',
}

service { 'nginx':
  ensure => running,
}

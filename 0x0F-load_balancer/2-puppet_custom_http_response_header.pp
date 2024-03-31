# Puppet manifest for configuring Nginx with a custom HTTP header

# Update package lists
exec { 'update_package_lists':
  command => '/usr/bin/apt-get update',
  unless  => '/usr/bin/apt-get -qq update | /bin/grep -q "All packages are up to date"',
}

# Ensure Nginx package is installed
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update_package_lists'],
}

# Define custom HTTP header in a separate file
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => 'file',
  content => "add_header X-Served-By ${::hostname};",
  notify  => Service['nginx'],
}

# Manage Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => Package['nginx'],
  subscribe => File['/etc/nginx/conf.d/custom_headers.conf'],
}

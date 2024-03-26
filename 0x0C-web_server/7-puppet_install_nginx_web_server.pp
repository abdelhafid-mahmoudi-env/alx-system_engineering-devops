# Ensure the nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Define the Nginx class
class { 'nginx':
  manage_repo => true,
  listen_port => 80,
}

# Define a custom file resource for the default HTML file
file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => "Hello World!\n",
  require => Class['nginx'],
}

# Define server configuration
nginx::resource::vhost { 'default':
  www_root          => '/var/www/html',
  listen_port       => 80,
  index_files       => ['index.html', 'index.htm', 'index.nginx-debian.html'],
  error_log_file    => '/var/log/nginx/error.log',
  access_log_file   => '/var/log/nginx/access.log',
  location_cfg_append => {
    '/' => {
      try_files => '$uri $uri/ =404',
    },
    '/redirect_me' => {
      rewrite => '^(.*)$ https://www.github.com/besthor permanent',
    },
    '/404.html' => {
      internal => true,
    },
  },
  error_pages       => {
    '404' => '/404.html',
  },
}

# Define custom 404 error page
file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n",
  require => Class['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Class['nginx'], Package['nginx']],
}

# Add a line to the Nginx configuration file
file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/besthor permanent;',
}

# Ensure the default HTML file is created
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

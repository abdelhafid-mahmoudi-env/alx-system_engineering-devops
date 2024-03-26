# Add stable version of Nginx repository
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  unless  => 'apt-cache policy | grep -q "nginx/stable"',
  notify  => Exec['update packages'],
}

# Update software packages list
exec { 'update packages':
  command => 'apt-get update',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  refreshonly => true,
}

# Install Nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update packages'],
}

# Allow HTTP traffic through the firewall for Nginx
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  unless  => "ufw status | grep -q 'Nginx HTTP'",
}

# Set folder permissions for /var/www/html
file { '/var/www/html':
  ensure  => 'directory',
  mode    => '0755',
  owner   => 'root',
  group   => 'root',
}

# Create index.html file
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => "Hello World!\n",
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

# Create custom 404.html page
file { '/var/www/html/404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page\n",
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

# Configure Nginx default server block with redirection and custom error page
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => @("EOT"
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }

    if (\$request_uri ~* "/redirect_me") {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
EOT
),
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  require => File['/var/www/html', '/var/www/html/index.html', '/var/www/html/404.html'],
  notify  => Service['nginx'],
}

# Restart Nginx service after configuration changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}

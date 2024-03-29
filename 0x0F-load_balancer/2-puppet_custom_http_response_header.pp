# 2-puppet_custom_http_response_header.pp

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Define custom header configuration for Nginx
$file_content = "# Custom Nginx configuration\nserver {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\tserver_name _;\n\n\t# Add custom HTTP header if not already present\n"
if !system("grep -q 'X-Served-By' /etc/nginx/sites-available/default") {
    $file_content += "\tadd_header X-Served-By $::hostname;\n"
}
$file_content += "\n\t# Other configuration directives...\n}"

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $file_content,
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

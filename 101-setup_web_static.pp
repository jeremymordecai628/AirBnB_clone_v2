# Install Nginx package
package { 'nginx':
  ensure => installed,
} ->

# Create directory structure
file { '/data':
  ensure => 'directory',
} ->

file { '/data/web_static':
  ensure => 'directory',
} ->

file { '/data/web_static/releases':
  ensure => 'directory',
}->

file { '/data/web_static/shared':
  ensure => 'directory',
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory',
} ->

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Holberton School Puppet\n',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
} ->

file { '/var/www/html':
  ensure => 'directory'
} ->

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n"
} ->

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
} ->

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => "\
server {
    listen 80;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}
",
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}

exec { 'nginx restart':
  path => '/etc/init.d/'
}

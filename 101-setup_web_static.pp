# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create directory structure
file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
}

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

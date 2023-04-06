# Install Nginx pachage

package { 'nginx':

  ensure => installed,
}

# configure Nginx Server
file { '/etc/nginx/sites-enabled/default':
  content => "server {
		listen 80 default_server;
		listen [::]:80 default_server;

		
		root /var/www/html;
		index index.html;


		server_name _;

		location / {
			try_files $uri $uri/ =404;
		}

		location /redirect_me {
			return 301 https://churchycodes.co.tz;
		}
		}",
}

# Remove default Nginx index.html file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Restart Nginx Service 
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [
    File['/etc/nginx/sites-enabled/default'],
    File['/var/www/html/index.html'],
  ],
}

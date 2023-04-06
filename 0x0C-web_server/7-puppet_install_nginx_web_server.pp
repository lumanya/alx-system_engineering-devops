# Install Nginx pachage

package { 'nginx':

  ensure => installed,
}


exec { 'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/blog.ehoneahobed.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

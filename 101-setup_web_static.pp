# Puppet manifest to set up web servers for the deployment of web_static

package { 'nginx':
  ensure => 'installed',
}

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  recurse => true,
}

file { '/data/web_static/shared':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  recurse => true,
}


file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => '<!DOCTYPE html>
<html lang="en">
<head>
    <!-- ... (your HTML content here) ... -->
</head>
<body>
    <h1>Hello World</h1>
    <a href="https://bio.link/olajide">Adeniji Olajide</a>
</body>
</html>',
  mode    => '0644',
}
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

exec { 'alias':
  command => 'sudo sed -i "/location \/ {/a\
location /hbnb_static/ {\n\
    alias /data/web_static/current/;\n}" /etc/nginx/sites-enabled/default',
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default', '/data/web_static/current'],
}

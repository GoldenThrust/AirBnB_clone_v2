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
  content => template('module_name/index.html.erb'), # Use an ERB template for the HTML content
  mode    => '0644',
}

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

exec { 'alias':
  command => 'sudo sed -i "/location \/ {/alocation /hbnb_static/ {\n    alias /data/web_static/current/;\n}" /etc/nginx/sites-enabled/default',
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

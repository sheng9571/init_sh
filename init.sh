# change source list
sudo sed -i '1, $s/tw.archive.ubuntu.com/free.nchc.org.tw/g' /etc/apt/sources.list


# install requirement packages
sudo apt-get update
sudo apt-get install -y ntp ntpdate python-setuptools python-dev build-essential vim tmux zsh git openssh-server libxml2-dev libxslt-dev


# time correction
export TZ='Asia/Taipei';
sudo /etc/init.d/ntp stop && sudo cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime && sudo ntpdate tw.pool.ntp.org && sudo /etc/init.d/ntp start


# install easy_install、pip、requests、lxml
sudo easy_install pip
sudo pip install --upgrade pip
sudo pip install requests lxml


# set default shell and link config files
chsh -s $(which zsh)
cd ~
git clone --recursive https://github.com/sheng9571/dotfiles.git ~/.dotfiles
cd ~/.dotfiles
make
cd ~

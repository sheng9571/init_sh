sudo apt-get update && sudo apt-get install -y libncurses5-dev libncursesw5-dev 
wget ftp://ftp.vim.org/pub/vim/unix/vim-7.4.tar.bz2 -P $HOME
cd $HOME && tar -xjf vim-7.4.tar.bz2
cd ~/vim74
./configure --prefix=/usr --with-features=huge --enable-rubyinterp --enable-pythoninterp
make && sudo make install
cd $HOME && rm -rf ~/vim74
echo Install vim 7.4 complete ...

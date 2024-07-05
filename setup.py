#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import os
import json
import urllib.request
import subprocess

name = ''
email = ''
options = { 'developer': '', 'android': '', 'ios': '', 'designer': '',
            'vim': '', 'zsh': '', 'flutter': '',
            'animations': '', 'showhiddenfiles': '', 'autoupdate': '', }


# Check if Xcode Command Line Tools are installed
if os.system('xcode-select -p') != 0:
  print("Installing XCode Tools")
  os.system('xcode-select --install')
  os.system('softwareupdate --install-rosetta --agree-to-license')
  print("**************************************************************")
  print("Install the XCode Command Line Tools and run this script again")
  print("**************************************************************")
  exit()

# Accept XCode License
# os.system('sudo xcodebuild -license accept')

# Sudo: Spectacle, ZSH, OSX Settings
print("\n\nWelcome... TO THE WORLD OF TOMORROW\n")

# Basic Info
while name == '':
  name = input("What's your name?\n").strip()

while email == '' or '@' not in email:
  email = input("What's your work email?\n").strip()


# Setup Options
while options['designer'] not in ['y', 'n']:
  options['designer'] = input("Do you want to install Designer Tools? (y|n) [y]  ") or "y"

while options['developer'] not in ['y', 'n']:
  options['developer'] = input("Do you want to install Developer Tools? (y|n) [y]  ") or "y"

if options['developer'] == 'y':
  while options['android'] not in ['y', 'n']:
    options['android'] = input("Do you want to install Android Tools? (y|n) [n]  ") or "n"

  while options['ios'] not in ['y', 'n']:
    options['ios'] = input("Do you want to install iOS Tools? (y|n) [n]  ") or "n"
  
  while options['flutter'] not in ['y', 'n']:
    options['flutter'] = input("Do you want to install Flutter SDK? (y|n) [n]  ") or "n"


# Other Options
while options['vim'] not in ['y', 'n']:
  options['vim'] = input("Do you want to install VIM with Awesome VIM? (y|n) [y]  ") or "y"

while options['zsh'] not in ['y', 'n']:
  options['zsh'] = input("Do you want to install Oh My Zsh? (y|n) [y]  ") or "y"

while options['animations'] not in ['y', 'n']:
  options['animations'] = input("Do you want to accelerate OSX animations? (y|n) [y]  ") or "y"

while options['showhiddenfiles'] not in ['y', 'n']:
  options['showhiddenfiles'] = input("Do you want to show hidden files? (y|n) [y]  ") or "y"

while options['autoupdate'] not in ['y', 'n']:
  options['autoupdate'] = input("Do you want to update your computer automatically? (y|n) [y]  ") or "y"


def show_notification(text):
  os.system('osascript -e \'display notification "{}" with title "Mac Setup"\' > /dev/null'.format(text))


print("Hi {}!".format(name))
print("You'll be asked for your password at a few points in the process")
print("*************************************")
print("Setting up your Mac...")
print("*************************************")


# Create a Private Key
if not os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub'):
  print("Creating your Private Key")
  os.system('ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "{}"'.format(email))


# Set computer name & git info (as done via System Preferences → Sharing)
os.system('sudo scutil --set ComputerName "{}"'.format(name))
os.system('sudo scutil --set HostName "{}"'.format(name))
os.system('sudo scutil --set LocalHostName "{}"'.format(name.replace(' ', '-'))) # Doesn't support spaces
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "{}"'.format(name))
os.system('git config --global user.name "{}"'.format(name))
os.system('git config --global user.email "{}"'.format(email))

# Install Brew & Brew Cask
print("Installing Brew & Brew Cask")
os.system('touch ~/.bash_profile')
os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
os.system('brew tap homebrew/cask-versions')
os.system('brew tap homebrew/cask-fonts')
os.system('brew update && brew upgrade && brew cleanup')


# Install Languages
print("Installing Git+NodeJS")
os.system('brew install git node')
os.system('brew link --overwrite git node')
os.system('brew install git-flow git-lfs svn') # For some reason most fonts require SVN
os.system('git lfs install')

print("Installing Command Line Tools")
os.system('npm install -g node-gyp serve yarn')

#Essentials
print("Installing Essential Apps")
os.system('brew install --cask iterm2 rectangle google-chrome visual-studio-code spotify slack')

print("Installing Fonts")
os.system('brew install font-dosis font-droid-sans-mono-for-powerline font-open-sans font-roboto font-roboto-mono font-roboto-slab font-consolas-for-powerline font-inconsolata font-inconsolata-for-powerline font-lato font-menlo-for-powerline font-meslo-lg font-meslo-for-powerline font-noto-sans font-noto-serif font-source-sans-pro font-source-serif-pro font-ubuntu font-pt-mono font-pt-sans font-pt-serif font-fira-mono font-fira-mono-for-powerline font-fira-code font-fira-sans font-source-code-pro font-hack font-anka-coder font-jetbrains-mono')

# Appropriate Software
if options['developer'] == 'y':
  print("Installing Developer Tools")
  os.system('brew install --cask docker sequel-ace imageoptim xnconvert')
  os.system('curl -o- https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash')
      
if options['android'] == 'y':
  print("Installing Android Tools")
  os.system('brew fetch java')
  show_notification("We need your password")
  os.system('brew install java')
  os.system('brew install --cask android-studio')
  os.system('brew install --cask android-platform-tools')

if options['ios'] == 'y':
  print("Installing iOS Tools")
  show_notification("We need your password")
  os.system('sudo gem install cocoapods')
  show_notification("We need your password")
  os.system('sudo gem install fastlane --verbose')

if options['flutter'] == 'y':
  print("Installing Flutter SDK")
  os.system('brew install --cask flutter')

if options['designer'] == 'y':
  print("Installing Designer Tools")
  os.system('brew install --cask figma')

if options['vim'] == 'y':
  print("Installing VIM + Awesome VIM")
  os.system('brew install vim')
  os.system('git clone https://github.com/amix/vimrc.git ~/.vim_runtime')
  os.system('sh ~/.vim_runtime/install_awesome_vimrc.sh')

# Oh-My-ZSH. Dracula Theme for iTerm2 needs to be installed manually
if options['zsh'] == 'y':
  print("Installing Oh-My-Zsh with Dracula Theme")
  show_notification("We need your password")

  # Setup Adapted from https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh
  if os.system('test -d ~/.oh-my-zsh') != 0:
    os.system('umask g-w,o-w && git clone --depth=1 https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh')
  if os.system('test -f ~/.zshrc') != 0:
    os.system('cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc')

  # If the user has the default .zshrc tune it a bit
  if (subprocess.call(['bash', '-c', 'diff <(tail -n +6 ~/.zshrc) <(tail -n +6  ~/.oh-my-zsh/templates/zshrc.zsh-template) > /dev/null']) == 0):
          
    # Plugins
    os.system('brew install zsh-autosuggestions zsh-syntax-highlighting bat tldr diff-so-fancy')
    os.system('echo "ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE=\\'fg=#777\\'" >> ~/.zshrc')
    os.system('sed -i .zshrc -e "s/plugins=(git)/plugins=(git brew bgnotify zsh-autosuggestions zsh-syntax-highlighting)/"')
    os.system('echo "" >> ~/.zshrc')
    os.system('echo "# syntax-highlighting must be last" >> ~/.zshrc')
    os.system('echo "source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc')
    os.system('echo "" >> ~/.zshrc')
    os.system('echo "source /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc')

    # https://github.com/dracula/dracula-theme
    os.system('echo "" >> ~/.zshrc')
    os.system('echo "# Dracula Theme" >> ~/.zshrc')
    os.system('echo "export ZSH=$HOME/.oh-my-zsh" >> ~/.zshrc')
    os.system('echo "ZSH_THEME=\\'dracula\\'" >> ~/.zshrc')
    os.system('echo "source $ZSH/oh-my-zsh.sh" >> ~/.zshrc')

  os.system('chsh -s $(which zsh)')

# Disable Press-And-Hold for VSCode. This needs to be done in the end, so that VSCode is installed
os.system('defaults write com.microsoft.VSCode ApplePressAndHoldEnabled -bool false')
os.system('defaults write com.microsoft.VSCodeInsiders ApplePressAndHoldEnabled -bool false')
os.system('defaults delete -g ApplePressAndHoldEnabled')

if options['animations'] == 'y':
  print("Accelerating OSX Animations")
  show_notification("We need your password")
  os.system('defaults write -g NSWindowResizeTime -float 0.003')
  os.system('defaults write com.apple.dock autohide-time-modifier -int 0;killall Dock')
  os.system('defaults write com.apple.dock expose-animation-duration -float 0.1; killall Dock')
  os.system('defaults write NSGlobalDomain KeyRepeat -int 0')

if options['showhiddenfiles'] == 'y':
  print("Showing Hidden Files")
  os.system('defaults write com.apple.finder AppleShowAllFiles YES;killall Finder')

if options['autoupdate'] == 'y':
  print("Enable Auto Update")
  show_notification("We need your password")
  os.system('sudo softwareupdate --schedule on')
  os.system('defaults write com.apple.SoftwareUpdate AutomaticCheckEnabled -bool true')
  os.system('defaults write com.apple.SoftwareUpdate AutomaticDownload -int 1')
  os.system('defaults write com.apple.SoftwareUpdate AutomaticallyInstallMacOSUpdates -int 1')
  os.system('defaults write com.apple.commerce AutoUpdate -bool true')
  os.system('defaults write com.apple.commerce AutoUpdateRestartRequired -bool true')


show_notification("Mac setup is complete!")
print("\n\nAll done!\n")

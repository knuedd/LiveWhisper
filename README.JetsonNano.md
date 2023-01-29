# Apply OpenAI Whisper and LiveWhisper on an NVIDIA JetsonNano SoC

## Proper image


## Install

## Install Whisper

Install as described at https://github.com/openai/whisper

You can use the 'tiny' and 'base' models. If only English is fine for you, then the 'tiny.en' and 'base.en' models work a bit faster and need less memory. 
The 'small' and 'small.en' models will fail with out of memory errors more often than not.

## Install LiveWhisper

Prerequisites:

    sudo apt install python3-pyaudio
    #apt install portaudio19-dev

## Remove clutter

Disable services that we don't need to free memory 

    sudo systemctl stop docker.service
    sudo systemctl disable docker.service

    sudo apt remove containerd
    sudo apt remove gnome-online-accounts
    sudo apt remove tracker-miner-fs
    sudo apt remove tracker-extract

    sudo systemctl stop teamviewerd.service
    sudo systemctl disable teamviewerd.service

    sudo systemctl stop cups
    sudo systemctl disable cups
    sudo systemctl stop cups-browsed
    sudo systemctl disable cups-browsed

In addition disable the graphical login if you work with your nano remotely which is recommended anyway to minimize memory usage

    sudo systemctl stop gdm.service
    sudo systemctl disable gdm.service
    sudo systemctl stop gdm3.service
    sudo systemctl disable gdm3.service


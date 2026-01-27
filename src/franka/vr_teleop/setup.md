Refer to https://poe.com/chat/46ka0kn0g2w30hhnri

```
hostname -I
10.13.127.63 100.99.219.35 172.17.0.1 fd7a:115c:a1e0::701:db23
```

This is normal:
```
sudo ufw status 
Status: inactive
```

Verify GelSight Mini works on Ubuntu (before involving Quest)
GelSight Mini often shows up as a normal V4L2 camera device.

Install tools:
```
sudo apt update
sudo apt install -y v4l-utils ffmpeg
```

List cameras:
```
v4l2-ctl --list-devices
```

```
Orbbec Gemini 335: Orbbec Gemin (usb-0000:00:14.0-4):
        /dev/video2
        /dev/video3
        /dev/video4
        /dev/video5
        /dev/media1
        /dev/media2

GelSight Mini R0B 2BUU-CE3E: Ge (usb-0000:00:14.0-9):
        /dev/video0
        /dev/video1
        /dev/media0
```

```
ls -l /dev/video*
```

```
crw-rw----+ 1 root video 81, 0 Jan 26 20:02 /dev/video0
crw-rw----+ 1 root video 81, 1 Jan 26 20:02 /dev/video1
crw-rw-rw-+ 1 root video 81, 2 Jan 26 20:27 /dev/video2
crw-rw-rw-+ 1 root video 81, 3 Jan 26 20:27 /dev/video3
crw-rw-rw-+ 1 root video 81, 4 Jan 26 20:27 /dev/video4
crw-rw-rw-+ 1 root video 81, 5 Jan 26 20:27 /dev/video5
```

Quick preview (replace /dev/videoX):
```
ffplay /dev/videoX
```

```
sudo apt install -y python3.10 python3.10-venv python3.10-dev

python3.10 -m venv rdp_venv
source rdp_venv/bin/activate
python --version   # should say Python 3.10.x
pip install -U pip

# follow their README for torch + requirements
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
pip install -r requirements.txt
```

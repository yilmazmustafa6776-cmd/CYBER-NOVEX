#!/bin/bash
set -e

if [ "$EUID" -ne 0 ]; then
    echo "Please run with sudo"
    exit 1
fi

apt-get update
apt-get install -y git python3 nmap lynis

INSTALL_DIR="/opt/CYBER-NOVEX"

if [ -d "$INSTALL_DIR/.git" ]; then
    git -C "$INSTALL_DIR" pull --ff-only
elif [ -e "$INSTALL_DIR" ]; then
    echo "Installation directory already exists."
    exit 1
else
    git clone https://github.com/yilmazmustafa6776-cmd/CYBER-NOVEX.git "$INSTALL_DIR"
fi

cat > /usr/local/bin/cyber-novex <<'EOF'
#!/bin/bash
cd /opt/CYBER-NOVEX
exec python3 novex.py
EOF

chmod +x /usr/local/bin/cyber-novex

echo "CYBER NOVEX installed successfully!"
echo "Run it using: cyber-novex"

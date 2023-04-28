#!/bin/bash


if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root!" >&2
    exit 1
fi


read -p "Enter the username: " username

# Check if the user already exists
if id "$username" &>/dev/null; then
    echo "User '$username' already exists. Please choose a different username." >&2
    exit 1
fi


useradd -m -s /bin/bash "$username"


echo "Enter the password for the new user:"
passwd "$username"

echo "User '$username' has been created successfully."
